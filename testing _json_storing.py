import json

#after importing json file we type this function to load or create a new json file#
def load_names():
    try:
        with open('name.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
#function to save data into json
def save_names(names):
    with open('name.json', 'w') as file:
        json.dump(names, file, indent = 4)

#main function
def name():
    names = load_names() #to load existing names

    user_name = input("enter your name: ")
    print(f"Hello, {user_name}") 

    names.append(user_name) #to add new name to the list
    save_names(names) #to save the new name to the json file

name()
