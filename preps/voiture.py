class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = int(kilometrage)

    def afficher_details(self):
        print(f"la marque de la voiture est: {self.marque}")
        print(f"le modele de la voiture est: {self.modele}")
        print(f"l'année de la voiture est: {self.annee}")
        print(f"le kilométrage de la voiture est: {self.kilometrage}")

    def rouler(self,km):
        self.kilometrage += km
        print(self.kilometrage)

voiture_vendue = Voiture("range rover", "Velar", "2018", "80000")
voiture_vendue.rouler(150)
Voiture.afficher_details(voiture_vendue)