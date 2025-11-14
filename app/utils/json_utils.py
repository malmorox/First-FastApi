import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / "data"


def load_json(filename):
    file_path = DATA_PATH / filename

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data, filename):
    file_path = DATA_PATH / filename
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)