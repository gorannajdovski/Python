# 1. Upis u fajl
import pathlib
fajl = pathlib.Path("vest.txt")
text = "  Danas je lep dan.\n  Danas učimo Python.\n  Python je zanimljiv."
fajl.write_text(text, encoding="utf-8")

# 2. Čitanje iz fajla
sadrzaj = fajl.read_text(encoding="utf-8")

linije = sadrzaj.splitlines() # Prebacujemo redove u listu redova
string = ""
for linija in linije: # Spajanje u jedan red i uklanjanje razmaka sa lstrip()
    string += linija.lstrip() + " " # dodajemo + " " da ima razmaka iza tačke
print(string)

# 3. Provera reči
if "Python" in string:
    print("Reč Python je pronađena u tekstu.")

# 4. Zamena reči
string = string.replace("Python", "Fajl")
fajl.write_text(string, encoding="utf-8") # Upis izmenjenog teksta
