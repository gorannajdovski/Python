from pathlib import Path  # importujemo klasu Path iz modula pathlib
fajl = Path('text_files/pi_million_digits.txt')  # instanciramo objekat path
sadrzaj = fajl.read_text()
linije = sadrzaj.splitlines()
pi_string = ''   # kreiramo promenjivu (string) gde cemo cuvati cifre za pi
for linija in linije:
    pi_string += linija.lstrip() # petlja dodaje svaki element liste u string

print(pi_string[:52])   # prikaz prvih 50 znakova stringa
print(len(pi_string))

rodjendan = input("Unesite Vaš datum rodjenja u obliku ddmmgg: ")
if rodjendan in pi_string:
    print("Tvoj rodjendan je u prvih milion cifara Pi!")
    print("Nalazi se na mestu", pi_string.find(rodjendan))
else:
    print("Tvoj rodjendan nije u prvih milion cifara Pi!")