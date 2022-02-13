from PyQt5 import QtCore, QtGui, QtWidgets
from additional_files import database
from additional_files import option
from mysql.connector import MySQLConnection,Error
#import ctypes

class Ui_MainWindow(object):

    #GUI
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366,768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background: rgb(255, 255, 217);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(450, 10, 415, 41))
        self.label.setStyleSheet("color:rgb(15,73,61);\n"
                                "font-family:century gothic;\n"
                                "font-size:40px;\n"
                                "text-align:center;\n"
                                "background:transparent;")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(430, 120, 451, 371))
        self.frame_2.setStyleSheet("*{\n"
                                    "background:rgb(201,230,202);\n"
                                    "}\n"
                                    "QLineEdit{\n"
                                        "border:1px solid black;\n"
                                        "border-radius:10px;\n"
                                        "padding:10px;\n"
                                        "font-size:15px;\n"
                                        "}\n"
                                        "QLabel{\n"
                                            "font-size:15px;\n"
                                            "font-weight:bold;\n"
                                            "}\n"
                                        "QPushButton#loginButton{\n"
                                            "background:rgb(15,73,61);\n"
                                            "border:1px solid black;\n"
                                            "color:white;\n"
                                            "font-size:15px;\n"
                                            "padding:5px;\n"
                                        "}")

        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 451, 61))
        self.label_2.setStyleSheet("background:rgb(15,73,61);\n"
                                    "color:white;\n"
                                    "font-size:30px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.userEdit = QtWidgets.QLineEdit(self.frame_2)
        self.userEdit.setGeometry(QtCore.QRect(30, 120, 401, 41))
        self.userEdit.setStyleSheet("")
        self.userEdit.setObjectName("userEdit")
        self.passEdit = QtWidgets.QLineEdit(self.frame_2)
        self.passEdit.setGeometry(QtCore.QRect(32, 260, 401, 41))
        self.passEdit.setObjectName("passEdit")
        self.passEdit.setEchoMode(2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 81, 21))
        self.label_4.setObjectName("label_4")
        self.loginButton = QtWidgets.QPushButton(self.frame_2)
        self.loginButton.setGeometry(QtCore.QRect(180, 320, 101, 31))
        self.loginButton.setObjectName("loginButton")
        self.status = QtWidgets.QLabel(self.frame)
        self.status.setGeometry(QtCore.QRect(426, 510, 451, 41))
        self.status.setStyleSheet("color:rgb(15,73,61);\n"
                                "font-size:20px;")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1348, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.MainWindow=MainWindow
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        MainWindow.setWindowIcon(QtGui.QIcon('additional_files/logo.jpg'))
        self.label.setText(_translate("MainWindow", "Welcome to Air India"))
        self.label_2.setText(_translate("MainWindow", "LOGIN"))
        self.label_3.setText(_translate("MainWindow", "Username:"))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.status.setText(_translate("MainWindow", ""))
        self.userEdit.setFocus()

        #click and return events
        self.userEdit.returnPressed.connect(self.passEdit.setFocus)
        self.passEdit.returnPressed.connect(self.loginButton.click)
        self.loginButton.clicked.connect(self.onSubmit)


    #connecting to database
    def onSubmit(self):
        if(self.userEdit.text()!='' and self.userEdit.text()!=''):
            db_obj=database.Database(self.userEdit.text(),self.passEdit.text())
            db_mysql=db_obj.callDatabase()

            if(db_mysql and isinstance(db_mysql,MySQLConnection)):
                self.optionWindow(db_mysql) 

            elif(db_mysql and isinstance(db_mysql,Error)):
                
                if db_mysql.errno==1045:
                    self.status.setText('wrong credentials')

                elif db_mysql.errno == 1049:
                    self.status.setText('database does not exist')
                
                elif db_mysql.errno == 2006:
                    self.status.setText('MySql server has gone')
                
                elif db_mysql.errno == 2002:
                    self.status.setText('Can\'t connect to local MySQL server through socket ')
                
                else:
                    self.status.setText(str(db_mysql))
                
                self.userEdit.setText('')
                self.passEdit.setText('')
                self.userEdit.setFocus()
        
        else:
            self.status.setText('No field can be left empty')
            self.userEdit.setText('')
            self.passEdit.setText('')
            self.userEdit.setFocus()


    #connection to option window 
    def optionWindow(self,db):
        self.window=QtWidgets.QMainWindow()
        self.ui=option.Ui_optionPage(db)
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('additional_files/logo.jpg'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
