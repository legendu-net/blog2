import datetime
import yaml
from pathlib import Path

def _parse_metadata(yaml_str: str) -> dict:
    metadata = yaml.load(yaml_str, Loader=yaml.FullLoader)
    if metadata is None:
        metadata = {}
    for key in ("created", "date"):
        val = metadata.get(key)
        if isinstance(val, str):
            val = datetime.datetime.fromisoformat(val)
        if isinstance(val, datetime.date) and not isinstance(val, datetime.datetime):
            val = datetime.datetime.combine(val, datetime.time.min)
        if isinstance(val, datetime.datetime) and val.tzinfo is None:
            val = val.astimezone()
        metadata[key] = val
    return metadata

mtime = (
    datetime.datetime.fromtimestamp(Path("blogger.py").stat().st_mtime)
    .astimezone()
    .replace(microsecond=0)
)
print(f"mtime: {mtime} (type: {type(mtime)})")

yaml_str = """---
date: 2023-10-27 10:00:00
"""
metadata = _parse_metadata(yaml_str)
print(f"Metadata date: {metadata['date']} (type: {type(metadata['date'])})")
print(f"Compare: {metadata['date'] >= mtime}")

yaml_str_date_only = """---
date: 2023-10-27
"""
metadata_date_only = _parse_metadata(yaml_str_date_only)
print(f"Metadata date (only): {metadata_date_only['date']} (type: {type(metadata_date_only['date'])})")
print(f"Compare: {metadata_date_only['date'] >= mtime}")
