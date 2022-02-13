from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import MySQLConnection , Error
import sys
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("*{\n"
"background:rgb(255,255,217);\n"
"font-size:15px;\n"
"}\n"
"QPushButton{\n"
"color:white;\n"
"background:rgb(15,73,61);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.actionButton = QtWidgets.QPushButton(self.frame)
        self.actionButton.setGeometry(QtCore.QRect(340, 350, 141, 41))
        self.actionButton.setObjectName("actionButton")
        self.actionButton2 = QtWidgets.QPushButton(self.frame)
        self.actionButton2.setGeometry(QtCore.QRect(340, 351, 141, 41))
        self.actionButton2.setObjectName("actionButton2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 781, 41))
        self.label.setStyleSheet("background:rgb(15,73,61);\n"
"font-size:30px;\n"
"color:white;")
        self.label.setObjectName("label")
        self.username = QtWidgets.QLabel(self.frame)
        self.username.setGeometry(QtCore.QRect(10, 130, 81, 31))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(self.frame)
        self.password.setGeometry(QtCore.QRect(10, 190, 71, 31))
        self.password.setObjectName("password")
        self.usernameEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameEdit.setGeometry(QtCore.QRect(180, 130, 281, 31))
        self.usernameEdit.setObjectName("usernameEdit")
        self.passEdit = QtWidgets.QLineEdit(self.frame)
        self.passEdit.setGeometry(QtCore.QRect(180, 190, 281, 31))
        self.passEdit.setObjectName("passEdit")
        self.passEdit.setEchoMode(2)
        self.status = QtWidgets.QLabel(self.frame)
        self.status.setGeometry(QtCore.QRect(0, 460, 781, 31))
        self.status.setStyleSheet("color:white;\n"
"background:rgb(15,73,61)")
        self.status.setObjectName("status")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 70, 781, 21))
        self.label_5.setStyleSheet("font-size:20px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.confirmPassword = QtWidgets.QLabel(self.frame)
        self.confirmPassword.setGeometry(QtCore.QRect(10, 260, 131, 16))
        self.confirmPassword.setObjectName("confirmPassword")
        self.conpassEdit = QtWidgets.QLineEdit(self.frame)
        self.conpassEdit.setGeometry(QtCore.QRect(180, 250, 281, 31))
        self.conpassEdit.setObjectName("conpassEdit")
        self.conpassEdit.setEchoMode(2)
        self.finishFrame = QtWidgets.QFrame(self.frame)
        self.finishFrame.setGeometry(QtCore.QRect(0, 40, 781, 421))
        self.finishFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.finishFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.finishFrame.setObjectName("finishFrame")
        self.label_2 = QtWidgets.QLabel(self.finishFrame)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 551, 211))
        self.label_2.setStyleSheet("font-size:30px;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actionButton.setText(_translate("MainWindow", "Create Database"))
        self.label.setText(_translate("MainWindow", "Setup Database"))
        self.username.setText(_translate("MainWindow", "Username:"))
        self.password.setText(_translate("MainWindow", "Password:"))
        self.status.setText(_translate("MainWindow", "Status"))
        self.label_5.setText(_translate("MainWindow", "Enter credentials of the root user"))
        self.confirmPassword.setText(_translate("MainWindow", "Confirm Password:"))
        self.label_2.setText(_translate("MainWindow", "Database and Admin successfully created. You can now close the window"))
        self.actionButton2.setText('create user')
        self.actionButton2.hide()
        self.status.hide()
        self.confirmPassword.hide()
        self.conpassEdit.hide()
        self.finishFrame.hide()

        #click events
        self.actionButton.clicked.connect(self.onSubmit)
        self.actionButton2.clicked.connect(self.onCreate)

        #return events
        self.usernameEdit.setFocus()
        self.usernameEdit.returnPressed.connect(self.passEdit.setFocus)
        self.conpassEdit.returnPressed.connect(self.actionButton2.click)

    #creating the database
    def onSubmit(self):
        if(self.usernameEdit.text()!='' and self.passEdit.text()!=''):
            try:
                self.db=MySQLConnection(host="localhost",user=self.usernameEdit.text(),password=self.passEdit.text())
                cur=self.db.cursor()

                with open('setupDatabase.txt','r') as f:
                    for line in f:
                        cur.execute(line)
                
                cur.close()

                #updating status
                self.status.show()
                self.status.setStyleSheet('background:rgb(15,73,61)')
                self.status.setText('airindia database created successfully')
                
                #adding the path of the directory
                path=os.path.dirname(os.getcwd())
                sys.path.append(path)

                #changing view
                self.usernameEdit.setFocus()
                self.usernameEdit.setText('')
                self.passEdit.setText('')
                self.actionButton.hide()
                self.actionButton2.show()
                self.confirmPassword.show()
                self.conpassEdit.show()
                self.label_5.setText('Add the admin')
                self.passEdit.returnPressed.connect(self.conpassEdit.setFocus)

            except Error as e:
                self.status.show()
                self.status.setStyleSheet('background:rgb(212,115,70)')

                if e.errno==1045:
                    self.status.setText("wrong credentials")
                
                elif e.errno==1044:
                    self.status.setText("Access denied to create a database")

                elif e.errno == 2006:
                    self.status.setText('MySql server has gone')
                
                elif e.errno == 2002:
                    self.status.setText('Can\'t connect to local MySQL server through socket ')
                
                else:
                    self.status.setText(str(e))
        
        else:
            self.status.show()
            self.status.setStyleSheet('background:rgb(212,115,70)')
            self.status.setText('No field can be left empty')

    def onCreate(self):
        if(self.usernameEdit.text()!='' and self.passEdit.text()!=''):
            if(self.passEdit.text()==self.conpassEdit.text()):
                try:
                    cur=self.db.cursor()
                    cur.execute('create user "{}"@"localhost" identified by "{}"'.format(self.usernameEdit.text(),self.passEdit.text()))
                    cur.execute('grant all privileges on *.* to "{}"@"localhost" with grant option'.format(self.usernameEdit.text()))

                    #updating status
                    self.status.setStyleSheet('background:rgb(15,73,61)')
                    self.status.setText('admin created successfully')

                    #updating view
                    self.finishFrame.show()
                    cur.close()

                except Error as e:
                    if e.errno == 1396:
                        self.status.setStyleSheet('background:rgb(212,115,70)')
                        self.status.setText("Cannot create admin with this username")

                    else:
                        self.status.setStyleSheet('background:rgb(212,115,70)')
                        self.status.setText(str(e)[20:])
                        
            else:
                self.status.setStyleSheet('background:rgb(212,115,70)')
                self.status.setText('passwords do not match')
   
        else:
            self.status.setStyleSheet('background:rgb(212,115,70)')
            self.status.setText('No fields can be left empty')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

