from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "data"

def work(project: str) -> Path:
    return DATA_DIR / "work" / project

def personal(area: str) -> Path:
    return DATA_DIR / "personal" / area

def study(area: str) -> Path:
    return DATA_DIR / "study" / area
