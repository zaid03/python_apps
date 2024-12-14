import tkinter as tk
from tkinter import *
from personnes.interface_personnes import interface_personnes_ui
from livres.interface_livres import interface_livres_ui

def main_interface():
    root = tk.Tk()
    root.title("Interface Principale")

    tk.Label(root, text="Interface Principale", font=("Arial", 16)).pack(pady=20)

    personne = Button(root, text="Gestion des Personnes", command=interface_personnes_ui, width=30, height=2)
    personne.pack(pady=10)

    livre = Button(root, text="Gestion des Livres", command=interface_livres_ui, width=30, height=2)
    livre.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main_interface()
