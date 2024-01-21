import json


def load_counts():
    try:
        with open("swear_counts.json", "r") as f:
            data = f.read()
            if not data:
                return {}
            return json.loads(data)
    except FileNotFoundError:
        return {}


def save_counts(counts):
    with open("swear_counts.json", "w") as f:
        json.dump(counts, f)
