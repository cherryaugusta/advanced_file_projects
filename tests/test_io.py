from pathlib import Path
from file_projects.common.io import write_lines, read_lines

def test_write_and_read(tmp_path: Path):
    file = tmp_path / "data.txt"
    write_lines(file, ["a", "b", "c"])

    assert read_lines(file) == ["a", "b", "c"]
