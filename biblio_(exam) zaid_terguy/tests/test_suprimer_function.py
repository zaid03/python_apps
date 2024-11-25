import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_connection import (
    supprimer_categories_sql,
    supprimer_personnes_sql,
    supprimer_livres_sql,
    supprimer_emprunt_sql,
    afficher_personnes_sql,
    afficher_livres_sql,
    afficher_categories_sql,
    afficher_emprunts_sql
)

# Test supprimer_personnes_sql to delete a person by ID
def test_supprimer_personnes():
    print("\nTesting supprimer_personnes_sql...")
    
    # First, delete the rental records associated with the person
    # Adjust person ID accordingly
    supprimer_emprunt_sql(1, 1)  # Example: Deleting rental for book 1 and person 1
    
    # Now delete the person
    supprimer_personnes_sql(1)  # Adjust the person ID accordingly
    
    # Verify by trying to fetch the person after deletion
    personnes = afficher_personnes_sql()
    if personnes:
        for personne in personnes:
            print(f"ID Personne: {personne['id_pers']}, Nom: {personne['nom']}, Prénom: {personne['prenom']}, Téléphone: {personne['tel']}, Email: {personne['email']}")
    else:
        print("No people found.")

# Test supprimer_livres_sql to delete a book by ID
def test_supprimer_livres():
    print("\nTesting supprimer_livres_sql...")
    
    # Example: First, delete rental records for the book (ensure rentals are deleted first)
    supprimer_emprunt_sql(1, 1)  # Adjust book ID and person ID
    
    # Then delete the book
    supprimer_livres_sql(1)  # Adjust book ID accordingly
    
    # Verify by trying to fetch the book after deletion
    livres = afficher_livres_sql()
    if livres:
        for livre in livres:
            print(f"ID Livre: {livre['id_livre']}, Titre: {livre['titre']}, Auteur: {livre['auteur']}, Prix: {livre['prix']}€")
    else:
        print("No books found.")

# Test supprimer_categories_sql to delete a category by ID
# Test supprimer_categories_sql to delete a category by ID
def test_supprimer_categories():
    print("\nTesting supprimer_categories_sql...")

    # Step 1: Fetch all books in the category (adjust filter if needed)
    books_in_category = afficher_livres_sql()  # Adjust if you want to filter by category
    if books_in_category:
        for book in books_in_category:
            # Step 2: Delete rental records associated with each book
            supprimer_emprunt_sql(book['id_livre'], 1)  # Adjust person ID if necessary
            print(f"Deleted rental for Book ID: {book['id_livre']}")
        
        # Step 3: Now delete the books
        for book in books_in_category:
            supprimer_livres_sql(book['id_livre'])
            print(f"Deleted Book ID: {book['id_livre']}")
    
    # Step 4: Finally, delete the category
    supprimer_categories_sql(1)  # Adjust category ID accordingly
    print("Deleted Category ID: 1")  # Adjust category ID if necessary

    # Step 5: Verify by fetching and printing all remaining categories
    categories = afficher_categories_sql()
    if categories:
        for category in categories:
            print(f"ID Catégorie: {category['id_cat']}, Nom: {category['nom']}")
    else:
        print("No categories found.")


# Test supprimer_emprunt_sql to delete a rental by book ID and person ID
def test_supprimer_emprunt():
    print("\nTesting supprimer_emprunt_sql...")
    
    # Example: Delete rental for book id_livre = 1 and person id_pers = 1 (adjust as needed)
    supprimer_emprunt_sql(1, 1)
    
    # Verify by trying to fetch the rental after deletion
    emprunts = afficher_emprunts_sql()
    if emprunts:
        for emprunt in emprunts:
            print(f"ID Livre: {emprunt['id_livre']}, Titre: {emprunt['titre']}, ID Personne: {emprunt['id_pers']}, Nom: {emprunt['nom']}, Prénom: {emprunt['prenom']}, Nombre de jours: {emprunt['date_jours']}")
    else:
        print("No rentals found.")

# Run the tests
def run_tests():
    test_supprimer_personnes()
    test_supprimer_livres()
    test_supprimer_categories()
    test_supprimer_emprunt()

# Run the test suite
if __name__ == "__main__":
    run_tests()
