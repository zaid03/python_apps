from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import Toplevel
from sql_funtions import *

#global function for ui to work in main
def interface_personnes_ui():
    window = Tk()
    window.title("Gestion des Emprunts et les Utilisateurs")
    window.geometry("1366x768")
    window.configure(bg="#2E2E2E")

    #frames left for buttons and right for buttun's content
    right_frame = Frame(window, bg="#D8CAB8", width=800, height=768)
    right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    left_frame = Frame(window, bg="grey", width=100, height=768)
    left_frame.pack(side=LEFT, fill=Y)
    
    #button's functions
    def ajouter_personne_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Nom complet:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        nom_entry = Entry(right_frame, font=("Arial", 14))
        nom_entry.pack(padx=10)
        label = Label(right_frame, text="N° de Telephone:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        tel_entry = Entry(right_frame, font=("Arial", 14))
        tel_entry.pack(padx=10)
        label = Label(right_frame, text="Email:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        email_entry = Entry(right_frame, font=("Arial", 14))
        email_entry.pack(padx=10)
        label = Label(right_frame, text="Type:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        options = ['Etudiant', 'Enseignant', 'Chercheur', 'Visiteur']
        type_combobox = ttk.Combobox(right_frame, font=("Arial", 14), values=options)
        type_combobox.pack(padx=10)

        def submit_personne():
            nom = nom_entry.get()
            tel = tel_entry.get()
            email = email_entry.get()
            type = type_combobox.get()
            ajouter_personne(nom, tel, email, type)
            nom_entry.delete(0, END)
            tel_entry.delete(0, END)
            email_entry.delete(0, END)
            type_combobox.set('')
            label.config(text="Personne ajoutée avec succès!")
            afficher_personne_action()

        submit_button = Button(right_frame, text="Ajouter", bg="green", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=submit_personne)
        submit_button.pack(pady=20)

    def modifier_personne_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Id de Personne:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        id_personne_entry = Entry(right_frame, font=("Arial", 14))
        id_personne_entry.pack(padx=10)
        label = Label(right_frame, text="Nom complet:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        nom_entry = Entry(right_frame, font=("Arial", 14))
        nom_entry.pack(padx=10)
        label = Label(right_frame, text="N° de Telephone:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        tel_entry = Entry(right_frame, font=("Arial", 14))
        tel_entry.pack(padx=10)
        label = Label(right_frame, text="Email:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        email_entry = Entry(right_frame, font=("Arial", 14))
        email_entry.pack(padx=10)
        label = Label(right_frame, text="Type:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        options = ['Etudiant', 'Enseignant', 'Chercheur', 'Visiteur']
        type_combobox = ttk.Combobox(right_frame, font=("Arial", 14), values=options)
        type_combobox.pack(padx=10)

        def submit_personne():
            id_personne = int(id_personne_entry.get())
            nom = nom_entry.get()
            tel = tel_entry.get()
            email = email_entry.get()
            type = type_combobox.get()
            modifier_personne(id_personne, nom, tel, email, type)
            id_personne_entry.delete(0,END)
            nom_entry.delete(0, END)
            tel_entry.delete(0, END)
            email_entry.delete(0, END)
            type_combobox.set('')
            label.config(text="Personne modifé avec succès!")
            afficher_personne_action()

        submit_button = Button(right_frame, text="modifier", bg="green", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=submit_personne)
        submit_button.pack(pady=20)

    def afficher_personne_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Listes des Personnes:", bg="#D8CAB8", font=("Arial", 14))
        label.pack(pady=20)
        table = ttk.Treeview(right_frame, columns=("id_personne","nom","tel","email","type"), show="headings", height=5)
        table.pack(pady=8, padx=8, fill=BOTH, expand=True)

        table.column("id_personne", width=50, anchor="center")
        table.column("nom", width=50, anchor="center")
        table.column("tel", width=200, anchor="center")
        table.column("email", width=150, anchor="center")
        table.column("type", width=50, anchor="center")

        table.heading("id_personne", text="Id")
        table.heading("nom", text="Nom complet")
        table.heading("tel", text="N° de Telephone")
        table.heading("email", text="Email")
        table.heading("type", text="Type")

        livres = afficher_personne()

        table.tag_configure('even', background='#f0f0f0')
        table.tag_configure('odd', background='#ffffff')

        for i, livre in enumerate(livres):
            tag = 'even' if i % 2 == 0 else 'odd'
            table.insert("", "end", values=(livre['id_personne'], livre['nom'], livre['tel'], livre['email'], livre['type']), tags=(tag,))

        def rechercher_action():
            nom = chercher_entry.get()
            livres = chercher_personne(nom)

            for row in table.get_children():
                table.delete(row)
            
            for livre in livres:
                table.insert("", "end", values=(livre['id_personne'], livre['nom'], livre['tel'], livre['email'], livre['type']))


        chercher_label = Label(right_frame, text="chercher une Personne", bg="#D8CAB8", font=("Arial", 12))
        chercher_label.pack(pady=10)

        chercher_entry = Entry(right_frame, font=("Arial", 14))
        chercher_entry.pack(pady=5)

        recherche_button = Button(right_frame, text="Rechercher", bg="orange", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=rechercher_action)
        recherche_button.pack(pady=20)

    def supprimer_personne_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Id de personne:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(pady=20)
        personne_entry = Entry(right_frame, font=("Arial", 14))
        personne_entry.pack(pady=20)

        def suprimer_personne():
            id_personne = personne_entry.get()
            supprimer_personne(id_personne)
            personne_entry.delete(0, END)
            label.config(text="Personne supprimer avec succès!")
            afficher_personne_action

        suprimer_button = Button(right_frame, text="Supprimer", bg="red", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=suprimer_personne)
        suprimer_button.pack(pady=20)

    def open_calendar(entry_widget):
        top = Toplevel()
        top.geometry("300x300")
        
        cal = Calendar(top, font=("Arial", 14), selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(padx=10, pady=10)

        def set_date():
            date = cal.get_date()
            entry_widget.delete(0, 'end')
            entry_widget.insert(0, date)
            top.destroy()

        btn = Button(top, text="Select Date", command=set_date)
        btn.pack(pady=10)

    def ajouter_emprunt_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        personnes = fetch_personnes()
        personne_dict = {personne['nom']: personne['id_personne'] for personne in personnes}
        personne_names = list(personne_dict.keys())
        label = Label(right_frame, text="Id de personne:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)

        id_personne_combobox = ttk.Combobox(right_frame, font=("Arial", 14), values=personne_names)
        id_personne_combobox.pack(padx=10)

        livres = fetch_livre()
        livre_dict = {livre['titre']: livre['id_livre'] for livre in livres}
        livre_names = list(livre_dict.keys())
        label = Label(right_frame, text="Id de livre:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)

        id_livre_combobox = ttk.Combobox(right_frame, font=("Arial", 14), values=livre_names)
        id_livre_combobox.pack(padx=10)

        label = Label(right_frame, text="Date d'emprunt:", bg="#D8CAB8", fg="white", font=("Arial", 14))
        label.pack(padx=10)
        date_emprunt = Entry(right_frame, font=("Arial", 14))
        date_emprunt.pack(padx=10)
        date_emprunt.bind("<Button-1>", lambda event: open_calendar(date_emprunt))

        label = Label(right_frame, text="Date de retour:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        date_retour = Entry(right_frame, font=("Arial", 14))
        date_retour.pack(padx=10)
        date_retour.bind("<Button-1>", lambda event: open_calendar(date_retour))


        label = Label(right_frame, text="Etat de location:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        options = ['En cours', 'Términé']
        status_combobox = ttk.Combobox(right_frame, font=("Arial", 14), values=options)
        status_combobox.pack(padx=10)

        label = Label(right_frame, text="Penalite:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        penalite_entry = Entry(right_frame, font=("Arial", 14))
        penalite_entry.pack(padx=10)

        def submit_livre():
            selected_personne_name = id_personne_combobox.get()
            id_personne = personne_dict.get(selected_personne_name)
            selected_livre_name = id_livre_combobox.get()
            id_livre = livre_dict.get(selected_livre_name)

            date_emprunt_value = date_emprunt.get().strip()
            date_retour_value = date_retour.get().strip()
        
            if not date_emprunt_value or not date_retour_value:
                label.config(text="Veuillez remplir toutes les dates.")
                return
            
            status = status_combobox.get()
            try:
                penalite = float(penalite_entry.get()) if penalite_entry.get() else 0
            except ValueError:
                penalite = 0

            ajouter_emprunt(id_personne,id_livre, date_emprunt_value, date_retour_value, status, penalite)

            id_personne_combobox.set('')
            id_livre_combobox.set('')
            date_emprunt.delete(0, END)
            date_retour.delete(0, END)
            status_combobox.set('')
            penalite_entry.delete(0, END)
            label.config(text="Livre ajoutée avec sucess")
            afficher_emprunt_action()

        submit_button = Button(right_frame, text="Ajouter", bg="green", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=submit_livre)
        submit_button.pack(pady=20)

    def afficher_emprunt_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Listes des Emprunt:", bg="#D8CAB8", font=("Arial", 14))
        label.pack(pady=20)
        table = ttk.Treeview(right_frame, columns=("id_emprunt","id_personne","id_livre","date_emprunt","date_retour","status","penalite"), show="headings", height=5)
        table.pack(pady=8, padx=8, fill=BOTH, expand=True)
        
        table.column("id_emprunt", width=50, anchor="center")
        table.column("id_personne", width=50, anchor="center")
        table.column("id_livre", width=50, anchor="center")
        table.column("date_emprunt", width=200, anchor="center")
        table.column("date_retour", width=150, anchor="center")
        table.column("status", width=50, anchor="center")
        table.column("penalite", width=50, anchor="center")

        table.heading("id_emprunt", text="Id d'emprunt")
        table.heading("id_personne", text="Id de personne")
        table.heading("id_livre", text="Livre")
        table.heading("date_emprunt", text="Date d'emprunt")
        table.heading("date_retour", text="Date de retour")
        table.heading("status", text="Status")
        table.heading("penalite", text="Pénalite")

        emprunts = afficher_emprunt()

        table.tag_configure('even', background='#f0f0f0')
        table.tag_configure('odd', background='#ffffff')

        for i, emprunt in enumerate(emprunts):
            tag = 'even' if i % 2 == 0 else 'odd'
            table.insert("", "end", values=(emprunt['id_emprunt'], emprunt['id_personne'], emprunt['id_livre'], emprunt['date_emprunt'], emprunt['date_retour'], emprunt['status'], emprunt['penalite']), tags=(tag,))

        def rechercher_action():
            id_livre = chercher_entry.get()
            emprunts = chercher_emprunt(id_livre)

            for row in table.get_children():
                table.delete(row)
            
            for emprunt in emprunts:
                table.insert("", "end", values=(emprunt['id_emprunt'], emprunt['id_personne'], emprunt['id_livre'], emprunt['date_emprunt'], emprunt['date_retour'], emprunt['status'], emprunt['penalite']))

        chercher_label = Label(right_frame, text="chercher un emprunt", bg="#D8CAB8", font=("Arial", 12))
        chercher_label.pack(pady=10)

        chercher_entry = Entry(right_frame, font=("Arial", 14))
        chercher_entry.pack(pady=5)

        recherche_button = Button(right_frame, text="Rechercher", bg="orange", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=rechercher_action)
        recherche_button.pack(pady=20)

    def supprimer_emprunt_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Id d'emprunt:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(pady=20)
        emprunt_entry = Entry(right_frame, font=("Arial", 14))
        emprunt_entry.pack(pady=20)

        def suprimer_livre():
            id_emprunt = emprunt_entry.get()
            supprimer_emprunt(id_emprunt)
            emprunt_entry.delete(0, END)
            label.config(text="livre supprimer avec succès!")
            afficher_emprunt_action()

        suprimer_button = Button(right_frame, text="Supprimer", bg="red", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=suprimer_livre)
        suprimer_button.pack(pady=20)

    def afficher_emprunt_personne_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Listes des Emprunt:", bg="#D8CAB8", font=("Arial", 14))
        label.pack(pady=20)
        table = ttk.Treeview(right_frame, columns=("id_emprunt","id_personne","id_livre","date_emprunt","date_retour","status","penalite"), show="headings", height=5)
        table.pack(pady=8, padx=8, fill=BOTH, expand=True)
        
        table.column("id_emprunt", width=50, anchor="center")
        table.column("id_personne", width=50, anchor="center")
        table.column("id_livre", width=50, anchor="center")
        table.column("date_emprunt", width=200, anchor="center")
        table.column("date_retour", width=150, anchor="center")
        table.column("status", width=50, anchor="center")
        table.column("penalite", width=50, anchor="center")

        table.heading("id_emprunt", text="Id d'emprunt")
        table.heading("id_personne", text="Id de personne")
        table.heading("id_livre", text="Livre")
        table.heading("date_emprunt", text="Date d'emprunt")
        table.heading("date_retour", text="Date de retour")
        table.heading("status", text="Status")
        table.heading("penalite", text="Pénalite")

        emprunts = afficher_emprunt()

        table.tag_configure('even', background='#f0f0f0')
        table.tag_configure('odd', background='#ffffff')

        for i, emprunt in enumerate(emprunts):
            tag = 'even' if i % 2 == 0 else 'odd'
            table.insert("", "end", values=(emprunt['id_emprunt'], emprunt['id_personne'], emprunt['id_livre'], emprunt['date_emprunt'], emprunt['date_retour'], emprunt['status'], emprunt['penalite']), tags=(tag,))

        def rechercher_action():
            id_personne = chercher_entry.get()
            emprunts = livre_epmrunter(id_personne)

            for row in table.get_children():
                table.delete(row)
            
            for emprunt in emprunts:
                table.insert("", "end", values=(emprunt['id_emprunt'], emprunt['id_personne'], emprunt['id_livre'], emprunt['date_emprunt'], emprunt['date_retour'], emprunt['status'], emprunt['penalite']))

        chercher_label = Label(right_frame, text="chercher quelqu'un", bg="#D8CAB8", font=("Arial", 12))
        chercher_label.pack(pady=10)

        chercher_entry = Entry(right_frame, font=("Arial", 14))
        chercher_entry.pack(pady=5)

        recherche_button = Button(right_frame, text="Rechercher", bg="orange", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=rechercher_action)
        recherche_button.pack(pady=20)

    
    def afficher_livres_populaires_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Top 10 Livres les Plus Empruntés", bg="#D8CAB8", font=("Arial", 14))
        label.pack(pady=20)

        table = ttk.Treeview(right_frame, columns=("rang", "titre", "emprunts"), show="headings", height=5)
        table.pack(pady=8, padx=8, fill=BOTH, expand=True)

        table.column("rang", width=50, anchor="center")
        table.column("titre", width=200, anchor="center")
        table.column("emprunts", width=100, anchor="center")

        table.heading("rang", text="Rang")
        table.heading("titre", text="Titre")
        table.heading("emprunts", text="Nombre d'emprunts")

        # Call the function to get top 10 borrowed books
        livres_populaires = livres_plus_empruntes()

        # Add entries to the table
        for i, livre in enumerate(livres_populaires):
            table.insert("", "end", values=(i+1, livre['titre'], livre['emprunts']))



    #initiazation for persones buttons
    cat_label = Label(left_frame, text="Gestion des Personne:", bg="grey", fg="white", font=("Arial", 12))
    cat_label.pack(pady=20, padx=50)
    
    #personnes buttons
    add_button = Button(left_frame, text="Ajouter une Personne", bg="green", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=ajouter_personne_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Modifier une Personne", bg="yellow", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=modifier_personne_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Aficher les Personnes", bg="orange", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=afficher_personne_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Suprimer une Personne", bg="red", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=supprimer_personne_action)
    add_button.pack(pady=10, padx=50)

    ##initiazation for emprunts buttons
    livres_label = Label(left_frame, text="Gestion des Emprunt:", bg="grey", fg="white", font=("Arial", 12))
    livres_label.pack(pady=20, padx=50)

    #emprunts buttons
    add_button = Button(left_frame, text="Ajouter un Emprunt", bg="green", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=ajouter_emprunt_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Aficher les Emprunt", bg="orange", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=afficher_emprunt_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Suprimer un Emprunt", bg="red", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=supprimer_emprunt_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Emrunt par personne", bg="brown", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=afficher_emprunt_personne_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="test", bg="brown", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=afficher_livres_populaires_action)
    add_button.pack(pady=10, padx=50)

    window.mainloop()

interface_personnes_ui()