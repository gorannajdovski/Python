import pathlib
import json

file = pathlib.Path("profil.json")

try:
    contents = file.read_text(encoding="utf-8")
    profil = json.loads(contents)
    print("\nTvoj profil:")
    print(f"Ime: {profil['ime']}")
    print(f"Godine: {profil['godine']}")
    print(f"Omiljeni predmet: {profil['predmet']}")

except (FileNotFoundError, json.JSONDecodeError):
    ime = input("Unesi ime: ")
    godine = int(input("Unesi godine: "))
    predmet = input("Omiljeni predmet: ")

    profil = {
        "ime": ime,
        "godine": godine,
        "predmet": predmet
    }
    contents = json.dumps(profil)
    file.write_text(contents, encoding="utf-8")
    print("Profile saved!")
        

