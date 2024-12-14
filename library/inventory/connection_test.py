from database import create_connection
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        print("La connexion à la base de données a été établie avec succès.")
        conn.close()
    else:
        print("Échec de la connexion à la base de données.")
