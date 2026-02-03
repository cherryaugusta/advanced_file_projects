from pathlib import Path
from file_projects.common.io import append_lines

def append_report_update(path: Path, message: str) -> None:
    append_lines(path, [f"- {message}"])
