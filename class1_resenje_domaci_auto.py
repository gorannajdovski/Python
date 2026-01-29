class Auto:
    """Klasa koja predstavlja automobil."""
    def __init__(self, proizvodjac, model):
        """Inicializacija atributa koji opisuju auto."""
        self.proizvodjac = proizvodjac
        self.model = model

    def opisi_auto(self):
        """Prikazuje osnovne podatke automobila."""
        print(f" Auto je  {self.proizvodjac}  , model {self.model} ")
    
    def godiste(self, godina):
        """Prikazuje godiste automobila."""
        print(f"Auto ima {2026 - godina}  godina.")

proizvodjac = input("Koji je proizvodjac automobila? ")
model = input("Koji je model automobila? ")
godina = int(input("Koje godine je auto proizveden?  "))
moj_auto = Auto(proizvodjac, model)
moj_auto.opisi_auto()
moj_auto.godiste(godina)

proizvodjac = input("Koji je proizvodjac automobila? ")
model = input("Koji je model automobila? ")
godina = int(input("Koje godine je auto proizveden?  "))
komsijin_auto = Auto(proizvodjac, model)
komsijin_auto.opisi_auto()
komsijin_auto.godiste(godina)
