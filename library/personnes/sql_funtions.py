from personnes.database import create_connection
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
            cursor.close()
            connection.close()

def execute_read_query(query, parameters=None):
    connection = create_connection()
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

#sql functions for personnes
def ajouter_personne(nom, tel, email, type):
    query = "INSERT INTO  personnes (nom, tel, email, type) VALUES (%s, %s, %s, %s)"
    parameters = (nom, tel, email, type)
    execute_write_query(query, parameters)

def modifier_personne(id_personne, nom=None, tel=None, email=None, type=None):
    query = "UPDATE personnes SET"
    parameters = []

    if nom is not None:
        query += " nom = %s, "
        parameters.append(nom)
    if tel is not None:
        query += "tel = %s, "
        parameters.append(tel)
    if email is not None:
        query += "email = %s, "
        parameters.append(email)
    if type is not None:
        query += "type = %s, "
        parameters.append(type)  

    query = query.rstrip(", ") + " WHERE id_personne = %s"
    parameters.append(id_personne)

    execute_write_query(query, parameters)

def afficher_personne():
    query = "SELECT * from personnes"
    return execute_read_query(query)

def fetch_personnes():
    query = "SELECT id_personne, nom from personnes"
    return execute_read_query(query)

def fetch_livre():
    query = "SELECT id_livre, titre from livres"
    return execute_read_query(query)

def chercher_personne(nom):
    query ="SELECT * FROM personnes WHERE nom LIKE %s"
    parameters = (f"%{nom}%",)
    return execute_read_query(query, parameters)

def supprimer_personne(id_personne):
    query = "DELETE FROM personnes WHERE id_personne = %s"
    parameters = (id_personne,)
    execute_write_query(query, parameters)

#sql functions for emprunts
def ajouter_emprunt(id_personne, id_livre, date_emprunt, date_retour, status, penalite):
    query = "INSERT INTO emprunt (id_personne, id_livre, date_emprunt, date_retour, status, penalite) VALUES (%s, %s, %s, %s, %s, %s)"
    parameters = (id_personne, id_livre, date_emprunt, date_retour, status, penalite)
    execute_write_query(query, parameters)

def afficher_emprunt():
    query = "SELECT * FROM emprunt"
    return execute_read_query(query)

def chercher_emprunt(id_livre):
    query ="SELECT * FROM emprunt WHERE id_livre LIKE %s"
    parameters = (f"%{id_livre}%",)
    return execute_read_query(query, parameters)

def supprimer_emprunt(id_emprunt):
    query = "DELETE FROM emprunt WHERE id_emprunt = %s"
    parameters = (id_emprunt)
    execute_write_query(query, tuple(parameters))

def livre_epmrunter(id_personne):
    query ="SELECT * FROM emprunt WHERE id_personne LIKE %s"
    parameters = (f"%{id_personne}%",)
    return execute_read_query(query, parameters)

def livres_plus_empruntes():
    query = """
    SELECT titre, COUNT(*) AS emprunt
    FROM emprunts
    INNER JOIN livres ON emprunts.id_livre = livres.id_livre
    GROUP BY titre
    ORDER BY emprunts DESC
    LIMIT 10;
    """
    return execute_read_query(query)

