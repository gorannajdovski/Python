import pathlib
import json

def get_stored_username(path):  # Pokušava da učita korisničko ime iz fajla.
   try: 
       contents = path.read_text(encoding="utf-8")
       return json.loads(contents)
   except (FileNotFoundError, json.JSONDecodeError):
      return None

def get_new_username(path):  # Traži unos od korisnika i čuva ga u fajl.
   username = input("What is your username? ")
   contents = json.dumps(username)
   path.write_text(contents, encoding="utf-8")
   return username

def greet_user():  #Glavna funkcija koja pozdravlja korisnika.
   file = pathlib.Path('username.json')
   username = get_stored_username(file)
    
   if username:
        print(f"Welcome {username}!")
   else:
        username = get_new_username(file)
        print("Username saved!")

greet_user()   # Pokretanje programa



