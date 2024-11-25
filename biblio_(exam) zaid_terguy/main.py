import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import (
    ajouter_personnes_sql,
    afficher_personnes_sql,
    supprimer_personnes_sql,
    ajouter_livres_sql,
    supprimer_livres_sql,
    chercher_livres_sql,
    ajouter_categories_sql,
    afficher_categories_sql,
    supprimer_categories_sql,
    fetch_data,
    afficher_livres_par_categorie_sql,
    fetch_categories,
)

BG_COLOR = "#2c3e50"
BTN_COLOR = "#3498db"
TEXT_COLOR = "#ecf0f1"
FONT_TITLE = ("Arial", 14, "bold")
FONT_BTN = ("Arial", 12)
FONT_TEXT = ("Arial", 11)

def main_menu():
    root = tk.Tk()
    root.title("Gestion de Bibliothèque")
    root.geometry("400x300")
    root.configure(bg=BG_COLOR)

    title = tk.Label(root, text="Bienvenue dans la Gestion de Bibliothèque", font=FONT_TITLE, fg=TEXT_COLOR, bg=BG_COLOR)
    title.pack(pady=20)

    tk.Button(root, text="Gérer les Catégories", command=open_categories, width=20, height=2, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT_BTN).pack(pady=10)
    tk.Button(root, text="Gérer les Livres", command=open_books, width=20, height=2, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT_BTN).pack(pady=10)
    tk.Button(root, text="Gérer les Personnes", command=open_people, width=20, height=2, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT_BTN).pack(pady=10)

    root.mainloop()

def open_categories():
    manage_window("Catégories", ajouter_categories_sql, afficher_categories_sql, supprimer_categories_sql, chercher_livres_sql)

def open_books():
    manage_window("Livres", ajouter_livres_sql, afficher_livres_par_categorie_sql, supprimer_livres_sql, chercher_livres_sql)

def open_people():
    manage_window("Personnes", ajouter_personnes_sql, afficher_personnes_sql, supprimer_personnes_sql, chercher_livres_sql)

def manage_window(title, ajouter_func, afficher_func, supprimer_func, chercher_func):
    window = tk.Toplevel()
    window.title(f"Gestion des {title}")
    window.geometry("400x470")
    window.configure(bg=BG_COLOR)

    tk.Label(window, text=f"Gestion des {title}", font=FONT_TITLE, fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=15)

    tk.Button(window, text="Ajouter", command=lambda: open_add_form(title, ajouter_func), width=15, height=2, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT_BTN).pack(pady=5)
    tk.Button(window, text="Afficher", command=lambda: afficher(title, afficher_func), width=15, height=2, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT_BTN).pack(pady=5)
    tk.Button(window, text="Supprimer", command=lambda: open_delete_form(title, supprimer_func), width=15, height=2, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT_BTN).pack(pady=5)
    tk.Button(window, text="Chercher", command=lambda: open_search_form(title, chercher_func), width=15, height=2, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT_BTN).pack(pady=5)

def open_add_form(title, ajouter_func):
    form_window = tk.Toplevel()
    form_window.title(f"Ajouter {title}")
    form_window.geometry("400x300")
    form_window.configure(bg=BG_COLOR)

    tk.Label(form_window, text=f"Ajouter {title}", font=FONT_TITLE, fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)

    entries = {}
    fields = {
        "Catégories": ["Nom"],
        "Livres": ["Titre", "Auteur", "Prix", "État de location"],
        "Personnes": ["Nom", "Prénom", "Téléphone", "Email"],
    }

    for idx, field in enumerate(fields[title]):
        tk.Label(form_window, text=f"{field}:", font=FONT_TEXT, fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=5)
        entry = tk.Entry(form_window)
        entry.pack(pady=5)
        entries[field] = entry

    def submit():
        data = {field: entry.get() for field, entry in entries.items()}
        if all(data.values()):
            ajouter_func(*data.values())
            messagebox.showinfo("Succès", f"{title} ajouté avec succès.")
            form_window.destroy()
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    tk.Button(form_window, text="Soumettre", command=submit, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT_BTN).pack(pady=15)

def afficher(title, afficher_func):
    records = afficher_func() if title != "Livres" else afficher_func(fetch_categories()[0]["id_cat"])
    if not records:
        messagebox.showinfo("Info", f"Aucun {title.lower()} trouvé.")
        return

    table_window = tk.Toplevel()
    table_window.title(f"Liste des {title}")
    table_window.geometry("600x400")
    table_window.configure(bg=BG_COLOR)

    tree = ttk.Treeview(table_window, columns=[f"col{i}" for i in range(len(records[0]))], show="headings", height=20)
    tree.pack(fill=tk.BOTH, expand=True)

    for i, key in enumerate(records[0].keys()):
        tree.heading(f"col{i}", text=key)
        tree.column(f"col{i}", width=100)

    for record in records:
        tree.insert("", "end", values=list(record.values()))

def open_delete_form(title, supprimer_func):
    form_window = tk.Toplevel()
    form_window.title(f"Supprimer {title}")
    form_window.geometry("300x150")
    form_window.configure(bg=BG_COLOR)

    tk.Label(form_window, text=f"Supprimer {title}", font=FONT_TITLE, fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)

    tk.Label(form_window, text="ID à supprimer:", font=FONT_TEXT, fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=5)
    id_entry = tk.Entry(form_window)
    id_entry.pack(pady=5)

    def submit():
        id_to_delete = id_entry.get()
        if id_to_delete.isdigit():
            supprimer_func(int(id_to_delete))
            messagebox.showinfo("Succès", f"{title[:-1]} supprimé avec succès.")
            form_window.destroy()
        else:
            messagebox.showerror("Erreur", "Veuillez entrer un ID valide.")

    tk.Button(form_window, text="Supprimer", command=submit, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT_BTN).pack(pady=10)

def open_search_form(title, chercher_func):
    form_window = tk.Toplevel()
    form_window.title(f"Chercher {title}")
    form_window.geometry("300x150")
    form_window.configure(bg=BG_COLOR)

    tk.Label(form_window, text=f"Chercher {title}", font=FONT_TITLE, fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)

    tk.Label(form_window, text="Titre à chercher:", font=FONT_TEXT, fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=5)
    search_entry = tk.Entry(form_window)
    search_entry.pack(pady=5)

    def submit():
        titre = search_entry.get()
        if titre:
            results = chercher_func(titre)
            messagebox.showinfo(f"Résultats de {title}", "\n".join(map(str, results)) if results else "Aucun résultat trouvé.")
            form_window.destroy()
        else:
            messagebox.showerror("Erreur", "Veuillez entrer un titre valide.")

    tk.Button(form_window, text="Chercher", command=submit, bg=BTN_COLOR, fg=TEXT_COLOR, font=FONT_BTN).pack(pady=10)

main_menu()
