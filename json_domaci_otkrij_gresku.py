import pathlib
import json


file = pathlib.Path("otkrivanja.json")

try:
    contents = file.read_text(encoding="utf-8")
    sadrzaj = json.loads(contents)
    print("Sadrzaj fajla:", sadrzaj)
except Exception as e:
    print("Greška:", e)