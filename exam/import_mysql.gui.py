import mysql.connector
from tkinter import Tk, Label, Button
from tkinter.ttk import Treeview

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Bibliotheque"
)
cursor = conn.cursor()

# Requête SELECT
cursor.execute("SELECT * FROM livre")
colonnes = [desc[0] for desc in cursor.description]  # Récupère les noms de colonnes
resultats = cursor.fetchall()

# Création de la fenêtre principale avec tkinter
root = Tk()
root.title("Résultats de la requête SELECT")
root.geometry("600x400")

# Titre
titre_label = Label(root, text="Résultats de la requête SELECT", font=("Helvetica", 16))
titre_label.pack(pady=10)

# Création du tableau Treeview
tableau = Treeview(root, columns=colonnes, show='headings')
tableau.pack(fill='both', expand=True)

# Définition des en-têtes de colonnes
for col in colonnes:
    tableau.heading(col, text=col)
    tableau.column(col, width=100)  # Ajustez la largeur des colonnes si nécessaire

# Insertion des données dans le tableau
for row in resultats:
    tableau.insert('', 'end', values=row)

# Bouton pour fermer la fenêtre
close_button = Button(root, text="Fermer", command=root.quit)
close_button.pack(pady=10)

# Boucle principale de tkinter
root.mainloop()

# Fermeture de la connexion à la base de données
cursor.close()
conn.close()
