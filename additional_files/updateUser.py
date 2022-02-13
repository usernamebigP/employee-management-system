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
"    background:white;\n"
"}\n"
"\n"
"QComboBox{\n"
"background:white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.heading = QtWidgets.QLabel(self.frame)
        self.heading.setGeometry(QtCore.QRect(0, -4, 931, 51))
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 90, 104, 23))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 184, 161, 23))
        self.label_2.setObjectName("label_2")
        self.accessEdit = QtWidgets.QComboBox(self.frame)
        self.accessEdit.setGeometry(QtCore.QRect(200, 180, 261, 27))
        self.accessEdit.setObjectName("accessEdit")
        self.accessEdit.addItem("")
        self.accessEdit.addItem("")
        self.accessEdit.setEditable(True)
        self.usernameEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameEdit.setGeometry(QtCore.QRect(200, 90, 261, 29))
        self.usernameEdit.setObjectName("usernameEdit")
        self.updateUser = QtWidgets.QPushButton(self.frame)
        self.updateUser.setGeometry(QtCore.QRect(200, 270, 85, 31))
        self.updateUser.setStyleSheet("color:white;\n"
"background:rgb(15,73,61)")
        self.updateUser.setObjectName("updateUser")
        self.status = QtWidgets.QLabel(self.frame)
        self.status.setGeometry(QtCore.QRect(5, 362, 931, 31))
        self.status.setStyleSheet("color:white;\n"
"background:rgb(15,73,61)")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heading.setText(_translate("MainWindow", "Update User"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.label_2.setText(_translate("MainWindow", "Change access:"))
        self.accessEdit.setItemText(0, _translate("MainWindow", "read"))
        self.accessEdit.setItemText(1, _translate("MainWindow", "write"))
        self.updateUser.setText(_translate("MainWindow", "Update "))
        self.status.setText(_translate("MainWindow", "Status"))

        #clicking events
        self.usernameEdit.setFocus()
        self.updateUser.clicked.connect(self.updateDetails)

        #actions for return key
        self.usernameEdit.returnPressed.connect(self.accessEdit.setFocus)
        self.accessEdit.lineEdit().returnPressed.connect(self.updateUser.click)


    def updateDetails(self):
        if(self.usernameEdit.text()!=''):
            cur=self.db.cursor()
            cur.execute('select user from mysql.user where user="{}"'.format(self.usernameEdit.text()))
            user=cur.fetchone()

            if user:
                user=user[0]
                #revoking privileges from the current user
                cur.execute('revoke all privileges on *.* from "{}"@"localhost"'.format(user))
                self.db.commit()

                #checking the access type and reassigning the privileges
                if(self.accessEdit.currentText()=="read"):
                    cur.execute('grant select on *.* to "{}"@"localhost"'.format(user))
                    self.db.commit()

                elif(self.accessEdit.currentText()=='write'):
                    cur.execute('grant select,update,insert,delete on *.* to "{}"@"localhost"'.format(user))
                    self.db.commit()
                
                #status GUI
                self.status.show()
                self.status.setStyleSheet('background:rgb(15,73,61);color:white')
                self.status.setText('successfully updated {} with {} access'.format(user,self.accessEdit.currentText()))
                self.clearData()
                self.usernameEdit.setFocus()

            else:
                self.status.show()
                self.status.setStyleSheet('background:rgb(212,115,70)')
                self.status.setText('no user found with name {}!'.format(self.usernameEdit.text()))
                self.usernameEdit.setFocus()
                self.clearData()

        else:
            self.status.show()
            self.status.setStyleSheet('background:rgb(212,115,70);color:white')
            self.status.setText("Enter a username")
            self.usernameEdit.setFocus()

    def clearData(self):
        self.usernameEdit.setText('')
        self.accessEdit.setCurrentIndex(0)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
