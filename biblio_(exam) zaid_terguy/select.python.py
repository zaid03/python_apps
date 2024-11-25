import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'bibliotheque'
}

# Function to fetch data from MySQL
def fetch_data():
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Query to fetch data
        cursor.execute("SELECT id, title FROM livres")
        data = cursor.fetchall()

        # Extract only names to display in dropdown
        return [f"{row[1]} (ID: {row[0]})" for row in data]

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return []

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Create the main application window
root = tk.Tk()
root.title("Database Dropdown with Tkinter")
root.geometry("300x200")

# Fetch data from the database
options = fetch_data()

# Check if options are available
if options:
    # Variable for selected option
    selected_option = tk.StringVar(root)
    selected_option.set(options[0])  # Set the default to the first item

    # Dropdown Menu (OptionMenu)
    option_menu = tk.OptionMenu(root, selected_option, *options)
    option_menu.pack(pady=20)
else:
    label_no_data = tk.Label(root, text="No data available.")
    label_no_data.pack(pady=20)

# Function to display the selected option
def submit():
    messagebox.showinfo("Selected Option", f"You selected: {selected_option.get()}")

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=20)

# Run the application
root.mainloop()