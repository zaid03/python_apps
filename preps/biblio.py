class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def afficher_details(self):
        print(f"titre: {self.titre}")
        print(f"auteur: {self.auteur}")
        print(f"anne de publication: {self.annee_publication}\n")

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, titre, auteur, annee_publication):
        nouveau_livre = Livre(titre, auteur, annee_publication)
        self.livres.append(nouveau_livre)

    def afficher_livres(self):
        if self.livres:
            print("listes des livres:")
            for livre in self.livres:
                livre.afficher_details()
        else:
            print("aucun livre.")

bibliotheque = Bibliotheque()

titre = input("enter le nom de livre: ")
auteur = input("enter l'auteur de livre: ")
annee_publication = int(input("enter l'année de publication de livre: "))

bibliotheque.ajouter_livre(titre, auteur, annee_publication)
bibliotheque.afficher_livres()