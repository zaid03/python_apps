import json
from datetime import datetime

class Voiture:
    def __init__(self, marque, modele, annee, prix_journalier, disponible=True):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix_journalier = prix_journalier
        self.disponible = disponible

    def cout_location(self, jours):
        return jours * self.prix_journalier

    def afficher_voiture(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Prix journalier: {self.prix_journalier} MAD")


class AgenceLocation:
    def __init__(self, filename='stock_voitures.json'):
        self.voitures_disponibles = []
        self.filename = filename
        self.load_voitures()

    def load_voitures(self):
        self.voitures_disponibles = []
        try:
            with open(self.filename, 'r') as file:
                voitures_data = json.load(file)
                for data in voitures_data:
                    voiture = Voiture(data['marque'], data['modele'], data['annee'], data['prix_journalier'], data['disponible'])
                    if voiture.disponible:
                        self.voitures_disponibles.append(voiture)
        except FileNotFoundError:
            print("Aucun fichier de voitures trouvé, créant une nouvelle liste.")

    def save_voitures(self):
        voitures_data = [{
            'marque': voiture.marque,
            'modele': voiture.modele,
            'annee': voiture.annee,
            'prix_journalier': voiture.prix_journalier,
            'disponible': voiture.disponible
        } for voiture in self.voitures_disponibles]

        with open(self.filename, 'w') as file:
            json.dump(voitures_data, file, indent=4)

    def ajouter_voiture(self, voiture):
        self.voitures_disponibles.append(voiture)
        self.save_voitures()

    def louer_voiture(self, index, date_location, jours):
        if 0 <= index < len(self.voitures_disponibles):
            voiture = self.voitures_disponibles[index]
            voiture.disponible = False  # Mise à jour de la disponibilité
            prix_total = voiture.cout_location(jours)
            print(f"Vous avez loué la voiture {voiture.marque} {voiture.modele}.")
            print(f"Votre voiture sera prête le {date_location}.")
            print(f"Le coût total pour louer la voiture pour {jours} jours est de {prix_total} MAD.")

            self.save_voitures()
            return voiture
        else:
            print("Cette voiture n'est pas disponible.")
            return None

    def afficher_voiture_disponibles(self):
        if self.voitures_disponibles:
            print("Voitures disponibles à la location :")
            for index, voiture in enumerate(self.voitures_disponibles):
                print(f"{index + 1}. ", end="")
                voiture.afficher_voiture()
        else:
            print("Aucune voiture disponible à la location.")


agence = AgenceLocation()

agence = AgenceLocation()


if not agence.voitures_disponibles:
    voiture1 = Voiture("Toyota", "Corolla", 2020, 300)
    voiture2 = Voiture("BMW", "Série 3", 2018, 500)
    voiture3 = Voiture("Audi", "A4", 2019, 450)
    voiture4 = Voiture("Ford", "Focus", 2020, 350)
    voiture5 = Voiture("Volkswagen", "Passat", 2021, 400)
    voiture6 = Voiture("Peugeot", "308", 2019, 300)
    voiture7 = Voiture("Nissan", "Qashqai", 2020, 370)
    voiture8 = Voiture("Hyundai", "i30", 2018, 320)
    voiture9 = Voiture("Kia", "Ceed", 2019, 330)
    voiture10 = Voiture("Mazda", "3", 2020, 390)

    agence.ajouter_voiture(voiture1)
    agence.ajouter_voiture(voiture2)
    agence.ajouter_voiture(voiture3)
    agence.ajouter_voiture(voiture4)
    agence.ajouter_voiture(voiture5)
    agence.ajouter_voiture(voiture6)
    agence.ajouter_voiture(voiture7)
    agence.ajouter_voiture(voiture8)
    agence.ajouter_voiture(voiture9)
    agence.ajouter_voiture(voiture10)


agence.afficher_voiture_disponibles()

try:
    choix = int(input("Entrez l'index de la voiture que vous souhaitez louer : ")) - 1
    date_location = input("Entrez la date à laquelle vous souhaitez louer la voiture (JJ/MM/AAAA) : ")

    try:
        datetime.strptime(date_location, '%d/%m/%Y')
        jours = int(input("Combien de jours souhaitez-vous louer la voiture ? "))
        agence.louer_voiture(choix, date_location, jours)
    except ValueError:
        print("Format de date invalide ou nombre de jours non valide.")
except ValueError:
    print("Veuillez entrer un numéro valide.")
except IndexError:
    print("Numéro de voiture invalide.")
