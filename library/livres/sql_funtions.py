from livres.database import create_connection
from mysql.connector import Error

#read_write functions
def execute_write_query(query, parameters=None):
    connection = create_connection()    
    try:
        cursor = connection.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        connection.commit()
        print("Requête exécutée avec succès")
    except Error as e:
        print(f"Erreur d'exécution de la requête d'écriture: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def execute_read_query(query, parameters=None):
    connection = create_connection()
    result = None
    try:
        cursor = connection.cursor(dictionary=True)
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Erreur d'exécution de la requête de lecture: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

#categories_functions
def ajouter_categories(nom):
    query = "INSERT INTO categories (nom) VALUES (%s)"
    parameters = (nom,)
    execute_write_query(query, parameters)

def afficher_categories():
    query = "SELECT * FROM categories"
    return execute_read_query(query)

def fetch_categories():
    query = "SELECT id_cat, nom from categories"
    return execute_read_query(query)

def supprimer_categorie(id_cat):
    query = "DELETE FROM categories WHERE id_cat = %s"
    parameters = (id_cat,)
    execute_write_query(query, parameters)

#livres_functions
def ajouter_livres(id_cat, titre, auteur, prix, etat_loc):
    query = "INSERT INTO livres (id_cat, titre, auteur, prix, etat_loc) VALUES (%s, %s, %s, %s, %s)"
    parameters = (id_cat, titre, auteur, prix, etat_loc)
    execute_write_query(query, parameters)

def rechercher_livre(titre):
    query ="SELECT * FROM livres WHERE titre LIKE %s"
    parameters = (f"%{titre}%",)
    return execute_read_query(query, parameters)

def afficher_livres():
    query = "SELECT * FROM livres"
    return execute_read_query(query)

def supprimer_livre(id_livre):
    query = "DELETE FROM livres WHERE id_livre = %s"
    parameters = (id_livre,)
    execute_write_query(query, parameters)