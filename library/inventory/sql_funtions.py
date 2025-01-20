from inventory.database import create_connection
from mysql.connector import Error

#initialization of the read and write functions
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
            cursor.close
            connection.close()

def execute_read_query(query, parameters=None):
    connection = create_connection()
    result = None
    try:
        cursor = connection.cursor(dictionary = True)
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Erreur d'exécution de la requête d'écriture: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close
            connection.close()

#sql functions for stock
def ajouter_stock(titre, auteur, status):
    query = "INSERT INTO stock (titre, auteur, status) VALUES (%s, %s, %s)"
    parameters = (titre, auteur, status)
    execute_write_query(query, parameters)

def rechercher_stock(titre):
    query = "SELECT * FROM stock WHERE titre LIKE %s"
    parameters = (f"%{titre}%",)
    return execute_read_query(query, parameters)

def afficher_stock():
    query = "SELECT * FROM stock"
    return execute_read_query(query)

def supprimer_stock(id):
    query = "DELETE FROM stock WHERE id = %s"
    parameters = (id,)
    execute_write_query(query, parameters)

#sql functions for reservations
def ajouter_reservation(id_personne, id_livre, reserv_date):
    query = "INSERT INTO reservations (id_personne, id_livre, reserv_date) VALUES (%s, %s, %s)"
    parameters = (id_personne, id_livre, reserv_date)
    execute_write_query(query, parameters)

def fetch_personnes():
    query = "SELECT id_personne, nom from personnes"
    return execute_read_query(query)

def fetch_livre():
    query = "SELECT id_livre, titre from livres"
    return execute_read_query(query)

def afficher_reservation():
    query = "SELECT * FROM reservations"
    return execute_read_query(query)

def chercher_reservation(id_personne):
    query = "SELECT * FROM reservations WHERE id_personne LIKE %s"
    parameters = (id_personne,)
    return execute_read_query(query, parameters)

def supprimer_reservation(id):
    query = "DELETE FROM reservations WHERE id = %s"
    parameters = (id,)
    execute_write_query(query, parameters)