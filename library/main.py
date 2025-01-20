import tkinter as tk
from tkinter import *
from personnes.interface_personnes import *
from livres.interface_livres import *
from inventory.inventory_interface import *

def main_interface():
    root = tk.Tk()
    root.title("Interface Principale")

    tk.Label(root, text="Interface Principale", font=("Arial", 16)).pack(pady=20)

    personne = Button(root, text="Gestion des Personnes", command=interface_personnes_ui, width=30, height=2, bg="blue", fg="white", font=("Arial", 12), relief="raised")
    personne.pack(pady=10)

    livre = Button(root, text="Gestion des Livres", command=interface_livres_ui, width=30, height=2,  bg="blue", fg="white", font=("Arial", 12), relief="raised")
    livre.pack(pady=10)

    inventory = Button(root, text="Gestion des stock", command=interface_stock_ui, width=30, height=2,  bg="blue", fg="white", font=("Arial", 12), relief="raised")
    inventory.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main_interface()
