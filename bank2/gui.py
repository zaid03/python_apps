import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5 import QtCore

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Bank of Tetuan')
window.setGeometry(0, 0, 800, 600)

layout = QVBoxLayout()

title_label = QLabel('Bienvenue', window)
title_label.setStyleSheet('font-size: 24px; font-weight: bold;c')
title_label.setAlignment(QtCore.Qt.AlignCenter)
layout.addWidget(title_label)


layout.addWidget(title_label)

deposit_button = QPushButton("Deposit", window)
withdraw_button = QPushButton("Withdraw", window)

layout.addWidget(deposit_button)
layout.addWidget(withdraw_button)

window.setLayout(layout)

window.showMaximized()

sys.exit(app.exec_())