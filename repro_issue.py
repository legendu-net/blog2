import datetime
import yaml
from pathlib import Path

def _parse_metadata(yaml_str: str) -> dict:
    metadata = yaml.load(yaml_str, Loader=yaml.FullLoader)
    if metadata is None:
        metadata = {}
    for key in ("created", "date"):
        if isinstance(metadata.get(key), str):
            metadata[key] = datetime.datetime.fromisoformat(metadata[key])
    return metadata

yaml_str = """---
date: 2023-10-27 10:00:00
"""
metadata = _parse_metadata(yaml_str)
print(f"Metadata date: {metadata['date']} (type: {type(metadata['date'])})")

mtime = (
    datetime.datetime.fromtimestamp(Path("blogger.py").stat().st_mtime)
    .astimezone()
    .replace(microsecond=0)
)
print(f"mtime: {mtime} (type: {type(mtime)})")

try:
    print(f"Compare: {metadata['date'] >= mtime}")
except TypeError as e:
    print(f"Caught expected error: {e}")

yaml_str_date_only = """---
date: 2023-10-27
"""
metadata_date_only = _parse_metadata(yaml_str_date_only)
print(f"Metadata date (only): {metadata_date_only['date']} (type: {type(metadata_date_only['date'])})")
try:
    print(f"Compare: {metadata_date_only['date'] >= mtime}")
except TypeError as e:
    print(f"Caught expected error: {e}")
