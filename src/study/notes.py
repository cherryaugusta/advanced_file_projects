from pathlib import Path
from file_projects.common.io import read_lines

def load_notes(path: Path) -> list[str]:
    return read_lines(path)
