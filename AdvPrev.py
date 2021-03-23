'''IMPORT OF LIBRARIES REQUIRED FOR 
THE CONSTRUCTION OF ALGORITHM'''
from PyQt5 import uic, QtWidgets
from PyQt5 import QtGui
import mysql.connector
import webbrowser


#CONNECTION TO THE MYSQL DATABASE 
#FOR VALIDATION AND INSERTING OF APPLICATION DATA.
banco = mysql.connector.connect(
        host="insert host",
        port="insert port",
        user="insert user",
        passwd="insert password",
        database="insert database"
    )


#INITIAL APPLICATION SCREEN, RECEIVING USER DATA AND 
# VALIDATING IN THE DATABASE
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


#OPENING THE REGISTRATION SCREEN
def registerscreen():
    login.close()
    register.show()


#CONNECTING TO THE DATABASE AND INSERTING A NEW USER
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


#ACCESS HOME
def home():
    logged.frame_3.show()


#ACCESS WEB SCREEN
def web():
    logged.frame_2.show()
    logged.frame_3.close()


#ACCESS DATA SCREEN
def graph():
    logged.frame.show()
    logged.frame_2.close()


#ACCESS THE JUSBRASIL WEBSITE
def jusbras():
    webbrowser.open('https://www.jusbrasil.com.br/home')


#ACCESS THE INSS WEBSITE
def inss():
    webbrowser.open('https://meu.inss.gov.br/')


#FINISH APPLICATION
def close():
    logged.close()


#READING THE SCREEN FILES IN UI FORMAT
app=QtWidgets.QApplication([])
login=uic.loadUi("login.ui")
register=uic.loadUi("register.ui")
logged=uic.loadUi("wid_logg.ui")


#ADDING FUNCTIONALITY TO THE SCREEN BUTTONS
login.pushButton_2.clicked.connect(registerscreen)
login.pushButton.clicked.connect(loginscreen)
register.pushButton.clicked.connect(newregister)
logged.pushButton_3.clicked.connect(web)
logged.pushButton_4.clicked.connect(graph)
logged.pushButton_2.clicked.connect(home)
logged.pushButton_7.clicked.connect(close)
logged.pushButton.clicked.connect(jusbras)
logged.pushButton_6.clicked.connect(inss)


#INSERTING IMAGES ON SCREENS
icon=QtGui.QPixmap([])
login.label_4.setPixmap(QtGui.QPixmap('img\logoadv.png'))
login.label_5.setPixmap(QtGui.QPixmap('img\justice.png'))
register.label_4.setPixmap(QtGui.QPixmap('img\logoadv_rg.png'))
logged.label_17.setPixmap(QtGui.QPixmap('img\icon.png'))
logged.label_23.setPixmap(QtGui.QPixmap('img\logoadv_rg.png'))
logged.label_19.setPixmap(QtGui.QPixmap('img\prev.png'))
logged.label_11.setPixmap(QtGui.QPixmap('img\pagjus.png'))
logged.label.setPixmap(QtGui.QPixmap('img\GraphStates.png'))
logged.label_2.setPixmap(QtGui.QPixmap('img\GraphMotive.png'))


#INITIALIZING THE APPLICATION
login.show()
app.exec()