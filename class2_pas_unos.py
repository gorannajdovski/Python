class Pas:
    def __init__(self, ime, rasa, godine):
        self.ime = ime
        self.rasa = rasa
        self.godine = godine

    def laj(self):
        print(f"{self.ime}, {self.rasa},  kaže: Av, av!")

    def starost(self):
        print(f"{self.ime}  ima {self.godine} godina!")

def unos():  # Mogli smo bez f-je, ali nije u duhu programiranja
    ime = input("Unesite ime psa: ")
    rasa = input("Unesite rasu psa: ")
    godine = int(input("Unesite godine psa: "))
    return (ime, rasa, godine)   # Vraća torku

moj_pas = Pas(*unos())    # Raspakuje torku jer 
tvoj_pas = Pas(*unos())    # __init__() očekuje 3 param.
moj_pas.laj()
moj_pas.starost()
tvoj_pas.laj()
tvoj_pas.starost()
