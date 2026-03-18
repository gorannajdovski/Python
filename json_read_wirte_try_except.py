import  pathlib
import json
file = pathlib.Path('username.json')  # instanciramo objekat sa nazivom fajla username.json
try:
   contents = file.read_text()        # Čitamo iz fajla metodom kao za obicne fajlove
   username = json.loads(contents)    # Čita JSON string contents i prenosi u promelj. username
   print(f"Welcome {username}!")

except FileNotFoundError:
   username = input("What is your username? ")
   contents = json.dumps(username) # f-ja za generisanje stringa u JSON formatu
   file.write_text(contents)       # Upisujemo u fajl metodom kao za obične fajlove


