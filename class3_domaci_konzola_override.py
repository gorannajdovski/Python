class Konzola:
    def __init__(self, naziv):
        self.naziv = naziv

    def pokreni_igru(self, ime_igre):
        print(f"{self.naziv} Učitavam igru {ime_igre}.")

class SuperKonzola(Konzola):
    def __init__(self, naziv, kapacitet_diska):
        super().__init__(naziv)
        self.kapacitet_diska = kapacitet_diska

    def pokreni_igru(self, ime_igre):  # OVERRIDE
        print("\n Proveravam licencu na internetu...")
        # Pozivamo roditelja da uradi osnovni ispis
        super().pokreni_igru(ime_igre)
        print(f"Igra se pokreće sa SSD-a kapaciteta {self.kapacitet_diska}")

naziv_konzole = input("Unesite naziv konzole: ")
kapacitet_diska = int(input("Unesite kapacitet diska: "))
ime_igre = input("Unesite ime igre: ")
moja_konzola = SuperKonzola(naziv_konzole, kapacitet_diska)
moja_konzola.pokreni_igru(ime_igre)
