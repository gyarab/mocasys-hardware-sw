#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit
import urllib.request
import json

middleend_host = "127.0.0.1"
middleend_port = "80"

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
#button has no action to avoid crash

response = QLabel("")

layout.addWidget(response)
layout.addLayout(name_layout)
layout.addLayout(pass_layout)
layout.addWidget(send_btn)

window.setLayout(layout)
window.show()

app.exec_()

def login(login, password):
    auth = {'username':[username], 'password':[password]}
    req = urllib.request.Request(middleend_host+"/auth/password")
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(auth)
    jsondata_bytes = jsondata.encode('utf-8')
    req.add_header('Content-Length', len(jsondata_bytes))
    auth_token_json = urllib.request.urlopen(req, jsondata_bytes)
    #not sure how to parse errors
