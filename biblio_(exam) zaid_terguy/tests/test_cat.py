import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_connection import (
    supprimer_categories_sql,
    supprimer_livres_sql,
    supprimer_emprunt_sql,
    afficher_categories_sql,
    afficher_livres_sql
)

# Function to delete rentals for a given book
def delete_rentals_for_book(book_id):
    print(f"Deleting rentals for Book ID: {book_id}")
    # Delete all rentals associated with this book
    supprimer_emprunt_sql(book_id, 1)  # Adjust the person ID if necessary

# Function to delete books in a given category
def delete_books_in_category():
    print("\nFetching all books in the category...")
    books_in_category = afficher_livres_sql()  # This should be filtered for the category if needed
    if books_in_category:
        for book in books_in_category:
            delete_rentals_for_book(book['id_livre'])  # Delete associated rentals
            supprimer_livres_sql(book['id_livre'])  # Delete the book itself
            print(f"Deleted Book ID: {book['id_livre']}")

# Function to delete a category
def delete_category(category_id):
    # Step 1: Delete all books and their rentals in the category
    delete_books_in_category()

    # Step 2: Now delete the category itself
    supprimer_categories_sql(category_id)
    print(f"Deleted Category ID: {category_id}")

    # Step 3: Verify by fetching and printing all remaining categories
    print("\nRemaining Categories:")
    categories = afficher_categories_sql()
    if categories:
        for category in categories:
            print(f"ID Catégorie: {category['id_cat']}, Nom: {category['nom']}")
    else:
        print("No categories found.")

# Function to run the category deletion test
def test_delete_category():
    print("\nTesting Deletion of Category...")

    category_id_to_delete = 6  # Set the category ID to delete (adjust as necessary)
    delete_category(category_id_to_delete)

# Run the test
if __name__ == "__main__":
    test_delete_category()
