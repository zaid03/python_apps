import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_connection import (
    ajouter_categories_sql,
    ajouter_personnes_sql,
    ajouter_livres_sql,
    ajouter_emprunt_sql
)

# Test ajouter_personnes_sql with unique data
def test_ajouter_personnes():
    print("\nTesting ajouter_personnes_sql...")
    # Add a new person with unique values
    ajouter_personnes_sql("Smith", "Alice", "9876543210", "alice.smith@example.com")
    ajouter_personnes_sql("Johnson", "Bob", "1231231234", "bob.johnson@example.com")

# Test ajouter_livres_sql with unique data
def test_ajouter_livres():
    print("\nTesting ajouter_livres_sql...")
    # Add new books with unique values
    ajouter_livres_sql(1, "The Hobbit", "J.R.R. Tolkien", 12.99, "Available")
    ajouter_livres_sql(2, "1984", "George Orwell", 14.99, "Unavailable")

# Test ajouter_categories_sql with unique data
def test_ajouter_categories():
    print("\nTesting ajouter_categories_sql...")
    # Add new categories with unique names
    ajouter_categories_sql("Fantasy")
    ajouter_categories_sql("Dystopian")

# Test ajouter_emprunt_sql with unique data (different book and person IDs)
def test_ajouter_emprunt():
    print("\nTesting ajouter_emprunt_sql...")
    # Rent a book for 7 days (assuming new book IDs and person IDs are used)
    ajouter_emprunt_sql(2, 2, 7)  # Renting "1984" by George Orwell for 7 days
    ajouter_emprunt_sql(1, 1, 10) # Renting "The Hobbit" by J.R.R. Tolkien for 10 days

# Run the tests
def run_tests():
    test_ajouter_personnes()
    test_ajouter_livres()
    test_ajouter_categories()
    test_ajouter_emprunt()

# Run the test suite
if __name__ == "__main__":
    run_tests()
