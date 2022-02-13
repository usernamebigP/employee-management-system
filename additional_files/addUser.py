from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import MySQLConnection, Error
class Ui_MainWindow(object):

    def __init__(self,db):
        self.db=db

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 455)
        MainWindow.setMaximumSize(QtCore.QSize(953, 455))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("*{\n"
"font-size:20px;\n"
"font-family:century gothic;\n"
"background-color: rgb(255, 255, 217);\n"
"font-weight:bold;\n"
"}\n"
"\n"
"\n"
"QLabel#heading{\n"
"    font-size:30px;\n"
"    color:white;\n"
"    background:rgb(15,73,61);\n"
"    font-weight:bold;\n"
"}\n"
"QLineEdit{\n"
"    background:white;\n"
"}\n"
"QPushButton{\n"
"    background:rgb(15,73,61);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox{\n"
"background:white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.heading = QtWidgets.QLabel(self.frame)
        self.heading.setGeometry(QtCore.QRect(-3, 0, 941, 51))
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.usernameEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameEdit.setGeometry(QtCore.QRect(210, 110, 251, 29))
        self.usernameEdit.setObjectName("usernameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordEdit.setGeometry(QtCore.QRect(210, 170, 251, 29))
        self.passwordEdit.setObjectName("passwordEdit")
        self.conpasswordEdit = QtWidgets.QLineEdit(self.frame)
        self.conpasswordEdit.setGeometry(QtCore.QRect(210, 220, 251, 29))
        self.conpasswordEdit.setObjectName("conpasswordEdit")
        self.accessEdit = QtWidgets.QComboBox(self.frame)
        self.accessEdit.setGeometry(QtCore.QRect(640, 100, 191, 41))
        self.accessEdit.setObjectName("accessEdit")
        self.accessEdit.addItem("")
        self.accessEdit.addItem("")
        self.accessEdit.setEditable(True)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 110, 101, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 181, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(495, 100, 131, 41))
        self.label_4.setObjectName("label_4")
        self.submit = QtWidgets.QPushButton(self.frame)
        self.submit.setGeometry(QtCore.QRect(210, 280, 75, 31))
        self.submit.setObjectName("submit")
        self.status = QtWidgets.QLabel(self.frame)
        self.status.setGeometry(QtCore.QRect(0, 360, 931, 31))
        self.status.setStyleSheet("color:white;\n"
"background:rgb(15,73,61)")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 953, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.status.hide()
        MainWindow.setWindowTitle(_translate("MainWindow", "Add User"))
        self.passwordEdit.setEchoMode(2)
        self.conpasswordEdit.setEchoMode(2)
        self.heading.setText(_translate("MainWindow", "Create new User"))
        self.accessEdit.setItemText(0, _translate("MainWindow", "Read"))
        self.accessEdit.setItemText(1, _translate("MainWindow", "Write"))
        self.label.setText(_translate("MainWindow", "username:"))
        self.label_2.setText(_translate("MainWindow", "password:"))
        self.label_3.setText(_translate("MainWindow", "confirm password:"))
        self.label_4.setText(_translate("MainWindow", "access type:"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.status.setText(_translate("MainWindow", "Status"))
 
        #setting click event on submit button
        self.submit.clicked.connect(self.submitDetails)

        #actions for enter key
        self.usernameEdit.returnPressed.connect(self.passwordEdit.setFocus)
        self.passwordEdit.returnPressed.connect(self.conpasswordEdit.setFocus)
        self.conpasswordEdit.returnPressed.connect(self.accessEdit.setFocus)
        self.accessEdit.lineEdit().returnPressed.connect(self.submit.click)


    #checking if the user doesn't already exists
    def checkUser(self,user):
        cur=self.db.cursor()
        cur.execute('select user from mysql.user where user="{}"'.format(user))
        data=cur.fetchall()
        if(not data):
            return True
        else:
            return False

    #submitting details
    def submitDetails(self):
        if(self.usernameEdit.text()!=""):
            if(self.passwordEdit.text()==self.conpasswordEdit.text() and self.passwordEdit.text()!='' and self.conpasswordEdit.text()!=''):
                if(self.checkUser(self.usernameEdit.text())):
                    
                    #creating a user
                    cur=self.db.cursor()
                    cur.execute('create user "{}"@"localhost" identified by "{}"'.format(self.usernameEdit.text(),self.passwordEdit.text()))
                    self.db.commit()

                    #checking access type for the user
                    if(self.accessEdit.currentText()=='Read'):
                        cur.execute('grant select on *.* to "{}"@"localhost"'.format(self.usernameEdit.text()))

                    elif(self.accessEdit.currentText()=="Write"):
                        cur.execute('grant select,update,insert,delete on *.* to "{}"@"localhost"'.format(self.usernameEdit.text()))

                    #status GUI
                    self.status.show()
                    self.status.setStyleSheet('color:white;background:rgb(15,73,61)')
                    self.status.setText('{} added successfully with {} access'.format(self.usernameEdit.text(),self.accessEdit.currentText()))
                    self.clearData()

                else:
                    self.status.show()
                    self.status.setStyleSheet('background:rgb(212,115,70);color:white;')
                    self.status.setText('User already exists !!')
                    self.usernameEdit.setFocus()
                    self.clearData()        

            else:
                self.passwordEdit.setText('')
                self.conpasswordEdit.setText('')
                self.passwordEdit.setFocus()
                self.status.show()
                self.status.setStyleSheet('background:rgb(212,115,70);color:white')
                self.status.setText("passwords do not match !!!")

        else:
            self.conpasswordEdit.setText('')
            self.usernameEdit.setFocus()
            self.status.show()
            self.status.setStyleSheet('background:rgb(212,115,70);color:white')
            self.status.setText('Enter a user first !!')

    def clearData(self):
        self.usernameEdit.setText('')
        self.passwordEdit.setText('')
        self.conpasswordEdit.setText('')
        self.accessEdit.setCurrentIndex(0)
        self.usernameEdit.setFocus()
                    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
