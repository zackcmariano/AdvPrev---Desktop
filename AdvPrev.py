from PyQt5 import uic, QtWidgets
from PyQt5 import QtGui
import mysql.connector
import webbrowser

'''IMPORTING THE DATABASE MODULE'''
banco = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="ZACKADM",
        passwd="Mk2855ssb#",
        database="advprev"
    )

def loginscreen():
    user = login.lineEdit.text()
    passw = login.lineEdit_2.text()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM advogados WHERE login = '{}' and senha = '{}'".format(user, passw))
    verificar = cursor.fetchone()
    try:
        if (user in verificar and passw in verificar):
            login.close()
            logged.show()
            logged.label_16.setText('{}'.format(user))

    except:
        login.label_6.setText("Dados de login incorretos !")
        login.lineEdit.setText("")
        login.lineEdit_2.setText("")

def registerscreen():
    login.close()
    register.show()

def newregister():
    login = register.lineEdit_5.text()
    nome = register.lineEdit.text()
    email = register.lineEdit_4.text()
    senha = register.lineEdit_2.text()
    c_senha = register.lineEdit_3.text()


    if (senha == c_senha):
        try:
            cursor = banco.cursor()
            cursor.execute("INSERT INTO advogados (login, nome, email, senha) VALUES('" + login + "','" + nome + "','" + email + "','" + senha + "')")
            banco.commit()
            banco.close()
            register.label_3.setText("Usuario Cadastrado com Sucesso")


        except mysql as erro:
            print("Print ao inserir dados", erro)

    else:
        register.label_3.setText("Dados incompletos ou senhas não conferem")

def home():
    logged.frame_3.show()

def web():
    logged.frame_2.show()
    logged.frame_3.close()

def graph():
    logged.frame.show()
    logged.frame_2.close()

def jusbras():
    webbrowser.open('https://www.jusbrasil.com.br/home')

def inss():
    webbrowser.open('https://meu.inss.gov.br/')

def close():
    logged.close()


#READING THE UI FILES#
app=QtWidgets.QApplication([])
login=uic.loadUi("login.ui")
register=uic.loadUi("register.ui")
logged=uic.loadUi("wid_logg.ui")

login.pushButton_2.clicked.connect(registerscreen)
login.pushButton.clicked.connect(loginscreen)
register.pushButton.clicked.connect(newregister)
logged.pushButton_3.clicked.connect(web)
logged.pushButton_4.clicked.connect(graph)
logged.pushButton_2.clicked.connect(home)
logged.pushButton_7.clicked.connect(close)
logged.pushButton.clicked.connect(jusbras)
logged.pushButton_6.clicked.connect(inss)

#INSERT IMAGE#
icon=QtGui.QPixmap([])
login.label_4.setPixmap(QtGui.QPixmap('logoadv.png'))
login.label_5.setPixmap(QtGui.QPixmap('justice.png'))
register.label_4.setPixmap(QtGui.QPixmap('logoadv_rg.png'))
logged.label_17.setPixmap(QtGui.QPixmap('icon.png'))
logged.label_23.setPixmap(QtGui.QPixmap('logoadv_rg.png'))
logged.label_19.setPixmap(QtGui.QPixmap('prev.png'))
logged.label_11.setPixmap(QtGui.QPixmap('pagjus.png'))
logged.label.setPixmap(QtGui.QPixmap('GraphStates.png'))
logged.label_2.setPixmap(QtGui.QPixmap('GraphMotive.png'))

login.show()
app.exec()