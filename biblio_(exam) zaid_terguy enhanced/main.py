import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import (
    ajouter_categories_sql,
    afficher_categories_sql,
    supprimer_categories_sql,
    ajouter_livres_sql,
    afficher_livres_par_categorie_sql,
    afficher_livres_sql,
    supprimer_livres_sql,
    rechercher_livre_sql,
    ajouter_personnes_sql,
    afficher_personnes_sql,
    supprimer_personnes_sql,
)

def update_table(frame, data, columns):
    for widget in frame.winfo_children():
        widget.destroy()

    tree = ttk.Treeview(frame, columns=columns, show="headings")
    tree.tag_configure("oddrow", background="#f9f9f9")
    tree.tag_configure("evenrow", background="#ffffff")

    for col in columns:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=150)

    for i, row in enumerate(data):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", tk.END, values=list(row.values()), tags=(tag,))

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

def main_app():
    def show_categories():
        categories = afficher_categories_sql()
        update_table(content_frame, categories, ["ID", "Nom"])

    def show_livres():
        livres = afficher_livres_sql()
        update_table(content_frame, livres, ["ID", "Titre", "Auteur", "Prix", "État", "Catégorie"])

        entry_label = tk.Label(content_frame, text="Titre de livre:", bg="#f0f4f9")
        entry_label.pack(pady=5)
        entry = ttk.Entry(content_frame, width=30)
        entry.pack(pady=5)

        def rechercher_livre():
            titre = entry.get().strip()
            if titre:
                try:
                    result = rechercher_livre_sql(titre)
                    if result:
                        update_table(content_frame, result, ["ID", "Titre", "Auteur", "Prix", "État", "Catégorie"])
                    else:
                        messagebox.showinfo("Résultat", "Aucun livre trouvé avec ce titre.")
                except Exception as e:
                    messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
            else:
                messagebox.showwarning("Attention", "Veuillez entrer un titre.")
        submit_btn = ttk.Button(content_frame, text="Rechercher", command=rechercher_livre)
        submit_btn.pack(pady=10)

    def show_personnes():
        personnes = afficher_personnes_sql()
        update_table(content_frame, personnes, ["ID", "Nom", "Prénom", "Téléphone", "Email"])

    def display_form(action_type, table_type):
        for widget in content_frame.winfo_children():
            widget.destroy()

        tk.Label(content_frame, text=f"{action_type} {table_type}", font=("Helvetica", 16, "bold"), bg="#f0f4f9").pack(pady=10)

        if action_type == "Ajouter":
            if table_type == "Catégories":
                entry_label = tk.Label(content_frame, text="Nom de la catégorie:", bg="#f0f4f9")
                entry_label.pack(pady=5)
                entry = ttk.Entry(content_frame, width=30)
                entry.pack(pady=5)

                def add_category():
                    if entry.get():
                        ajouter_categories_sql(entry.get())
                        messagebox.showinfo("Succès", "Catégorie ajoutée avec succès.")
                        show_categories()

                submit_btn = ttk.Button(content_frame, text="Ajouter", command=add_category)
                submit_btn.pack(pady=10)

            elif table_type == "Livres":
                categories = afficher_categories_sql()
                if not categories:
                    messagebox.showinfo("Erreur", "Veuillez d'abord ajouter des catégories.")
                    return

                tk.Label(content_frame, text="Catégorie:", bg="#f0f4f9").pack(pady=5)
                category_options = [f"{cat['nom']} (ID: {cat['id_cat']})" for cat in categories]
                selected_category = tk.StringVar()
                category_menu = ttk.Combobox(content_frame, textvariable=selected_category, values=category_options)
                category_menu.pack(pady=5)

                fields = [("Titre", None), ("Auteur", None), ("Prix (MAD)", None), ("État (disponible/loué)", None)]
                entries = {}
                for field, _ in fields:
                    tk.Label(content_frame, text=f"{field}:", bg="#f0f4f9").pack(pady=5)
                    entry = ttk.Entry(content_frame, width=30)
                    entry.pack(pady=5)
                    entries[field] = entry

                def add_book():
                    try:
                        id_cat = int(selected_category.get().split(" (ID: ")[-1][:-1])
                        ajouter_livres_sql(
                            id_cat,
                            entries["Titre"].get(),
                            entries["Auteur"].get(),
                            float(entries["Prix (MAD)"].get()),
                            entries["État (disponible/loué)"].get(),
                        )
                        messagebox.showinfo("Succès", "Livre ajouté avec succès.")
                        show_livres()
                    except ValueError:
                        messagebox.showerror("Erreur", "Veuillez entrer des données valides.")

                submit_btn = ttk.Button(content_frame, text="Ajouter", command=add_book)
                submit_btn.pack(pady=10)

                

            elif table_type == "Personnes":
                fields = [("Nom", None), ("Prénom", None), ("Téléphone", None), ("Email", None)]
                entries = {}
                for field, _ in fields:
                    tk.Label(content_frame, text=f"{field}:", bg="#f0f4f9").pack(pady=5)
                    entry = ttk.Entry(content_frame, width=30)
                    entry.pack(pady=5)
                    entries[field] = entry

                def add_person():
                    ajouter_personnes_sql(
                        entries["Nom"].get(),
                        entries["Prénom"].get(),
                        entries["Téléphone"].get(),
                        entries["Email"].get(),
                    )
                    messagebox.showinfo("Succès", "Personne ajoutée avec succès.")
                    show_personnes()

                submit_btn = ttk.Button(content_frame, text="Ajouter", command=add_person)
                submit_btn.pack(pady=10)

    root = tk.Tk()
    root.title("Gestion de Bibliothèque")
    root.geometry("900x700")
    root.configure(bg="#f0f4f9")

    menu_frame = tk.Frame(root, width=200, bg="#2c3e50")
    menu_frame.pack(side=tk.LEFT, fill=tk.Y)

    content_frame = tk.Frame(root, bg="#f0f4f9")
    content_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

    tk.Label(menu_frame, text="Menu", font=("Helvetica", 18, "bold"), fg="white", bg="#2c3e50").pack(pady=15)

    button_style = {"font": ("Helvetica", 12), "bg": "#34495e", "fg": "white", "activebackground": "#1abc9c", "bd": 0}

    tk.Button(menu_frame, text="Afficher Catégories", command=show_categories, **button_style).pack(pady=5, fill=tk.X)
    tk.Button(menu_frame, text="Afficher Livres", command=show_livres, **button_style).pack(pady=5, fill=tk.X)
    tk.Button(menu_frame, text="Afficher Personnes", command=show_personnes, **button_style).pack(pady=5, fill=tk.X)

    tk.Label(menu_frame, text="Actions", font=("Helvetica", 16), fg="white", bg="#2c3e50").pack(pady=20)

    tk.Button(menu_frame, text="Ajouter Catégories", command=lambda: display_form("Ajouter", "Catégories"), **button_style).pack(pady=5, fill=tk.X)
    tk.Button(menu_frame, text="Ajouter Livres", command=lambda: display_form("Ajouter", "Livres"), **button_style).pack(pady=5, fill=tk.X)
    tk.Button(menu_frame, text="Ajouter Personnes", command=lambda: display_form("Ajouter", "Personnes"), **button_style).pack(pady=5, fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    main_app()