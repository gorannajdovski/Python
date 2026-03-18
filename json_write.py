import pathlib
import json  # importujemo modul json

file = pathlib.Path('numbers.json')  # instanciramo objekat iz fajla numbers.json
contents = file.read_text() # Citamo iz fajla metodom kao za obicne fajlove
numbers = json.loads(contents)  # Čita string contents koji je u JSON formatu i prenosi u promenljivu numbers

print(numbers)