class CompteBancaire:
    def __init__(self, taux_interet, titulaire, solde):
        self.taux_interet = taux_interet
        self.titulaire = titulaire
        self.solde = solde
    
    def depot(self, montant_ajoute):
        self.solde += montant_ajoute
        return self.solde
    
    def retrait(self, montant_ret):
        if montant_ret <= self.solde:
            self.solde -= montant_ret
            return self.solde
        else:
            print("solde insuffisant")
            return self.solde

    def calculer_interet(self):
        interet = self.solde * self.taux_interet
        self.solde += interet
        return interet
    

compte = CompteBancaire(0.03, "zaid", 1000)
print(compte.solde)

montant_ajoute = int(input("depot: "))
compte.depot(montant_ajoute)
print(compte.solde)

montant_ret = int(input("retrait: "))
compte.retrait(montant_ret) 
print(compte.solde)

interet = compte.calculer_interet()
print(f"intérét: {interet}")
print(f"Solde apres les interet: {compte.solde}")