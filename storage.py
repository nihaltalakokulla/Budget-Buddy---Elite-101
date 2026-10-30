
import json
from pathlib import Path

DATA_DIRECTORY = Path(__file__).parent / "data"
DATA_FILE = DATA_DIRECTORY / "purchases.json"


def load_purchases():
    DATA_DIRECTORY.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            purchases = json.load(file)

        return purchases if isinstance(purchases, list) else []

    except (json.JSONDecodeError, OSError):
        return []


def save_purchases(purchases):
    DATA_DIRECTORY.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(purchases, file, indent=4)
