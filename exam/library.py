from sql_connection import ajouter_livre_sql, afficher_livre_sql, supprimer_livre_sql

class Livre:

    def __init_(self, id_livre, titre, date_de_pub, prix, auteur):
        self.id_livre = id_livre
        self.titre = titre
        self.date_de_pub = date_de_pub
        self.prix = prix
        self.auteur = auteur

    def ajouter_livre(self, livres):
        titre = input("Enterz le titre du livre: ")
        date_de_pub = input("entrez la date de publication: ")
        prix = int(input("entrez le prix du livre: "))
        auteur = input("entrez l'auteur du livre: ")
        
        ajouter_livre__sql(self.titre, self.date_de_pub, self.prix, self.auteur)
        print("Livre ajouté avec succés")
    
    def afficher_livre(self, livre):
        aficher_livre_sql()

    def supprimer_livre(self, livre):
        id_livre = input("Entrez l'id du livre à supprimer: ")
        suprimer_livre_sql()
        print("Livre supprimé avec succés")

class Categorie:
    def __init__(self, id_cat, nom):
        self.id_cat = id_cat
        self.nom = nom
    
    def ajouter_categorie(self):
        self.nom = input("Entrez la nom de categorie: ")
        ajouter_categorie_sql(self.nom)
        print("Categorie ajoutée avec succés")

    def afficher_categorie(self):
        afficher_categorie_sql()

class Personnes:
    def __init__(self, id_pers, nom, prenom, tel, addresse):
        self.idpers = id_pers
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.addresse = addresse

    