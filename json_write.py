import pathlib
import json  # importujemo modul json

numbers = [5, 7, 11, 14, 17, 21]

file = pathlib.Path('numbers.json')  # instanciramo objekat sa nazivom fajla numbers.json
contents = json.dumps(numbers) # f-ja za gererisanje stringa u JSON formatu
file.write_text(contents)      # Upisujemo u fajl metodom kao za obicne fajlove
