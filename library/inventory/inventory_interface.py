from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from sql_funtions import *

#global function ui for main interface
def interface_stock_ui():
    window = Tk()
    window.title("Gestion des stocks")
    window.geometry("1366x768")
    window.configure(bg="#2E2E2E")

    #initialization of the left frame for buttons and right frame for button's content
    right_frame = Frame(window, bg="#D8CAB8", width=800, height=768)
    right_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    left_frame = Frame(window, bg="grey", width=100, height=768)
    left_frame.pack(side=LEFT, fill=Y)

    #buttons functions
    def ajouter_signal_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Titre de Livre:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        titre_entry = Entry(right_frame, font=("Arial", 14))
        titre_entry.pack(padx=10)

        label = Label(right_frame, text="Auteur de livre:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        auteur_entry = Entry(right_frame, font=("Arial", 14))
        auteur_entry.pack(padx=10)

        label = Label(right_frame, text="Etat de livre:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(padx=10)
        options = ['endomages', 'perdus']
        status_combobox = ttk.Combobox(right_frame, font=("Arial", 14), values=options)
        status_combobox.pack(padx=10)

        def submit_livre():
            titre = titre_entry.get()
            auteur = auteur_entry.get()
            status = status_combobox.get()
            ajouter_stock(titre, auteur, status)
            titre_entry.delete(0, END)
            auteur_entry.delete(0, END)
            status_combobox.set('')
            label.config(text="livre ajoutée avec succès!")
            afficher_signal_action()

        submit_button = Button(right_frame, text="Ajouter", bg="green", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=submit_livre)
        submit_button.pack(pady=20)

    def afficher_signal_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Listes des signales:", bg="#D8CAB8", font=("Arial", 14))
        label.pack(pady=20)
        table = ttk.Treeview(right_frame, columns=("id","titre","auteur","status"), show="headings", height=5)
        table.pack(pady=8, padx=8, fill=BOTH, expand=True)

        table.column("id", width=50, anchor="center")
        table.column("titre", width=50, anchor="center")
        table.column("auteur", width=200, anchor="center")
        table.column("status", width=150, anchor="center")

        table.heading("id", text="Id")
        table.heading("titre", text="Titre")
        table.heading("auteur", text="Auteur")
        table.heading("status", text="Status")

        signales = afficher_stock()

        table.tag_configure('even', background='#f0f0f0')
        table.tag_configure('odd', background='#ffffff')

        for i, signal in enumerate(signales):
            tag = 'even' if i % 2 == 0 else 'odd'
            table.insert("", "end", values=(signal['id'], signal['titre'], signal['auteur'], signal['status']), tags=(tag,))

        def rechercher_action():
            titre = chercher_entry.get()
            signales = rechercher_stock(titre)

            for row in table.get_children():
                table.delete(row)
            
            table.tag_configure('even', background='#f0f0f0')
            table.tag_configure('odd', background='#ffffff')
            for i, signal in enumerate(signales):
                tag = 'even' if i % 2 == 0 else 'odd'
                table.insert("", "end", values=(signal['id'], signal['titre'], signal['auteur'], signal['status']), tags=(tag,))

        chercher_label = Label(right_frame, text="chercher un titre", bg="#D8CAB8", font=("Arial", 12))
        chercher_label.pack(pady=10)

        chercher_entry = Entry(right_frame, font=("Arial", 14))
        chercher_entry.pack(pady=5)

        recherche_button = Button(right_frame, text="Rechercher", bg="orange", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=rechercher_action)
        recherche_button.pack(pady=20)

    def supprimer_signal_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Id de signal:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(pady=20)
        signal_entry = Entry(right_frame, font=("Arial", 14))
        signal_entry.pack(pady=20)

        def suprimer_livre():
            id = signal_entry.get()
            supprimer_stock(id)
            signal_entry.delete(0, END)
            label.config(text="signal supprimer avec succès!")
            afficher_signal_action()

        suprimer_button = Button(right_frame, text="Supprimer", bg="red", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=suprimer_livre)
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

    def ajouter_reservation_action():
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

        label = Label(right_frame, text="Date de reservation:", bg="#D8CAB8", fg="white", font=("Arial", 14))
        label.pack(padx=10)
        date_reserv = Entry(right_frame, font=("Arial", 14))
        date_reserv.pack(padx=10)
        date_reserv.bind("<Button-1>", lambda event: open_calendar(date_reserv))

        def submit_reservation():
            selected_personne_name = id_personne_combobox.get()
            id_personne = personne_dict.get(selected_personne_name)
            selected_livre_name = id_livre_combobox.get()
            id_livre = livre_dict.get(selected_livre_name)
            date_reserv_value = date_reserv.get().strip()
        
            if not date_reserv_value:
                label.config(text="Veuillez remplir toutes les dates.")
                return

            ajouter_reservation(id_personne,id_livre, date_reserv_value)

            id_personne_combobox.set('')
            id_livre_combobox.set('')
            date_reserv.delete(0, END)
            label.config(text="Reservation ajoutée avec sucess")
            afficher_reservation_action()

        submit_button = Button(right_frame, text="Ajouter", bg="green", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=submit_reservation)
        submit_button.pack(pady=20)

    def afficher_reservation_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Listes des reservation:", bg="#D8CAB8", font=("Arial", 14))
        label.pack(pady=20)
        table = ttk.Treeview(right_frame, columns=("id","id_personne","id_livre","reserv_date"), show="headings", height=5)
        table.pack(pady=8, padx=8, fill=BOTH, expand=True)
        
        table.column("id", width=50, anchor="center")
        table.column("id_personne", width=50, anchor="center")
        table.column("id_livre", width=50, anchor="center")
        table.column("reserv_date", width=200, anchor="center")

        table.heading("id", text="Id d'emprunt")
        table.heading("id_personne", text="Id de personne")
        table.heading("id_livre", text="Livre")
        table.heading("reserv_date", text="Date d'emprunt")

        reservations = afficher_reservation()

        table.tag_configure('even', background='#f0f0f0')
        table.tag_configure('odd', background='#ffffff')

        for i, reservation in enumerate(reservations):
            tag = 'even' if i % 2 == 0 else 'odd'
            table.insert("", "end", values=(reservation['id'], reservation['id_personne'], reservation['id_livre'], reservation['reserv_date'],), tags=(tag,))

        def rechercher_action():
            id_personne = chercher_entry.get()
            reservations = chercher_reservation(id_personne)

            for row in table.get_children():
                table.delete(row)
            
            table.tag_configure('even', background='#f0f0f0')
            table.tag_configure('odd', background='#ffffff')
            
            for i, reservation in enumerate(reservations):
                tag = 'even' if i % 2 == 0 else 'odd'
                table.insert("", "end", values=(reservation['id'], reservation['id_personne'], reservation['id_livre'], reservation['reserv_date'],), tags=(tag,))

        chercher_label = Label(right_frame, text="chercher un reservation", bg="#D8CAB8", font=("Arial", 12))
        chercher_label.pack(pady=10)

        chercher_entry = Entry(right_frame, font=("Arial", 14))
        chercher_entry.pack(pady=5)

        recherche_button = Button(right_frame, text="Rechercher", bg="orange", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=rechercher_action)
        recherche_button.pack(pady=20)

    def supprimer_reservation_action():
        for widget in right_frame.winfo_children():
            widget.destroy()

        label = Label(right_frame, text="Id de reservation:", bg="#D8CAB8",fg="white", font=("Arial", 14))
        label.pack(pady=20)
        reserv_entry = Entry(right_frame, font=("Arial", 14))
        reserv_entry.pack(pady=20)

        def suprimer_livre():
            id = reserv_entry.get()
            supprimer_reservation(id)
            reserv_entry.delete(0, END)
            label.config(text="livre supprimer avec succès!")
            afficher_reservation_action()

        suprimer_button = Button(right_frame, text="Supprimer", bg="red", fg="white", font=("Arial", 12), width=15, height=1, bd=2, relief="flat", command=suprimer_livre)
        suprimer_button.pack(pady=20)

    #stock buttons
    cat_label = Label(left_frame, text="Gestion des stock:", bg="grey", fg="white", font=("Arial", 12))
    cat_label.pack(pady=20, padx=50)

    add_button = Button(left_frame, text="signaler un livre", bg="green", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=ajouter_signal_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Aficher les signales", bg="orange", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10),command=afficher_signal_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Suprimer un signal", bg="red", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=supprimer_signal_action)
    add_button.pack(pady=10, padx=50)

    #reservations buttons
    livres_label = Label(left_frame, text="Gestion des reservations:", bg="grey", fg="white", font=("Arial", 12))
    livres_label.pack(pady=20, padx=50)

    add_button = Button(left_frame, text="Ajouter un reservation", bg="green", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=ajouter_reservation_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Aficher les reservations", bg="orange", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10),command=afficher_reservation_action)
    add_button.pack(pady=10, padx=50)
    add_button = Button(left_frame, text="Suprimer un reservation", bg="red", fg="white", width=20, height=2, bd=2, relief="flat", font=("Arial", 10), command=supprimer_reservation_action)
    add_button.pack(pady=10, padx=50)

    window.mainloop()

interface_stock_ui()