class Auto:
    """Klasa koja predstavlja automobil."""
    def __init__(self, proizvodjac, model):
        """ Inicijalizujte atribute da bi ste opisali automobil."""
        self.proizvodjac = proizvodjac
        self.model = model
        self.kilometraza = 2345

    def opisi_auto(self):
        """Prikazuje osnovne podatke automobila."""
        print(f" Auto je  {self.proizvodjac}  , model {self.model} ")
    
    def godiste_kilometraza(self, godina, kilometara):
        """Prikazuje godiste i ukupnu kilometražu automobila."""
        print(f"Auto ima {2026 - godina}  godina.")
        self.kilometraza += kilometara
        print(f"Auto je presao {self.kilometraza} kilometara.")

def unos1():
    proizvodjac = input("Koji je proizvodjac automobila? ")
    model = input("Koji je model automobila? ")
    return (proizvodjac, model)

def unos2():
    godina = int(input("Koje godine je auto proizveden?  "))
    kilometara = int(input("Za koliko je uvecana kilometraza? "))
    return (godina, kilometara)

moj_auto = Auto(*unos1())
moj_auto.opisi_auto()
moj_auto.godiste_kilometraza(*unos2())

komsijin_auto = Auto(*unos1())
komsijin_auto.opisi_auto()
komsijin_auto.godiste_kilometraza(*unos2())
