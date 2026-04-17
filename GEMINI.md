# GEMINI.md - Project Context

## Project Overview

This is **Ben Du's Personal Blogging System**, a custom-built infrastructure for managing and publishing blog posts. It is based on **Jupyter Book 2** and uses **MyST Markdown** for content.

The project consists of:

- A **Python-based CLI tool** (`blog.py` and `blogger.py`) for managing blog posts (searching, querying, and potentially processing records).
- A documentation structure under `docs/` following Jupyter Book conventions (`myst.yml`, `toc.yml`, `index.md`).
- Support for various post types: `articles`, `drafts`, and `outdated`.
- Metadata management using SQLite and YAML for "spells" (title/tag corrections).

### Main Technologies

- **Python 3.14+**
- **Jupyter Book 2** & **MyST Markdown**
- **SQLite** (for indexing/searching posts)
- **BeautifulSoup4** (for HTML parsing/scraping)
- **Loguru** (for logging)
- **nbformat** (for handling Jupyter Notebooks)
- **uv** (for Python package management)

## Building and Running

The project uses `uv` for dependency management.

### Setup

```bash
uv sync
```

### Blog Management (CLI)

The `blog.py` script serves as the main entry point for blog operations.

- **Help:** `./blog.py -h` which shows sub-command and corresponding descriptions.
- **Help on a sub-command:** `./blog.py subcmd -h` which shows the help doc of `subcmd`.
- **Example Usage:**
  - Search for posts containing keywords `linux` and `python`.
    ```bash
    ./blog.py s linux python
    ```
  - Show all results of the previous search.
    ```bash
    ./blog.py l -n0
    ```

### Site Generation / Deployment

Check for details in `.github/workflow/deploy.yml`.

### Development

- **Run Tests:**
  ```bash
  uv run pytest
  ```
- **Linting:**
  ```bash
  uv run ruff format && uv run ruff check && uv run ty check && uv run deptry .
  ```

## Development Conventions

- **Tooling:**
  - `uv` for dependency management
  - `ruff` for checking syntax errors
  - `ty` for checking type annotation erros
  - `deptry` for checking dependency
  - `pytest` for unit testing
- **Content Format:** Content is primarily written in MyST Markdown (`.md`) or Jupyter Notebooks (`.ipynb`).
- **Post Metadata:** Posts contain YAML frontmatter (titles, authors, tags, labels).
- **Directory Structure:**
  - `docs/articles/`: Stable, published articles.
  - `docs/drafts/`: Fragmentary and immature notes.
  - `docs/outdated/`: Legacy content which won't updated.
  - `spells/`: YAML files for correcting titles and tags.
- **Testing:** Small unit tests are located in `tests/` using `pytest`.

## Key Files

- `blog.py`: Main CLI script.
- `blogger.py`: Core logic for the blogging system (database interaction, file parsing).
- `pyproject.toml`: Project metadata and dependencies.
- `docs/myst.yml`: Configuration for the MyST parser and Jupyter Book.
- `docs/toc.yml`: Table of contents for the generated site.
- `uv.lock`: Locked dependencies.
