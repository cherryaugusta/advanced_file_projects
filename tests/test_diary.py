from pathlib import Path
from file_projects.personal.diary import append_entry

def test_diary_append(tmp_path: Path):
    diary = tmp_path / "diary.txt"
    append_entry(diary, "Test entry")

    content = diary.read_text(encoding="utf-8")
    assert "Test entry" in content
