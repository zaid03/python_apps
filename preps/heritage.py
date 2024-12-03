class Animal:
    def __init__(self, nom, age, parler):
        self.nom = nom
        self.age = age
        self.parler = parler
    
    def afficher(self):
        print(f"nom: {self.nom}")
        print(f"age: {self.age}")
        print(f"son: {self.parler}\n")

class Chien(Animal):
    def __init__(self, nom, age):
        super().__init__(nom, age, "Wouf!")

class Chat(Animal):
    def __init__(self, nom, age):
        super().__init__(nom,age, "Miaw!")

kelb = Chien("jojo", "5")
kelb.afficher()

kita = Chat("momo", "10")
kita.afficher()