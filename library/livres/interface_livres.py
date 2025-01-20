from tkinter import *
from tkinter import ttk
from livres.sql_funtions import *

def interface_livres_ui():
    #window_initialization
    window = Tk()
    window.title("Gestion des Livres")
    window.geometry("1366x768")
    window.configure(bg="#2E2E2E")

    #right_frame for content / left_frame for buttons
    right_frame = Frame(window, bg="#D8CAB8", width=800, height=768)
    right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    left_frame = Frame(window, bg="grey", width=100, height=768)
    left_frame.pack(side=LEFT, fill=Y)

    #button_functions / content_modification
    def ajouter_categories_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Nom de catégorie:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(pady=20)
        categorie_entry = Entry(right_frame, font=("Arial", 14))
        categorie_entry.pack(pady=20)

        def submit_category():
            categorie_nom = categorie_entry.get()
            ajouter_categories(categorie_nom)
            categorie_entry.delete(0, END)
            label.config(text="Catégorie ajoutée avec succès!")
            afficher_categories_action()

        submit_button = Button(right_frame, text="Ajouter", bg="green", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=submit_category)
        submit_button.pack(pady=20)

    def afficher_categories_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Listes des catégories:", bg="#D8CAB8", font=("Arial", 14))
        label.pack(pady=20)
        table = ttk.Treeview(right_frame, columns=("id_cat","nom"), show="headings", height=100)
        table.pack(pady=20, padx=20, fill=BOTH, expand=True)

        table.heading("id_cat", text="Id")
        table.heading("nom", text="Nom")

        categories = afficher_categories()

        for categorie in categories:
            table.insert("", "end", values=(categorie['id_cat'], categorie['nom']))

    def supprimer_categorie_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Id de catégorie:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(pady=20)
        categorie_entry = Entry(right_frame, font=("Arial", 14))
        categorie_entry.pack(pady=20)

        def suprimer_category():
            id_cat = categorie_entry.get()
            supprimer_categorie(id_cat)
            categorie_entry.delete(0, END)
            label.config(text="Catégorie supprimer avec succès!")
            afficher_categories_action()

        suprimer_button = Button(right_frame, text="Supprimer", bg="red", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=suprimer_category)
        suprimer_button.pack(pady=20)

    def ajouter_livre_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        categories = fetch_categories()
        category_dict = {category['nom']: category['id_cat'] for category in categories}
        category_names = list(category_dict.keys())
        label = Label(right_frame, text="Id de Categorie:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)

        id_cat_combobox = ttk.Combobox(right_frame, font=("Arial", 14), values=category_names)
        id_cat_combobox.pack(padx=10)

        label = Label(right_frame, text="Titre de Livre:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        titre_entry = Entry(right_frame, font=("Arial", 14))
        titre_entry.pack(padx=10)
        label = Label(right_frame, text="Auteur de livre:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        auteur_entry = Entry(right_frame, font=("Arial", 14))
        auteur_entry.pack(padx=10)
        label = Label(right_frame, text="Prix de livre:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        prix_entry = Entry(right_frame, font=("Arial", 14))
        prix_entry.pack(padx=10)
        label = Label(right_frame, text="Etat de location:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)

        options = ['oui', 'non']
        etat_loc_combobox = ttk.Combobox(right_frame, font=("Arial", 14), values=options)
        etat_loc_combobox.pack(padx=10)

        def submit_livre():
            selected_category_name = id_cat_combobox.get()
            id_cat = category_dict.get(selected_category_name)
            titre = titre_entry.get()
            auteur = auteur_entry.get()
            prix = prix_entry.get()
            etat_loc = etat_loc_combobox.get()
            ajouter_livres(id_cat, titre, auteur, prix, etat_loc)
            id_cat_combobox.set('')
            titre_entry.delete(0, END)
            auteur_entry.delete(0, END)
            auteur_entry.delete(0, END)
            prix_entry.delete(0, END)
            etat_loc_combobox.set('')
            label.config(text="Livre ajoutée avec sucess")
            afficher_livre_action()

        submit_button = Button(right_frame, text="Ajouter", bg="green", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=submit_livre)
        submit_button.pack(pady=20)

    def afficher_livre_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Listes des Livres:", bg="#D8CAB8", font=("Arial", 14))
        label.pack(pady=20)
        table = ttk.Treeview(right_frame, columns=("id_livre","id_cat","titre","auteur","prix","etat_loc"), show="headings", height=5)
        table.pack(pady=8, padx=8, fill=BOTH, expand=True)

        table.column("id_livre", width=50, anchor="center")
        table.column("id_cat", width=50, anchor="center")
        table.column("titre", width=200, anchor="center")
        table.column("auteur", width=150, anchor="center")
        table.column("prix", width=50, anchor="center")
        table.column("etat_loc", width=50, anchor="center")

        table.heading("id_livre", text="Id")
        table.heading("id_cat", text="Catégorie")
        table.heading("titre", text="Titre")
        table.heading("auteur", text="Auteur")
        table.heading("prix", text="Prix")
        table.heading("etat_loc", text="Etat de location")

        livres = afficher_livres()

        table.tag_configure('even', background='#f0f0f0')
        table.tag_configure('odd', background='#ffffff')

        for i, livre in enumerate(livres):
            tag = 'even' if i % 2 == 0 else 'odd'
            table.insert("", "end", values=(livre['id_livre'], livre['id_cat'], livre['titre'], livre['auteur'], livre['prix'], livre['etat_loc']), tags=(tag,))

        def rechercher_action():
            titre = chercher_entry.get()
            livres = rechercher_livre(titre)

            for row in table.get_children():
                table.delete(row)
            
            for livre in livres:
                table.insert("", "end", values=(livre['id_livre'], livre['id_cat'], livre['titre'], livre['auteur'], livre['prix'], livre['etat_loc']))

        chercher_label = Label(right_frame, text="chercher un titre", bg="#D8CAB8", font=("Arial", 12))
        chercher_label.pack(pady=10)

        chercher_entry = Entry(right_frame, font=("Arial", 14))
        chercher_entry.pack(pady=5)

        recherche_button = Button(right_frame, text="Rechercher", bg="orange", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=rechercher_action)
        recherche_button.pack(pady=20)

    def supprimer_livre_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Id de livre:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(pady=20)
        livre_entry = Entry(right_frame, font=("Arial", 14))
        livre_entry.pack(pady=20)

        def suprimer_livre():
            id_livre = livre_entry.get()
            supprimer_livre(id_livre)
            livre_entry.delete(0, END)
            label.config(text="livre supprimer avec succès!")
            afficher_livre_action()

        suprimer_button = Button(right_frame, text="Supprimer", bg="red", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=suprimer_livre)
        suprimer_button.pack(pady=20)

    #categorie_buttons
    cat_label = Label(left_frame, text="Gestion des Categories:", bg="grey", fg="white", font=("Arial", 12))
    cat_label.pack(pady=20, padx=50)

    add_button = Button(left_frame, text="Ajouter une Catégorie", bg="green", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=ajouter_categories_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Aficher les Catégories", bg="orange", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=afficher_categories_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Suprimer une Catégorie", bg="red", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=supprimer_categorie_action)
    add_button.pack(pady=10, padx=50)

    #livres_button
    livres_label = Label(left_frame, text="Gestion des Livres:", bg="grey", fg="white", font=("Arial", 12))
    livres_label.pack(pady=20, padx=50)

    add_button = Button(left_frame, text="Ajouter un Livre", bg="green", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=ajouter_livre_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Aficher les Livres", bg="orange", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=afficher_livre_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Suprimer un Livre", bg="red", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=supprimer_livre_action)
    add_button.pack(pady=10, padx=50)

    #to keep the app running untill closed
    window.mainloop()
