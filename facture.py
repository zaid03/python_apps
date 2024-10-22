class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

class Facture:
    def __init__(self, produits):
        self.produits = produits

    def ajouter_produit(self, produits):
        self.produit.append(produits)

    def cout_total(self, produits):
         return sum([produit.prix * produit.quantite for produit in self.produits])
        
    def afficher(self):
        for produit in self.produits:
            print(f"{produit.nom}, {produit.prix} dh/kg, {produit.quantite} kg")
        print(f"Coût total: {self.cout_total(self.produits)} dh")

produit1 = Produit("Pomme", 2, 3)
produit2 = Produit("banane", 3, 2)
produit3 = Produit("orange", 1, 5)

facture = Facture([produit1, produit2, produit3])
facture.afficher()