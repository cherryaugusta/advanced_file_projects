from file_projects.common.paths import work
from file_projects.work.reports import append_report_update

def main() -> None:
    report_file = work("project_a") / "report.txt"
    append_report_update(report_file, "Added weekly progress notes")

if __name__ == "__main__":
    main()
