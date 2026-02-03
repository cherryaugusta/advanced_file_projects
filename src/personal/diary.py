from datetime import datetime
from pathlib import Path
from file_projects.common.io import append_lines

def append_entry(path: Path, entry: str) -> None:
    timestamp = datetime.now().isoformat(timespec="seconds")
    append_lines(path, [f"{timestamp} - {entry}"])
