import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox, QComboBox

class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            return True
        else:
            return False

    def afficher_solde(self):
        return self.solde

class CompteEspargne(CompteBancaire):
    def __init__(self, titulaire, solde, taux_interet):
        super().__init__(titulaire, solde)
        self.taux_interet = taux_interet

    def ajouter_interets(self):
        interets = self.solde * (self.taux_interet / 100)
        self.solde += interets

class CompteCourant(CompteBancaire):
    def __init__(self, titulaire, solde, decouvert_autorise):
        super().__init__(titulaire, solde)
        self.decouvert_autorise = decouvert_autorise

    def retirer(self, montant):
        if montant <= self.solde + self.decouvert_autorise:
            self.solde -= montant
            return True
        else:
            return False

class BankAccountApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Bank Account System')
        self.setGeometry(0, 0, 800, 600)

        self.layout = QVBoxLayout()

        self.title_label = QLabel('Bienvenue dans la Banque cih (système 5asar)', self)
        self.title_label.setStyleSheet('font-size: 24px; font-weight: bold;')
        self.layout.addWidget(self.title_label)

        self.account_type = QComboBox(self)
        self.account_type.addItems(["Savings Account", "Current Account"])
        self.layout.addWidget(self.account_type)

        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Enter amount")
        self.layout.addWidget(self.amount_input)

        self.deposit_button = QPushButton("Deposit", self)
        self.withdraw_button = QPushButton("Withdraw", self)

        self.deposit_button.clicked.connect(self.deposit)
        self.withdraw_button.clicked.connect(self.withdraw)

        self.layout.addWidget(self.deposit_button)
        self.layout.addWidget(self.withdraw_button)

        self.setLayout(self.layout)

        self.showMaximized()

        self.compte_espargne = CompteEspargne("Zaid", 1000, 5)
        self.compte_courant = CompteCourant("Abir", 500, 200)

    def deposit(self):
        try:
            amount = float(self.amount_input.text())
            account_type = self.account_type.currentText()

            if account_type == "Savings Account":
                self.compte_espargne.deposer(amount)
                QMessageBox.information(self, "Success", f"Deposited {amount} MAD to Savings Account")
            else: 
                self.compte_courant.deposer(amount)
                QMessageBox.information(self, "Success", f"Deposited {amount} MAD to Current Account")

            self.amount_input.clear() 
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid number")

    def withdraw(self):
        try:
            amount = float(self.amount_input.text())
            account_type = self.account_type.currentText()
            success = False

            if account_type == "Savings Account":
                success = self.compte_espargne.retirer(amount)
            else:
                success = self.compte_courant.retirer(amount)

            if success:
                QMessageBox.information(self, "Success", f"Withdrew {amount} MAD from {account_type}")
            else:
                QMessageBox.warning(self, "Error", "Insufficient balance or limit exceeded")

            self.amount_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid number")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankAccountApp()
    sys.exit(app.exec_())
