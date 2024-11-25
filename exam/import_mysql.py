import mysql.connector
from mysql.connector import Error

try:
    # Connexion à la base de données
    connection = mysql.connector.connect(
        host="localhost",       # Hôte du serveur MySQL
        user="root",     # Ton nom d'utilisateur MySQL
        password="", # Ton mot de passe MySQL
        database="Bibliotheque"  # Nom de ta base de données
    )
    
    if connection.is_connected():
        print("Connexion réussie à la base de données")

        # Création d'un curseur pour exécuter la requête
        cursor = connection.cursor()
        
        # Requête de sélection
        query = "SELECT * FROM livre"
        cursor.execute(query)
        
        # Récupération de tous les enregistrements
        records = cursor.fetchall()
        
        print("Données récupérées depuis la table 'employees':")
        
        # Affichage des données
        for row in records:
            print("ID:", row[0], "Nom:", row[1], "Poste:", row[2])

except Error as e:
    print("Erreur lors de la connexion à MySQL", e)