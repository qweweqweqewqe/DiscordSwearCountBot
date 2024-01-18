import json


def load_counts():
    try:
        with open("swear_counts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_counts(counts):
    with open("swear_counts.json", "w") as f:
        json.dump(counts, f)
