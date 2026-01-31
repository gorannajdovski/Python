class Pas:
    """Postavljanje podrazumevane vrednosti (default) atributa tezina"""
    def __init__(self, ime, rasa, godine): 
        """ Čak iako dodamo parametar tezina, ona ostaje 35. """
        self.ime = ime
        self.rasa = rasa
        self.godine = godine
        self.tezina = 35

    def laj(self):
        print(f"{self.ime}, {self.rasa}, kaže: Av, av!")

    def starost(self):
        print(f"{self.ime} ima {self.godine} godina!")

    def tezi(self):
        print(f"{self.ime}  teži {self.tezina} kg!")

""" def tezi(self):
        # Možemo menjati vrednost atributa direktno preko metode
        self.tezina +=10        
        print(f"{self.ime}  teži {self.tezina} kg!")   
"""


def unos():  # Mogli smo bez f-je, ali nije u duhu programiranja
    ime = input("Unesite ime psa: ")
    rasa = input("Unesite rasu psa: ")
    godine = int(input("Unesite godine psa: "))
    return (ime, rasa, godine)   # Vraća torku

moj_pas = Pas(*unos())    # Raspakuje torku jer 
moj_pas.laj()
moj_pas.starost()
moj_pas.tezi()
""" Možemo menjati vrednost atributa direktno preko instance 
moj_pas.tezina = 55  # Iako u __init__ imamo self.tezina = 35, ona je 55 za moj_pas.
"""