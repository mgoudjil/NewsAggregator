import json
from pathlib import Path
from os.path import dirname

def load_json(filepath):
    with open(dirname(filepath) + "/sources/" + Path(filepath).stem + ".json") as f:
        data = json.load(f)
    return data