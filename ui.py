#!.venv/bin/python3
from argparse import ArgumentParser, Namespace
import getpass
import subprocess as sp
from loguru import logger
from blog.utils import (
    BASE_DIR,
    gen_toc,
    get_vim,
    qmarks,
    option_files,
    option_indexes,
    option_where,
    option_dir,
    option_num,
    option_from,
    option_to,
    option_editor,
    option_all,
    option_full_path,
)
from blog.blogger import Post, Blogger, ARTICLES, DRAFTS, OUTDATED, TAG_SEPARATOR

USER = getpass.getuser()
DASHES = "\n" + "-" * 100 + "\n"


def move(blogger, args):
    _resolve_files(args)
    if args.files:
        blogger.move(args.files, args.target)
    blogger.commit()


def _resolve_files(args: Namespace) -> None:
    if "all" in args and args.all:
        args.files = blogger.path(Blogger.SRPS, where="")
        return
    if "indexes" in args and args.indexes:
        args.files = blogger.path(
            Blogger.SRPS,
            where=f"rowid IN ({qmarks(args.indexes)})",
            params=args.indexes,
        )


def trash(blogger, args):
    _resolve_files(args)
    if args.files:
        for index, file in enumerate(args.files):
            print(f"\n{index}: {file}")
        answer = input(
            "\nAre you sure to delete the specified files in the srps table (y/N): "
        )
        if answer.lower() in ("y", "yes"):
            blogger.trash(args.files)
    else:
        print("No file to delete is specified!\n")
    blogger.commit()


def _subparse_trash(subparsers):
    desc = "Move posts to the trash directory."
    subparser_trash = subparsers.add_parser(
        "trash", aliases=["rm"], help=desc, description=desc
    )
    option_indexes(subparser_trash)
    option_all(subparser_trash)
    option_files(subparser_trash)
    subparser_trash.set_defaults(func=trash)


def find_label_title_mismatch(blogger, args):
    blogger.find_label_title_mismatch()
    blogger.show(args.n)


def _subparse_find_label_title_mismatch(subparsers):
    desc = "Find posts where their label and title are mismatched."
    subparser_find_label_title_mismatch = subparsers.add_parser(
        "findmismatch",
        aliases=["fm"],
        help=desc,
        description=desc,
    )
    option_num(subparser_find_label_title_mismatch)
    option_full_path(subparser_find_label_title_mismatch)
    subparser_find_label_title_mismatch.set_defaults(func=find_label_title_mismatch)


def match_title(blogger, args):
    _resolve_files(args)
    if not args.files:
        print("No specifed files to update labels to match titles!\n")
        return
    for file in args.files:
        blogger.match_title(file)


def vim(blogger, args):
    args.editor = get_vim()
    edit(blogger, args)


def edit(blogger, args):
    _resolve_files(args)
    if args.files:
        blogger.edit(args.files, args.editor)
    else:
        print("No post is specified for editing!\n")
    blogger.commit()


def search(blogger, args):
    blogger.update_changed()
    filter_ = []
    if args.filter:
        filter_.append(" ".join(args.filter))
    if args.doc_dir:
        dirs = ", ".join(f"'{d}'" for d in args.doc_dir)
        filter_.append(f"doc_dir IN ({dirs})")
    if args.tags:
        tags = " ".join(args.tags)
        filter_.append(f"tags MATCH '{tags}'")
    if args.title:
        args.title = " ".join(args.title)
        filter_.append(f"title MATCH '{args.title}'")
    blogger.search(" ".join(args.phrase), " AND ".join(filter_))
    blogger.show(args.n)
    blogger.commit()


def last(blogger, args):
    blogger.last(args.n)
    blogger.show(args.n)


def add(blogger, args):
    file = blogger.add_post(" ".join(args.title), args.doc_dir, notebook=args.notebook)
    blogger.edit(file, args.editor)
    blogger.search(phrase="", filter_=f"path = '{file}'")
    blogger.show(1)
    blogger.commit()


def update_tags(blogger, args):
    _resolve_files(args)
    if args.files:
        for file in args.files:
            blogger.update_tags(Post(file), args.from_tag, args.to_tag)
    else:
        for path in blogger.path(
            blogger.POSTS,
            where=f"tags LIKE '%{TAG_SEPARATOR}{args.from_tag}{TAG_SEPARATOR}%'",
        ):
            blogger.update_tags(Post(path), args.from_tag, args.to_tag)
    blogger.commit()


def tags(blogger, args):
    tags = blogger.tags(where=args.where)
    for tag in tags:
        print(tag)


def auto_git_push(blogger, args):
    """Push changes in this repository."""
    blogger.update_changed()
    gen_toc()
    cmd = f"""git -C {BASE_DIR} add . \
            && git -C {BASE_DIR} commit -m ..."""
    sp.run(cmd, shell=True, check=False)
    cmd = f"""git -C {BASE_DIR} push origin main"""
    sp.run(cmd, shell=True, check=True)


def clean_db(blogger, _):
    blogger.clean_db()


def exec_notebook(blogger, args):
    # TODO:
    _resolve_files(args)
    # TODO: rename to files?
    if args.indexes:
        args.notebooks = blogger.path(args.indexes)
    if args.notebooks:
        cmd = [
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--inplace",
            "--execute",
        ] + args.notebooks
        sp.run(cmd, check=True)


def format_notebook(_, args):
    # TODO: is this necessary?
    # Can you use ruff to format notebooks? And if so, you can do this directly, right?
    # _resolve_files(args)
    cmd = f"black {BASE_DIR}"
    sp.run(cmd, shell=True, check=True)


def _subparse_format_notebook(subparsers):
    desc = "Format notebooks."
    subparser_format_notebook = subparsers.add_parser(
        "format_notebook",
        aliases=["format", "fmt", "f"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_format_notebook)
    option_files(subparser_format_notebook)
    option_all(subparser_format_notebook)
    subparser_format_notebook.set_defaults(func=format_notebook)


def _subparse_trust_notebooks(subparsers):
    desc = "Trust notebooks."
    subparsers.add_parser(
        "trust_notebooks",
        aliases=["trust"],
        help=desc,
        description=desc,
    )


def _subparse_exec_notebook(subparsers):
    desc = "Execute a notebook."
    subparser_exec_notebook = subparsers.add_parser(
        "exec_notebook",
        aliases=["exec"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_exec_notebook)
    option_files(subparser_exec_notebook)
    subparser_exec_notebook.set_defaults(func=exec_notebook)


def _subparse_clean_db(subparsers):
    desc = "Remove the underlying SQLite3 database."
    subparser_clean_db = subparsers.add_parser(
        "clean_db",
        help=desc,
        description=desc,
    )
    subparser_clean_db.set_defaults(func=clean_db)


def _subparse_utag(subparsers):
    desc = "update tags of posts."
    subparser_utag = subparsers.add_parser(
        "update_tags",
        aliases=["utag"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_utag)
    option_files(subparser_utag)
    option_from(subparser_utag)
    option_to(subparser_utag)
    subparser_utag.set_defaults(func=update_tags)


def _subparse_tags(subparsers):
    desc = "List all tags and their frequencies."
    subparser_tags = subparsers.add_parser(
        "tags",
        aliases=["t"],
        help=desc,
        description=desc,
    )
    option_where(subparser_tags)
    option_dir(subparser_tags)
    subparser_tags.set_defaults(func=tags)


def reload_posts(blogger, _):
    blogger.reload_posts()
    blogger.commit()


def _subparse_reload_posts(subparsers):
    desc = "Reload information of posts."
    subparser_reload = subparsers.add_parser(
        "reload_posts",
        aliases=["reload", "r"],
        help=desc,
        description=desc,
    )
    subparser_reload.set_defaults(func=reload_posts)


def _subparse_last(subparsers):
    desc = "List recently changed posts."
    subparser_last = subparsers.add_parser(
        "last",
        aliases=[],
        help=desc,
        description=desc,
    )
    option_num(subparser_last)
    option_full_path(subparser_last)
    subparser_last.set_defaults(func=last)


def _subparse_list(subparsers):
    desc = "List last search results."
    subparser_list = subparsers.add_parser(
        "list",
        aliases=["l"],
        help=desc,
        description=desc,
    )
    option_num(subparser_list)
    option_full_path(subparser_list)
    subparser_list.set_defaults(func=lambda blogger, args: blogger.show(args.n))


def _subparse_search(subparsers):
    desc = (
        "Search for posts. "
        "Tokens separated by spaces ( ) or plus signs (+) in the search phrase "
        "are matched in order with tokens in the text. "
        "ORDERLESS match of tokens can be achieved by separating them with the AND keyword. "
        "You can also limit match into specific columns. "
        "For more information, please refer to https://sqlite.org/fts5.html"
    )
    subparser_search = subparsers.add_parser(
        "search",
        aliases=["s"],
        help=desc,
        description=desc,
    )
    subparser_search.add_argument(
        "phrase",
        nargs="*",
        default=(),
        help="The phrase to match in posts. "
        "The phrase is optional. "
        "For example if you want to filter by category only without constraints on full-text search, "
        "you can use ./blog.py s the -c some_category.",
    )
    subparser_search.add_argument(
        "-i",
        "--title",
        nargs="+",
        dest="title",
        default=(),
        help="Search for posts with the sepcified title.",
    )
    subparser_search.add_argument(
        "-t",
        "--tags",
        nargs="+",
        dest="tags",
        default=(),
        help="Search for posts with the sepcified tags.",
    )
    subparser_search.add_argument(
        "-d",
        "--doc-dir",
        dest="doc_dir",
        nargs="+",
        default=(),
        help="Search for posts in the specified sub blog directory.",
    )
    subparser_search.add_argument(
        "-f",
        "--filter",
        dest="filter",
        nargs="+",
        default=(),
        help="Futher filtering conditions in addition to the full-text match.",
    )
    option_num(subparser_search)
    option_full_path(subparser_search)
    subparser_search.set_defaults(func=search)


def _subparse_add(subparsers):
    desc = "Add a new post."
    subparser_add = subparsers.add_parser(
        "add", aliases=["a"], help=desc, description=desc
    )
    option_editor(subparser_add)
    subparser_add.add_argument(
        "-a",
        "--articles",
        dest="doc_dir",
        action="store_const",
        const=ARTICLES,
        default=DRAFTS,
        help="Create a post in the en sub blog directory.",
    )
    group = subparser_add.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-m",
        "--markdown",
        dest="notebook",
        action="store_false",
        help="Create a MarkDown (default Notebook) post.",
    )
    group.add_argument(
        "-n",
        "--notebook",
        "--ipynb",
        dest="notebook",
        action="store_true",
        help="Create a MarkDown (default Notebook) post.",
    )
    subparser_add.add_argument(
        "title", nargs="+", help="Title of the post to be created."
    )
    subparser_add.set_defaults(func=add)


def _subparse_vim(subparsers):
    desc = "Edit a post using Vim."
    subparser_vim = subparsers.add_parser(
        "vim",
        aliases=["v"],
        help=desc,
        description=desc,
    )
    subparser_vim.add_argument(
        "indexes", nargs="*", type=int, help="Row IDs in the search results."
    )
    subparser_vim.add_argument(
        "-f",
        "--files",
        nargs="+",
        default=[],
        dest="files",
        help="Path of the post to be edited.",
    )
    subparser_vim.set_defaults(func=vim)


def _subparse_edit(subparsers):
    desc = "Edit a post."
    subparser_edit = subparsers.add_parser(
        "edit",
        aliases=["e"],
        help=desc,
        description=desc,
    )
    subparser_edit.add_argument(
        "indexes", nargs="*", type=int, help="Row IDs in the search results."
    )
    option_editor(subparser_edit)
    subparser_edit.add_argument(
        "-f",
        "--files",
        nargs="+",
        default=[],
        dest="files",
        help="Path of the post to be edited.",
    )
    subparser_edit.set_defaults(func=edit)


def _subparse_move(subparsers):
    desc = "Move a post."
    subparser_move = subparsers.add_parser(
        "move",
        aliases=["m"],
        help=desc,
        description=desc,
    )
    subparser_move.add_argument(
        "indexes", type=int, nargs="*", help="Rowid in the search results."
    )
    subparser_move.add_argument(
        "-f", "--files", nargs="*", dest="files", help="Path of the post to be moved."
    )
    subparser_move.add_argument(
        "-t", "--target", dest="target", default=DRAFTS, help="Path of destination file"
    )
    subparser_move.add_argument(
        "-a",
        "--articles",
        dest="target",
        action="store_const",
        const=ARTICLES,
        help="Move to the articles sub blog directory.",
    )
    subparser_move.add_argument(
        "-d",
        "--drafts",
        dest="target",
        action="store_const",
        const=DRAFTS,
        help="Move to the drafts sub blog directory.",
    )
    subparser_move.add_argument(
        "-o",
        "--out",
        "--outdated",
        dest="target",
        action="store_const",
        const=OUTDATED,
        help="Move to the outdated sub blog directory.",
    )
    subparser_move.set_defaults(func=move)


def _subparse_match_title(subparsers):
    desc = "match post name and title"
    subparser_match_post = subparsers.add_parser(
        "matchpost",
        aliases=["mp"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_match_post)
    option_all(subparser_match_post)
    subparser_match_post.set_defaults(func=match_title)


def _subparse_auto(subparsers):
    desc = "Auto push the Git repository."
    subparser_auto = subparsers.add_parser(
        "auto_git_push",
        aliases=["auto", "agp", "ap"],
        help=desc,
        description=desc,
    )
    subparser_auto.set_defaults(func=auto_git_push)


def _subparse_git_status(subparsers):
    desc = "The git status command."
    subparser_status = subparsers.add_parser(
        "status",
        aliases=["st", "sts"],
        help=desc,
        description=desc,
    )
    subparser_status.set_defaults(func=_git_status)


def _subparse_git_diff(subparsers):
    desc = "The git diff command."
    subparser_git = subparsers.add_parser(
        "diff",
        aliases=["df", "dif"],
        help=desc,
        description=desc,
    )
    subparser_git.add_argument(
        "file", nargs="*", default=(), help="Path of the post to run git diff on."
    )
    subparser_git.set_defaults(func=_git_diff)


def _git_status(_, __):
    sp.run("git status", shell=True, check=True)


def _git_diff(_, args):
    sp.run(f"git diff {' '.join(args.file)}", shell=True, check=True)


def _git_pull(blogger, args):
    logger.info("Pulling origin/main ...")
    sp.run("git pull origin main && git status", shell=True, check=True)
    reload_posts(blogger, args)


def _subparse_git_pull(subparsers):
    desc = "The git pull command."
    subparser_status = subparsers.add_parser(
        "pull",
        aliases=["pu"],
        help=desc,
        description=desc,
    )
    subparser_status.set_defaults(func=_git_pull)


def empty_posts(blogger, args):
    blogger.empty_posts()
    blogger.show(args.n)


def _subparse_empty_posts(subparsers):
    desc = "Find empty post."
    subparser_status = subparsers.add_parser(
        "empty",
        aliases=["em"],
        help=desc,
        description=desc,
    )
    option_num(subparser_status)
    option_full_path(subparser_status)
    subparser_status.set_defaults(func=empty_posts)


def convert(blogger, args):
    _resolve_files(args)
    if args.files:
        for file in args.files:
            blogger.convert(file)


def _subparse_convert(subparsers):
    desc = "Convert markdown/notebook to notebooks/markdown."
    subparser_convert = subparsers.add_parser(
        "convert",
        aliases=["conv"],
        help=desc,
        description=desc,
    )
    option_indexes(subparser_convert)
    option_files(subparser_convert)
    subparser_convert.set_defaults(func=convert)


def parse_args(args=None, namespace=None) -> Namespace:
    """Parse command-line arguments.

    :param args: The arguments to parse.
        If None, the arguments from command-line are parsed.
    :param namespace: An inital Namespace object.
    :return: A namespace object containing parsed options.
    """
    parser = ArgumentParser(description="Write blog in command line.")
    subparsers = parser.add_subparsers(dest="sub_cmd", help="Sub commands.")
    _subparse_utag(subparsers)
    _subparse_tags(subparsers)
    _subparse_reload_posts(subparsers)
    _subparse_list(subparsers)
    _subparse_last(subparsers)
    _subparse_search(subparsers)
    _subparse_add(subparsers)
    _subparse_edit(subparsers)
    _subparse_vim(subparsers)
    _subparse_move(subparsers)
    _subparse_auto(subparsers)
    _subparse_clean_db(subparsers)
    _subparse_git_status(subparsers)
    _subparse_git_diff(subparsers)
    _subparse_git_pull(subparsers)
    _subparse_empty_posts(subparsers)
    _subparse_trash(subparsers)
    _subparse_find_label_title_mismatch(subparsers)
    _subparse_match_title(subparsers)
    _subparse_exec_notebook(subparsers)
    _subparse_format_notebook(subparsers)
    _subparse_trust_notebooks(subparsers)
    _subparse_convert(subparsers)
    return parser.parse_args(args=args, namespace=namespace)


if __name__ == "__main__":
    blogger = Blogger()
    args = parse_args()
    args.func(blogger, args)
