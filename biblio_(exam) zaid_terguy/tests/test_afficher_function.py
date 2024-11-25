import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_connection import (
    afficher_categories_sql,
    afficher_personnes_sql,
    afficher_livres_sql,
    afficher_emprunts_sql
)

# Test afficher_personnes_sql to fetch all people
def test_afficher_personnes():
    print("\nTesting afficher_personnes_sql...")
    personnes = afficher_personnes_sql()
    if personnes:
        for personne in personnes:
            print(f"ID Personne: {personne['id_pers']}, Nom: {personne['nom']}, Prénom: {personne['prenom']}, Téléphone: {personne['tel']}, Email: {personne['email']}")
    else:
        print("No people found.")

# Test afficher_livres_sql to fetch all books
def test_afficher_livres():
    print("\nTesting afficher_livres_sql...")
    livres = afficher_livres_sql()
    if livres:
        for livre in livres:
            print(f"ID Livre: {livre['id_livre']}, Titre: {livre['titre']}, Auteur: {livre['auteur']}, Prix: {livre['prix']}€")
    else:
        print("No books found.")

# Test afficher_categories_sql to fetch all categories
def test_afficher_categories():
    print("\nTesting afficher_categories_sql...")
    categories = afficher_categories_sql()
    if categories:
        for categorie in categories:
            print(f"ID Catégorie: {categorie['id_cat']}, Nom: {categorie['nom']}")
    else:
        print("No categories found.")

# Test afficher_emprunts_sql to fetch all rentals
def test_afficher_emprunts():
    print("\nTesting afficher_emprunts_sql...")
    emprunts = afficher_emprunts_sql()
    if emprunts:
        for emprunt in emprunts:
            print(f"ID Livre: {emprunt['id_livre']}, Titre: {emprunt['titre']}, ID Personne: {emprunt['id_pers']}, Nom: {emprunt['nom']}, Prénom: {emprunt['prenom']}, Nombre de jours: {emprunt['date_jours']}")
    else:
        print("No rentals found.")

# Run the tests
def run_tests():
    test_afficher_personnes()
    test_afficher_livres()
    test_afficher_categories()
    test_afficher_emprunts()

# Run the test suite
if __name__ == "__main__":
    run_tests()
