from file_projects.common.paths import personal
from file_projects.personal.diary import append_entry

def main() -> None:
    entry = input("Diary entry: ").strip()
    if not entry:
        return

    diary_file = personal("diary") / "daily_log.txt"
    append_entry(diary_file, entry)

if __name__ == "__main__":
    main()
