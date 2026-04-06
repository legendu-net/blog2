#!/usr/bin/env python3
# encoding: utf-8
"""Main logic of the blogging system."""

from collections import namedtuple
import datetime
import json
import multiprocessing
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess as sp
import time
from typing import Any, Iterable, Self, Sequence, TypeAlias
import nbformat
from loguru import logger
from tqdm import tqdm
import yaml
from blog.utils import BASE_DIR, qmarks

AnyPath: TypeAlias = str | Path
Number: TypeAlias = int | float
ARTICLES = "articles"
DRAFTS = "drafts"
OUTDATED = "outdated"
DISCLAIMER_DRAFTS = "**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**\n"
DISCLAIMER_OUTDATED = "**Things under legendu.net/outdated are outdated technologies that the author does not plan to update any more. Please look for better alternatives.**\n"
MARKDOWN = ".md"
IPYNB = ".ipynb"
# TODO: move into a function
with Path(BASE_DIR / "words.yml").open(encoding="utf-8") as _:
    WORDS = yaml.load(_, Loader=yaml.FullLoader)
# TODO: move into Record directly and access via .fields
POSTS_COLS = [
    "path",
    "doc_dir",
    "created",
    "date",
    "title",
    "tags",
    "content",
    "empty",
    "match",
]
TAG_SEPARATOR = "|"
SITE = "https://legendu-net.github.io/blog"
Record = namedtuple("Record", POSTS_COLS)


def _parse_record(path: AnyPath):
    return Post(path).parse().record()


def _parse_records() -> list[Record]:
    logger.info("Parsing posts into records ...")
    paths = []
    for doc_dir in (ARTICLES, DRAFTS, OUTDATED):
        for ext in (MARKDOWN, IPYNB):
            paths.extend(BASE_DIR.glob(f"docs/{doc_dir}/20??/??/*/index{ext}"))
    # TODO:
    # with multiprocessing.Pool(processes=1) as pool:
    # return pool.map(_parse_record, paths)
    return [_parse_record(path) for path in paths]


def _format_title(title):
    # TODO: replacement at beginning and end might have bugs
    # it's possible to have the same pattern in the middle
    # and the replacements assumes space as the separator,
    # which might not always be true.
    # it sounds better to use regex.
    # Easier to just update words.json to use regex.
    title = title.title()
    for origin, replace in WORDS:
        title = title.replace(f" {origin} ", f" {replace} ")
        if title.startswith(origin + " "):
            title = title.replace(origin + " ", replace + " ")
        if title.endswith(" " + origin):
            title = title.replace(" " + origin, " " + replace)
    if title.startswith("the "):
        title = "The " + title[4:]
    if title.startswith("a "):
        title = "A " + title[2:]
    return title


def _label(title: str) -> str:
    """Generate a label from the title of the Post.

    :param title: The title to create the slug from.
    :return: A label created from the title.
    """
    title = title.lower()
    hyphen = "-"
    strs = [" ", "/", ",", "(", ")", ":", "=", "?", "!", "“", "”", hyphen * 2]
    for s in strs:
        title = title.replace(s, hyphen)
    return title


class Post:
    """A class abstracting a post."""

    def __init__(self, path: AnyPath):
        self.path: Path = Path()
        self._doc_dir = ""
        self.is_markdown = True
        self.metadata = {}
        self.lines = []
        self.notebook = {}
        self._set_path(path)

    def change_doc_dir(self, doc_dir: str):
        if doc_dir not in (ARTICLES, DRAFTS, OUTDATED):
            raise ValueError(
                f"doc_dir must be one of {ARTICLES}, {DRAFTS} or {OUTDATED}!"
            )
        if doc_dir == self._doc_dir:
            return
        parts = list(self.path.parts)
        parts[1] = doc_dir
        path_new = BASE_DIR.joinpath(*parts)
        dir_new = path_new.parent
        dir_new.mkdir(parents=True, exist_ok=True)
        self.path.parent.move(dir_new)
        self._set_path(path_new)
        self.parse()

    def parse(self) -> Self:
        if self.is_markdown:
            with self.path.open(encoding="utf-8") as fin:
                lines = fin.readlines()
            self.notebook = {}
        else:
            self.notebook = self._read_notebook()
            lines = self.notebook["cells"][0]["source"].copy()
            for cell in self.notebook["cells"][1:]:
                lines.append("<!-- Cell -->")
                lines.extend(cell["source"])
        idx = lines.index("---\n", 1)
        try:
            self.metadata = yaml.load("".join(lines[:idx]), Loader=yaml.FullLoader)
        except Exception as err:
            print(
                "Failed to parse the YAML metadata of the following post!\n",
                self.path,
                sep="",
            )
            for line in lines:
                print(line)
            print()
            raise err
        for idx in range(idx + 1, len(lines)):
            if lines[idx].strip():
                break
        self.lines = lines[idx:]
        self._check_disclaimer()
        return self

    def _is_disclaimer_valid(self) -> tuple[bool, bool]:
        """Check whether the disclaimer is valid, and whether there's a disclaimer."""
        if self.lines[0] == DISCLAIMER_DRAFTS:
            return self._doc_dir == DRAFTS, True
        if self.lines[0] == DISCLAIMER_OUTDATED:
            return self._doc_dir == OUTDATED, True
        return self._doc_dir == ARTICLES, False

    def _check_disclaimer(self):
        if not self.lines:
            return
        valid, has_disclaimer = self._is_disclaimer_valid()
        if has_disclaimer:
            self.lines = self.lines[1:]
        if not valid:
            self._write()

    def _set_path(self, path: AnyPath):
        if isinstance(path, str):
            path = Path(path)
        path = path.resolve()
        if path.suffix not in (MARKDOWN, IPYNB):
            raise ValueError(f"{self.path} is not a {MARKDOWN} or {IPYNB} file.")
        self.path = path.relative_to(BASE_DIR)
        self._doc_dir = self.path.parts[1]
        self.is_markdown = path.suffix == MARKDOWN

    def label(self) -> str:
        if next(iter(self.metadata.keys()), "") == "label":
            return self.metadata["label"]
        return _label(self.metadata["title"])

    def is_match(self) -> bool:
        """Check whether the file anme and the title of the post does not match.

        :param title: The title of the post.
        :return: 1 if mismatch and 0 otherwise.
        """
        return self.label() == self.metadata["label"] and self.metadata["label"] == self.path.parts[4]

    def _write(self):
        if self.is_markdown:
            with self.path.open("w", encoding="utf-8") as fout:
                fout.writelines(self._metadata_lines())
                if self._doc_dir == DRAFTS:
                    fout.write(DISCLAIMER_DRAFTS)
                elif self._doc_dir == OUTDATED:
                    fout.write(DISCLAIMER_OUTDATED)
                fout.writelines(self.lines)
        else:
            cell0 = self.notebook["cells"][0]
            cell0["source"] = self._metadata_lines()
            if self._doc_dir == DRAFTS:
                cell0["source"].append(DISCLAIMER_DRAFTS)
            elif self._doc_dir == OUTDATED:
                cell0["source"].append(DISCLAIMER_OUTDATED)
            self.path.write_text(json.dumps(self.notebook, indent=1), encoding="utf-8")

    def _metadata_lines(self) -> list[str]:
        """Convert the metadata dict into metadata lines."""
        lines = ["---\n"]
        for line in (
            yaml.dump(self.metadata, allow_unicode=True, sort_keys=False)
            .strip()
            .split("\n")
        ):
            lines.append(line + "\n")
        lines.append("---\n")
        return lines

    def _read_notebook(self) -> dict:
        notebook = json.loads(self.path.read_text(encoding="utf-8"))
        if notebook["cells"][0]["cell_type"] != "markdown":
            raise SyntaxError(
                f"The first cell of the notebook {self.path} is not a markdown cell!"
            )
        return notebook

    def _is_post_empty(self) -> int:
        """Check whether the post is essentially empty."""
        return all(line.strip() == "" for line in self.lines)

    def format_tags(self) -> str:
        return TAG_SEPARATOR + TAG_SEPARATOR.join(self.metadata["tags"]) + TAG_SEPARATOR

    def record(self) -> Record:
        tags = self.format_tags()
        content = self.metadata["title"] + "\n" + tags + "\n" + "".join(self.lines)
        return Record(
            str(self.path),
            self._doc_dir,
            self.metadata["created"],
            self.metadata["date"],
            self.metadata["title"],
            tags,
            content,
            self._is_post_empty(),
            int(self.is_match()),
        )

    def update_meta_field(self, metadata: dict[str, Any]) -> None:
        """Update metadata. The date field is automatically updated."""
        self.metadata.update(metadata)
        self.metadata["date"] = (
            datetime.datetime.now()
            if metadata
            else datetime.datetime.fromtimestamp(self.path.stat().st_mtime)
        )
        self._write()

    def update_tags(self, from_tag: str, to_tag: str) -> bool:
        tags = self.metadata["tags"]
        if not (from_tag in tags or "" in tags):
            return False
        tags = [t for tag in tags if (t := to_tag if tag == from_tag else tag)]
        self.update_meta_field(metadata={"tags": tags})
        return True

    def match_title(self) -> None:
        """Make the post's slug and path name match its title."""
        label_new = self.label()
        self.update_meta_field(
            {
                "label": label_new,
            }
        )
        dir_ = self.path.parent
        dir_new = dir_.with_name(label_new)
        dir_.move(dir_new)
        self._set_path(dir_new / self.path.name)

    def _add_markdown_cell(self, index: int = -1, source: list[str] | None = None):
        """Add an empty markdown cell."""
        cell = nbformat.versions[nbformat.current_nbformat].new_markdown_cell()  # ty: ignore[unresolved-attribute]
        if source:
            cell["source"] = self.lines
        self.notebook["cells"].insert(index, cell)

    def _new_notebook(self):
        """Create a new notebook with an empty metadata (markdown) cell."""
        self.notebook = nbformat.versions[nbformat.current_nbformat].new_notebook()
        self._add_markdown_cell()
        if self._doc_dir in (DRAFTS, OUTDATED):
            self._add_markdown_cell()

    def create(self, metadata_or_title: dict[str, Any] | str):
        if isinstance(metadata_or_title, str):
            metadata_or_title = {
                "title": _format_title(metadata_or_title),
                "created": datetime.datetime.now(),
                "date": datetime.datetime.now(),
                "authors": ["bendu"],
                "label": _label(metadata_or_title),
                "license": "CC-BY-4.0",
                "tags": ["computer science", "programming"],
            }
        self.metadata = metadata_or_title
        self.lines = []
        self._new_notebook()
        self._write()

    def convert(self) -> Path:
        """Convert a markdown post to a notebook blog, vice versa."""
        if self.is_markdown:
            self._new_notebook()
            self._add_markdown_cell(source=self.lines)
            path_new = self.path.with_suffix(".ipynb")
        else:
            path_new = self.path.with_suffix(".md")
        self.path.rename(path_new)
        self._set_path(path_new)
        self._write()
        return path_new


class Blogger:
    """A class for managing blog."""

    POSTS = "posts"
    SRPS = "srps"
    ACCESSED = "accessed"
    SRPS_COLS = "path, title, doc_dir"
    ACCESSED_COLS = "path, atime"

    def __init__(self, db: str = ""):
        """Create an instance of Blogger.

        :param dir_: the root directory of the blog.
        :param db: the path to the SQLite3 database file.
        """
        self._db = db if db else str(BASE_DIR / ".blogger.sqlite3")
        self._conn = sqlite3.connect(self._db)
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._create_vtable_posts()
        self._create_table_srps()
        self._create_table_accessed()

    def _create_vtable_posts(self):
        sql = f"""
            CREATE VIRTUAL TABLE IF NOT EXISTS {self.POSTS} USING fts5 (
                {", ".join(POSTS_COLS)},
                tokenize = porter
            )
            """
        self._conn.execute(sql)

    def _create_table_srps(self):
        sql = f"CREATE TABLE IF NOT EXISTS {self.SRPS} ({self.SRPS_COLS})"
        self._conn.execute(sql)

    def _create_table_accessed(self):
        sql = f"CREATE TABLE IF NOT EXISTS {self.ACCESSED} ({self.ACCESSED_COLS})"
        self._conn.execute(sql)

    def clean_db(self):
        """Remove the SQLite3 database."""
        os.remove(self._db)

    def commit(self):
        """Commit changes made to the SQLite3 database."""
        self._conn.commit()

    def reload_posts(self):
        """Reload posts into the SQLite3 database."""
        self.delete_records(self.POSTS, "")
        records = _parse_records()
        logger.info("Inserting records into SQLite3 ...")
        batch = 1000
        for i in tqdm(range(0, len(records), batch)):
            self.load_records(records[i : i + batch])

    def load_records(self, records: Iterable[Record]):
        # TODO: can be unified with load_post, use just 1 function
        sql = f"""
            INSERT INTO {self.POSTS} (
                {", ".join(POSTS_COLS)}
            ) VALUES (
                {qmarks(POSTS_COLS)}
            )
            """
        self._conn.executemany(sql, records)

    def load_post(self, post: Post):
        sql = f"""
            INSERT INTO {self.POSTS} (
                {", ".join(POSTS_COLS)}
            ) VALUES (
                {qmarks(POSTS_COLS)}
            )
            """
        self._conn.execute(sql, post.record())

    def trash(self, paths: str | list[str]):
        """Move the specified posts to the trash directory.

        :param paths: Paths of posts to be removed.
        """
        if isinstance(paths, AnyPath):
            paths = [paths]
        dir_ = BASE_DIR / "trash"
        if not dir_.is_dir():
            dir_.mkdir(0o700, True, True)
        for path in paths:
            shutil.move(path, dir_)
        self.delete_records(table=self.POSTS, paths=paths)

    def delete_records(self, table: str, paths: str | list[str]) -> None:
        """Delete records from a table.

        :param paths: Paths correspond to records to delete.
            If a trivia value ("" or []) is specified,
            then all records are deleted from the table.
        """
        sql = f"DELETE FROM {table} "
        if not paths:
            self._conn.execute(sql)
            return
        if isinstance(paths, AnyPath):
            paths = [paths]
        sql += f"WHERE path IN ({qmarks(paths)})"
        self._conn.execute(sql, paths)

    def move(self, paths: AnyPath | Sequence[AnyPath], doc_dir: str) -> None:
        """Move specified posts into a destination directory.

        :param paths: A (sequence of) path(s).
        :param dst: The destination path or directory to move posts to.
        """
        if isinstance(paths, AnyPath):
            paths = [paths]
        for path in paths:
            post = Post(path)
            post.change_doc_dir(doc_dir)
            self.update_records(
                table=self.POSTS,
                paths=path,
                kvs={"path": post.path, "doc_dir": doc_dir},
            )

    def match_title(self, post: str | Post) -> None:
        if isinstance(post, str):
            post = Post(post).parse()
        if post.is_match():
            print(
                "The lable and title of the following post already matches.\n    ",
                post.path,
                "\n",
                sep="",
            )
            return
        path_old = str(post.path)
        post.match_title()
        kvs: dict[str, str | datetime.datetime | int] = {
            "path": str(post.path),
        }
        self.update_records(table=self.SRPS, paths=path_old, kvs=kvs)
        kvs["date"] = post.metadata["date"]
        kvs["match"] = 1
        self.update_records(table=self.POSTS, paths=path_old, kvs=kvs)

    def update_tags(self, post: str | Post, from_tag: str, to_tag: str) -> None:
        if isinstance(post, str):
            post = Post(post).parse()
        if post.update_tags(from_tag, to_tag):
            self.update_records(
                table=self.POSTS,
                paths=post.path,
                kvs={"tags": post.format_tags()},
            )

    def insert_records(self, table: str, fields: str | list[str], values: list[Any]):
        if not isinstance(fields, str):
            fields = ", ".join(fields)
        sql = f"""
            INSERT INTO {table} (
                {fields}
            ) VALUES (
                {qmarks(fields)}
            )
            """
        self._conn.executemany(sql, values)

    def edit(self, paths: str | list[str], editor: str) -> None:
        """Edit the specified posts using the specified editor."""
        if isinstance(paths, str):
            paths = [paths]
        self.delete_records(self.ACCESSED, paths=paths)
        self.insert_records(
            self.ACCESSED,
            self.ACCESSED_COLS,
            [(path, Path(path).stat().st_atime) for path in paths],
        )
        paths = " ".join(f"'{path}'" for path in paths)
        sp.run(f"{editor} {paths}", shell=True, check=True)

    def update_records(
        self, table: str, paths: AnyPath | list[AnyPath], kvs: dict
    ) -> None:
        """Update records corresponding to the specified paths.
        :param kvs: A dictionary of the form dict[field, value].
        :param paths: Paths of records to be updated.
        """
        if isinstance(paths, AnyPath):
            paths = [paths]
        sql = f"""
            UPDATE {table}
            SET {", ".join(f"{k} = ?" for k in kvs)} 
            WHERE path in ({qmarks(paths)})
            """
        self._conn.execute(sql, list(kvs.values()) + paths)

    def update_changed(self):
        """Update information of the changed posts."""
        SECONDS_4_HOURS = 4 * 3600
        for path, atime in self._conn.execute(
            f"SELECT {self.ACCESSED_COLS} FROM {self.ACCESSED}"
        ):
            p = Path(path)
            if not p.exists():
                self.delete_records(self.ACCESSED, paths=path)
                continue
            if p.stat().st_mtime > atime:
                self.delete_records(self.POSTS, path)
                post = Post(path).parse()
                post.update_meta_field(metadata={})
                self.load_post(post)
                self.update_records(
                    self.ACCESSED, paths=path, kvs={"atime": time.time() + 1}
                )
            elif time.time() - atime >= SECONDS_4_HOURS:
                self.delete_records(self.ACCESSED, path)

    def add_post(self, title: str, doc_dir: str, notebook: bool = True) -> str:
        """Add a new post with the given title."""
        label = _label(title)
        paths = self.path(
            self.POSTS,
            where="path LIKE ?",
            params=[f"%/{label}/index.%"],
        )
        if paths:
            print(f"\nA post with the specified title already exists.\n{paths[0]}\n")
            return paths[0]
        yyyymm = datetime.date.today().strftime("%Y/%m")
        dir_ = Path("docs") / doc_dir / yyyymm / label
        dir_.mkdir(parents=True, exist_ok=False)
        path = dir_ / ("index" + (IPYNB if notebook else MARKDOWN))
        post = Post(path)
        post.create(title)
        self.load_post(post)
        print("\nThe following post is added.\n", path, "\n", sep="")
        return str(path)

    def convert(self, path: AnyPath) -> None:
        path_new = Post(path).convert()
        self.update_records(table=self.POSTS, paths=path, kvs={"path": path_new})

    def empty_posts(self) -> None:
        """Load all empty posts into the table srps."""
        self.reload_posts()
        self._srps(where="empty = 1")

    def find_mismatch(self):
        self._srps(where="match = 0")

    def _srps(self, where: str, order_by: str = "", limit: int = 0) -> None:
        self.delete_records(self.SRPS, "")
        sql = f"""
            INSERT INTO {self.SRPS}
            SELECT {self.SRPS_COLS}
            FROM {self.POSTS}
            {"WHERE " + where if where else ""}
            {"ORDER BY " + order_by if order_by else ""}
            {f"LIMIT {limit}" if limit else ""}
            """
        self._conn.execute(sql)

    def search(self, phrase: str, filter_: str = ""):
        """Search for posts containing the phrase.

        :param phrase: The phrase to search for in posts.
        :param filter_: Extra filtering conditions.
        """
        conditions = []
        if phrase:
            conditions.append(f"posts MATCH '{phrase}'")
        if filter_:
            conditions.append(filter_)
        self._srps(where=" AND ".join(conditions), order_by="rank")

    def last(self, n: int):
        """Get last (according to modification time) n posts.
        :param n: The number of posts to get.
        """
        self._srps(where="", order_by="date DESC", limit=n)

    def path(
        self, table: str, where: str, params: Sequence[str | int] = ()
    ) -> list[str]:
        """Get paths correspondings to indexes in the srps table."""
        sql = f"""
            SELECT path FROM {table}
            {"WHERE " + where if where else ""}
            """
        return [row[0] for row in self._conn.execute(sql, params)]

    def tags(self, where: str = ""):
        """Get all tags and their frequencies in all posts.

        :param where: A filtering condition.
        """
        tags = {}
        sql = f"""
            SELECT tags FROM {self.POSTS}
            {"WHERE " + where if where else ""}
            """
        for row in self._conn.execute(sql):
            for tag in row[0].strip(TAG_SEPARATOR).split(TAG_SEPARATOR):
                tags.setdefault(tag, 0)
                tags[tag] += 1
        return sorted(tags.items(), key=lambda pair: pair[1], reverse=True)

    def num_srps(self) -> int:
        row = self._conn.execute(f"SELECT count(*) FROM {self.SRPS}").fetchone()
        return row[0]

    def show(self, n: int) -> None:
        print("\nNumber of matched posts:", self.num_srps())
        for row in self._conn.execute(
            f"SELECT rowid, path, title, doc_dir FROM {self.SRPS} LIMIT {n}"
        ):
            rowid, path, title, doc_dir = row
            parts = list(Path(path).parts[0:5])
            parts[0] = SITE
            url = "/".join(parts)
            print(f"\n{rowid}: [{title}]( {url} )  |  {path}")
        print("")
