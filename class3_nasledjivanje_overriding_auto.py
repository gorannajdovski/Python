class Auto:
    """Klasa koja predstavlja automobil."""
    def __init__(self, proizvodjac, model):
        """ Inicijalizujte atribute da bi ste opisali automobil."""
        self.proizvodjac = proizvodjac
        self.model = model
        self.kilometraza = 2345

    def opisi_auto(self):
        """Prikazuje osnovne podatke automobila."""
        print(f" Auto je {self.proizvodjac}, model {self.model} ")
    
    def godiste_kilometraza(self, godina, kilometara):
        """Prikazuje godiste i ukupnu kilometražu automobila."""
        print(f"Auto ima {2026 - godina} godina.")
        self.kilometraza += kilometara
        print(f"Auto je presao {self.kilometraza} kilometara.")
        
    def punjenje(self):  # Preklopljena metoda
        print("Pazite da li vaš auto koristi dizel ili benzin! ")
        
class ElekticniAuto(Auto):     # Ovim smo rekli da je ElekticniAuto dete klase Auto 
    def __init__(self, proizvodjac, model, baterija):   # dete preuzima atribute
        super().__init__(proizvodjac, model) # preuzima atr. i met. klase roditelj
        self.baterija = baterija  # dodajemo novi atribut samo za el. Automobile
    
    # def opis_baterije(self):    
    #    print(f"Ovaj auto ima {self.baterija} kWh bateriju") 
    
    def punjenje(self):  # “Obični" overriding 
        print("Koristite isključivo utičnice odgovarajuće snage! ")
        
    def opisi_auto(self): # "Pametni" overriding 
        # Prvo kažemo roditelju da ispiše ono što on zna   
        super().opisi_auto()
        # Zatim mi dodajemo ono što je specifično za nas
        print(f"Ovaj auto ima {self.baterija} kWh bateriju")
         
def unos1():
    proizvodjac = input("Koji je proizvodjac automobila? ")
    model = input("Koji je model automobila? ")
    return (proizvodjac, model)

def unos2():
    godina = int(input("Koje godine je auto proizveden? "))
    kilometara = int(input("Za koliko je uvecana kilometraza? "))
    return (godina, kilometara)

baterija = int(input("Koliki je kapacitet baterije? "))
moja_tesla = ElekticniAuto(*unos1(), baterija)
moja_tesla.opisi_auto()
moja_tesla.godiste_kilometraza(*unos2())
moja_tesla.punjenje()    # Koristimo preklopljenu metodu
