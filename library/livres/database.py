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