from pathlib import Path  # importujemo klasu Path iz modula pathlib
fajl = Path('text_files/pi_digits.txt')  # instanciramo objekat klase Path
sadrzaj = fajl.read_text()

linije = sadrzaj.splitlines() # .splitlines() pravi listu ciji su elementi linije u fajlu
pi_string = ''   # kreiramo promenjivu (string) gde cemo cuvati cifre za pi
for linija in linije:
    pi_string += linija.lstrip() # petlja dodaje svaki element liste u string
                                 # a prethodno sklanjamo praznine desno od elementa
print(pi_string)
print(len(pi_string))  # duzina stringa
