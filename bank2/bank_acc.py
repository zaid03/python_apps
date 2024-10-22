class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"deposé {montant} MAD. nouveau solde: {self.solde}MAD")

    def retirer(self, montant):
        if montant < self.solde:
            self.solde -= montant
            print(f"retiré {montant} MAD. nouveau solde: {self.solde} MAD")
        else:
            print("votre solde est insuffisant")
    
    def afficher_solde(self):
        print(f"votre solde est de {self.solde} DH")
    
class CompteEspargne(CompteBancaire):
    def __init__(self, titulaire, solde, taux_interet):
        super().__init__(titulaire, solde)
        self.taux_interet = taux_interet
    
    def ajouter_interets(self):
        interets = self.solde * (self.taux_interet / 100)
        self.solde += interets
        print(f"intérêts ajoutes: {interets} MAD nouveau solde: {self.solde} mad")
    
class CompteCourant(CompteBancaire):
    def __init__(self, titulaire, solde, decouvert_autorise):
        super().__init__(titulaire, solde)
        self.decouvert_autorise = decouvert_autorise

    def retiter(self, montant):
        if montant <= self.solde + self.decouvert_autorise:
            self.solde -= montant
            print(f"retiré {montant} MAD. nouveau solde: {self.solde} MAD")
        else:
            print(f"impossible de retirer {montant} MAD. limite dépassé")


compte_espargne = CompteEspargne("zaid", 1000, 5)
compte_espargne.ajouter_interets()
compte_espargne.afficher_solde

compte_courant = CompteCourant("abir", 500, 200)
compte_courant.retirer(800)

compte_courant.afficher_solde()
compte_courant.retirer(150)