#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
name_layout = QHBoxLayout()
pass_layout = QHBoxLayout()

name = QLineEdit()
name_label = QLabel("username: ")
name_layout.addWidget(name_label)
name_layout.addWidget(name)

password_label = QLabel("password: ")
password = QLineEdit()
password.setEchoMode(QLineEdit.Password)
pass_layout.addWidget(password_label)
pass_layout.addWidget(password)

send_btn = QPushButton("Login")

response = QLabel("")

layout.addWidget(response)
layout.addLayout(name_layout)
layout.addLayout(pass_layout)
layout.addWidget(send_btn)

window.setLayout(layout)
window.show()

app.exec_()

