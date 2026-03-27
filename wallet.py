class Novcanik:
    def __init__(self, iznos=0):
        self.stanje = iznos

    def dodaj_novac(self, kolicina):
        self.stanje += kolicina

    def potrosi_novac(self, kolicina):
        if kolicina > self.stanje:
            print("Nema dovoljno novca!")
        else:
            self.stanje -= kolicina