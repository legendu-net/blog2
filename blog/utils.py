"""Utils for the blog module."""

from typing import Sequence
import os
from pathlib import Path
import shutil
import subprocess as sp

BASE_DIR = Path(__file__).resolve().parent.parent


def get_vim() -> str:
    return "nvim" if shutil.which("nvim") else "vim"


def get_code() -> str:
    return "code-server" if shutil.which("code-server") else "code"


def get_editor() -> str:
    """Get the path of a valid editor (default to get_vim())."""
    code = get_code()
    if shutil.which(code):
        return code
    return get_vim()


def qmarks(n: int | Sequence) -> str:
    """Generate n question marks delimited by comma."""
    if isinstance(n, int):
        return ", ".join(["?"] * n)
    if isinstance(n, str):
        return qmarks(n.count(",") + 1)
    return qmarks(len(n))


def _github_repos_url(dir_: str, https: bool = False) -> str:
    repos = {
        "home": "dclong.github.io",
        "en": "en",
        "cn": "cn",
        "misc": "misc",
        "outdated": "outdated",
    }[dir_]
    if https:
        return f"https://github.com/dclong/{repos}.git"
    return f"git@github.com:dclong/{repos}.git"


def option_indexes(subparser):
    """Add the positional option "indexes".

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "indexes",
        nargs="*",
        type=int,
        default=(),
        help="Row IDs in the search results.",
    )


def option_files(subparser):
    """Add the option --files.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "--files", nargs="+", dest="filels", default=(), help="Paths to files."
    )


def option_where(subparser):
    """Add the option --where.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-w",
        "--where",
        dest="where",
        default="",
        help="A user-specified filtering condition.",
    )


def option_dir(subparser):
    """Add the option --doc-dir.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-d",
        "--doc-dir",
        dest="doc_dir",
        default="",
        help="The doc directory to searching/querying operations.",
    )


def option_num(subparser):
    """Add the option -n.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-n", dest="n", type=int, default=5, help="Number of matched records to show."
    )


def option_from(subparser):
    """Add the option --from.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "--from", dest="from", default="", help="The tag to change from."
    )


def option_to(subparser):
    """Add the option --to.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument("--to", dest="to", default="", help="The tag to change to.")


def option_full_path(subparser):
    """Add the option --full-path.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-F",
        "--full-path",
        dest="full_path",
        action="store_true",
        help="whether to show full (instead of short/relative) path.",
    )


def option_editor(subparser):
    """Add the option --editor.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-v",
        "--vim",
        dest="editor",
        action="store_const",
        const=get_vim(),
        default=get_editor(),
        help="Edit the post using NeoVim/Vim.",
    )
    subparser.add_argument(
        "--code",
        "--vscode",
        dest="editor",
        action="store_const",
        const=get_code(),
        help="Edit the post using Code Server/VSCode.",
    )


def option_all(subparser):
    """Add the option --all.

    :param subparser: A sub parser for command-line options.
    """
    subparser.add_argument(
        "-a",
        "--all",
        dest="all",
        action="store_true",
        help="Select all files in the search results.",
    )


def gen_toc(path: str | Path = BASE_DIR / "docs/toc.yml") -> None:
    mapping = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec",
    }

    def _gen_toc_month(dir_: str, year: str, month: str):
        path = Path(f"docs/{dir_}/{year}/{month}")
        if any(True for _ in path.glob("*/index.md")):
            if any(True for _ in path.glob("*/index.ipynb")):
                return f"""
            - title: "{mapping[month]}"
              children:
                - pattern: {dir_}/{year}/{month}/*/*.md
                - pattern: {dir_}/{year}/{month}/*/*.ipynb"""
            else:
                return f"""
            - title: "{mapping[month]}"
              children:
                - pattern: {dir_}/{year}/{month}/*/*.md"""
        else:
            if any(True for _ in path.glob("*/index.ipynb")):
                return f"""
            - title: "{mapping[month]}"
              children:
                - pattern: {dir_}/{year}/{month}/*/*.ipynb"""
            else:
                return ""
        path.glob()

    def _gen_toc_year(dir_: str, year: str):
        path = Path(f"docs/{dir_}/{year}")
        months = sorted((p.name for p in path.glob("??/")), reverse=True)
        return f"""
        - title: "{year}"
          children:""" + "".join(
            _gen_toc_month(dir_, year, month) for month in months
        )

    def _gen_toc_dir(dir_: str):
        path = Path(f"docs/{dir_}")
        years = sorted((p.name for p in path.glob("????/")), reverse=True)
        return f"""
    - title: "{dir_.capitalize()}"
      children:""".strip("\n") + "".join(_gen_toc_year(dir_, year) for year in years)

    text = "\n".join([
            "version: 1",
            "project:",
            "  toc:",
            "    - file: index.md",
            _gen_toc_dir("articles"),
            _gen_toc_dir("drafts"),
            _gen_toc_dir("outdated"),
    ])
    if isinstance(path, str):
        path = Path(path)
    path.write_text(text)
