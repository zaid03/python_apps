import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

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

class BankAccountApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Bank Account System')
        self.setGeometry(0, 0, 800, 600)

        self.compte_espargne = CompteBancaire("Zaid", 1000)

        # Initialize pages once
        self.welcome_widget = self.create_welcome_page()
        self.main_widget = self.create_main_page()
        self.deposit_widget = self.create_deposit_page()
        self.withdraw_widget = self.create_withdraw_page()

        # Show the welcome page initially
        self.setCentralWidget(self.welcome_widget)

    def create_welcome_page(self):
        welcome_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        welcome_label = QLabel('Bienvenue dans la Banque CIH (Système 5asar)')
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet('font-size: 24px; font-weight: bold; margin-bottom: 20px;')
        layout.addWidget(welcome_label)

        enter_button = QPushButton('Entrer')
        enter_button.setFixedSize(200, 40)
        enter_button.setStyleSheet('font-size: 16px; padding: 10px 20px; background-color: #3b8ea5; color: white; border-radius: 10px;')
        enter_button.clicked.connect(self.show_main_page)
        layout.addWidget(enter_button)
        
        welcome_widget.setLayout(layout)
        return welcome_widget

    def create_main_page(self):
        main_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title_label = QLabel(f"Bienvenue, {self.compte_espargne.titulaire}")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet('font-size: 18px; font-weight: bold; margin-bottom: 20px;')
        layout.addWidget(title_label)

        deposit_button = QPushButton("Dépôt")
        withdraw_button = QPushButton("Retrait")

        for button in (deposit_button, withdraw_button):
            button.setStyleSheet('font-size: 16px; padding: 10px 20px; background-color: #3b8ea5; color: white; border-radius: 10px;')
            button.setFixedSize(200, 40)

        deposit_button.clicked.connect(self.show_deposit_page)
        withdraw_button.clicked.connect(self.show_withdraw_page)

        layout.addWidget(deposit_button)
        layout.addWidget(withdraw_button)

        main_widget.setLayout(layout)
        return main_widget

    def create_deposit_page(self):
        deposit_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        balance_label = QLabel(f"Solde actuel : {self.compte_espargne.solde} MAD")
        balance_label.setAlignment(Qt.AlignCenter)
        balance_label.setStyleSheet('font-size: 18px; font-weight: bold; margin-bottom: 20px;')
        layout.addWidget(balance_label)

        deposit_label = QLabel("Entrez le montant du dépôt")
        deposit_label.setAlignment(Qt.AlignCenter)
        deposit_label.setStyleSheet('font-size: 18px; margin-bottom: 20px;')
        layout.addWidget(deposit_label)

        self.deposit_input = QLineEdit()
        self.deposit_input.setFixedWidth(300)
        layout.addWidget(self.deposit_input)

        confirm_deposit_button = QPushButton("Confirmer le dépôt")
        confirm_deposit_button.setStyleSheet('font-size: 16px; padding: 10px 20px; background-color: #3b8ea5; color: white; border-radius: 10px;')
        confirm_deposit_button.setFixedSize(200, 40)
        confirm_deposit_button.clicked.connect(lambda: self.perform_deposit(balance_label))
        
        layout.addWidget(confirm_deposit_button)

        deposit_widget.setLayout(layout)
        return deposit_widget

    def create_withdraw_page(self):
        withdraw_widget = QWidget()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        balance_label = QLabel(f"Solde actuel : {self.compte_espargne.solde} MAD")
        balance_label.setAlignment(Qt.AlignCenter)
        balance_label.setStyleSheet('font-size: 18px; font-weight: bold; margin-bottom: 20px;')
        layout.addWidget(balance_label)

        withdraw_label = QLabel("Entrez le montant du retrait")
        withdraw_label.setAlignment(Qt.AlignCenter)
        withdraw_label.setStyleSheet('font-size: 18px; margin-bottom: 20px;')
        layout.addWidget(withdraw_label)

        self.withdraw_input = QLineEdit()
        self.withdraw_input.setFixedWidth(300)
        layout.addWidget(self.withdraw_input)

        confirm_withdraw_button = QPushButton("Confirmer le retrait")
        confirm_withdraw_button.setStyleSheet('font-size: 16px; padding: 10px 20px; background-color: #3b8ea5; color: white; border-radius: 10px;')
        confirm_withdraw_button.setFixedSize(200, 40)
        confirm_withdraw_button.clicked.connect(lambda: self.perform_withdraw(balance_label))
        
        layout.addWidget(confirm_withdraw_button)

        withdraw_widget.setLayout(layout)
        return withdraw_widget

    def show_main_page(self):
        self.setCentralWidget(self.main_widget)

    def show_deposit_page(self):
        self.setCentralWidget(self.deposit_widget)

    def show_withdraw_page(self):
        self.setCentralWidget(self.withdraw_widget)

    def perform_deposit(self, balance_label):
        try:
            amount = float(self.deposit_input.text())
            self.compte_espargne.deposer(amount)
            balance_label.setText(f"Solde actuel : {self.compte_espargne.solde} MAD")
            QMessageBox.information(self, "Succès", f"Vous avez déposé {amount} MAD.")
            self.deposit_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un nombre valide")

    def perform_withdraw(self, balance_label):
        try:
            amount = float(self.withdraw_input.text())
            if self.compte_espargne.retirer(amount):
                balance_label.setText(f"Solde actuel : {self.compte_espargne.solde} MAD")
                QMessageBox.information(self, "Succès", f"Vous avez retiré {amount} MAD.")
            else:
                QMessageBox.warning(self, "Erreur", "Solde insuffisant")
            self.withdraw_input.clear()
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un nombre valide")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BankAccountApp()
    window.showMaximized()
    sys.exit(app.exec_())
