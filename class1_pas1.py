# Ovo je KLASA (recept, nacrt za psa)
class Pas:
    def __init__(self, ime, rasa):
        self.ime = ime        # Osobina: Ime
        self.rasa = rasa      # Osobina: Rasa

    def laj(self):            # Veština: Lajanje
        print(f"{self.ime}, {self.rasa},  kaže: Av, av!")

# Ovo su OBJEKTI (Pravi psi u igrici)
moj_pas = Pas(ime="Bobi", rasa="Rotvajler")
tvoj_pas = Pas(ime="Maza", rasa="Pudla")

# Sada objekti mogu da koriste svoje veštine
moj_pas.laj()
tvoj_pas.laj()
