import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="zaid.123",
            database="my_database"
        )
        if connection.is_connected():
            print("Connection établie")
            return connection
    except Error as e:
        print(f"Erreur de connexion à MySQL: {e}")
        return None


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
        if connection.is_connected():
            cursor.close()
            connection.close()

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
        if connection.is_connected():
            cursor.close()
            connection.close()

##for persons
def ajouter_personnes_sql(nom, prenom, tel, email):
    query = "INSERT INTO personnes (nom, prenom, tel, email) VALUES (%s, %s, %s, %s)"
    parameters = (nom, prenom, tel, email)
    execute_write_query(query, parameters)

def afficher_personnes_sql():
    query = "SELECT * FROM personnes"
    return execute_read_query(query)

def supprimer_personnes_sql(id_pers):
    query = "DELETE FROM personnes WHERE id_pers = %s"
    parameters = (id_pers,)
    execute_write_query(query, parameters)

#for books 
def ajouter_livres_sql(id_cat, titre, auteur, prix, etat_loc):
    query = "INSERT INTO livres (id_cat, titre, auteur, prix, etat_loc) VALUES (%s, %s, %s, %s, %s)"
    parameters = (id_cat, titre, auteur, prix, etat_loc)
    execute_write_query(query, parameters)

def check_categories_exists(id_cat):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM categories WHERE id_cat = %s", (id_cat,))
        return cursor.fetchone() is not None
    except mysql.connector.Error as e:
        print(f"Erreur lors de la vérification de la catégorie: {e}")
        return False
    finally:
        cursor.close()
        connection.close()

def afficher_livres_par_categorie_sql(id_cat):
    query = "SELECT * FROM livres WHERE id_cat = %s"
    parameters = (id_cat,)
    return execute_read_query(query, parameters)

def fetch_categories():
    query = "SELECT id_cat, nom FROM categories"
    return execute_read_query(query)

def supprimer_livres_sql(id_livre):
    query = "DELETE FROM livres WHERE id_livre = %s"
    parameters = (id_livre,)
    execute_write_query(query, parameters)

def chercher_livres_sql(titre):
    query = "SELECT * FROM livres WHERE titre = %s"
    parameters = (titre,)
    return execute_read_query(query, parameters)
    
#for categories
def ajouter_categories_sql(nom):
    query = "INSERT INTO categories (nom) VALUES (%s)"
    parameters = (nom,)
    execute_write_query(query, parameters)

def afficher_categories_sql():
    query = "SELECT * FROM categories"
    return execute_read_query(query)

def supprimer_categories_sql(id_cat):
    query = "DELETE FROM categories WHERE id_cat = %s"
    parameters = (id_cat,)
    execute_write_query(query, parameters)

def fetch_data():
    conn = None
    cursor = None
    try:
        # Use the create_connection function to establish a database connection
        conn = create_connection()
        if conn is not None and conn.is_connected():
            cursor = conn.cursor()
            # Query to fetch data
            query = "SELECT id_cat, nom FROM categories"
            cursor.execute(query)
            data = cursor.fetchall()

            return [f"{row[1]} (ID: {row[0]})" for row in data]

    except Error as e:
        print(f"Erreur d'exécution de la requête de lecture: {e}")
        return []

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

#for emprunt
def ajouter_emprunt_sql(id_livre, id_pers, date_jours):
    query = "INSERT INTO emprunt (id_livre, id_pers, date_jours) VALUES (%s, %s, %s)"
    parameters = (id_livre, id_pers, date_jours)
    execute_write_query(query, parameters)

def afficher_emprunts_sql():
    query = """
    SELECT e.id_livre, l.titre, e.id_pers, p.nom, p.prenom, e.date_jours 
    FROM emprunt e
    JOIN livres l ON e.id_livre = l.id_livre
    JOIN personnes p ON e.id_pers = p.id_pers
    """
    return execute_read_query(query)

def supprimer_emprunt_sql(id_livre, id_pers):
    query = "DELETE FROM emprunt WHERE id_livre = %s AND id_pers = %s"
    parameters = (id_livre, id_pers)
    execute_write_query(query, parameters)