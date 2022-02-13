from PyQt5 import QtCore, QtGui, QtWidgets
import os

#importing all the windows for option view
from additional_files import addTrainee as Ui_addTrainee #adding trainee window
from additional_files import searchTrainee as Ui_searchTrainee #search trainee window
from additional_files import updateTrainee as Ui_updateTrainee #update trainee window
from additional_files import deleteTrainee as Ui_deleteTrainee #delete trainee window
from additional_files import addUser as Ui_addUser #adding a new user to access database
from additional_files import updateUser as Ui_updateUser #updating the user rights
from additional_files import deleteUser as Ui_deleteUser #deleting the user

import ctypes

class Ui_optionPage(object):
    def __init__(self,db):
        self.db=db

    #GUI
    def setupUi(self, optionPage):
        optionPage.setObjectName("optionPage")
        #optionPage.resize(ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
        optionPage.resize(1366,768)
        self.centralwidget = QtWidgets.QWidget(optionPage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background:rgb(255, 255, 217);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(480, 40, 421, 571))
        self.frame_2.setStyleSheet("*{\n"
"background: rgb(201, 230, 202);\n"
"font-size:15px;\n"
"}\n"
"QPushButton{\n"
"background:transparent;\n"
"border:none;\n"
"color:rgb(9,36,8);\n"
"text-align:left;\n"
"padding:5px;\n"
"}\n"
"QLabel#heading{\n"
"font-size:40px;\n"
"background:rgb(15, 73, 61);\n"
"color:white;\n"
"}\n"
"QLabel{\n"
"color:rgb(65,0,0);\n"
"font-weight:bold;\n"
"}\n"
"QPushButton:focus{\n"
"background:rgb(172,178,144);\n"
"font-weight:500;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.addTrainee = QtWidgets.QPushButton(self.frame_2)
        self.addTrainee.setGeometry(QtCore.QRect(30, 130, 145, 31))
        self.addTrainee.setStyleSheet("")
        self.addTrainee.setObjectName("addTrainee")
        self.addTrainee.setDefault(True)
        self.heading = QtWidgets.QLabel(self.frame_2)
        self.heading.setGeometry(QtCore.QRect(0, 0, 421, 61))
        self.heading.setScaledContents(False)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.manageTrainee = QtWidgets.QLabel(self.frame_2)
        self.manageTrainee.setGeometry(QtCore.QRect(25, 90, 145, 31))
        self.manageTrainee.setObjectName("manageTrainee")
        self.manageUsers = QtWidgets.QLabel(self.frame_2)
        self.manageUsers.setGeometry(QtCore.QRect(20, 320, 111, 21))
        self.manageUsers.setObjectName("manageUsers")
        self.searchTrainee = QtWidgets.QPushButton(self.frame_2)
        self.searchTrainee.setGeometry(QtCore.QRect(30, 170, 145, 31))
        self.searchTrainee.setObjectName("searchTrainee")
        self.searchTrainee.setDefault(True)
        self.updateTrainee = QtWidgets.QPushButton(self.frame_2)
        self.updateTrainee.setGeometry(QtCore.QRect(30, 210, 145, 31))
        self.updateTrainee.setObjectName("updateTrainee")
        self.updateTrainee.setDefault(True)
        self.deleteTrainee = QtWidgets.QPushButton(self.frame_2)
        self.deleteTrainee.setGeometry(QtCore.QRect(30, 250, 145, 31))
        self.deleteTrainee.setObjectName("deleteTrainee")
        self.deleteTrainee.setDefault(True)
        self.addUser = QtWidgets.QPushButton(self.frame_2)
        self.addUser.setGeometry(QtCore.QRect(30, 360, 131, 31))
        self.addUser.setObjectName("addUser")
        self.addUser.setDefault(True)
        self.UpdateUser = QtWidgets.QPushButton(self.frame_2)
        self.UpdateUser.setGeometry(QtCore.QRect(30, 400, 131, 31))
        self.UpdateUser.setObjectName("UpdateUser")
        self.UpdateUser.setDefault(True)
        self.deleteUser = QtWidgets.QPushButton(self.frame_2)
        self.deleteUser.setGeometry(QtCore.QRect(30, 440, 131, 31))
        self.deleteUser.setObjectName("deleteUser")
        self.deleteUser.setDefault(True)
        self.logout = QtWidgets.QPushButton(self.frame_2)
        self.logout.setGeometry(QtCore.QRect(170, 530, 81, 31))
        self.logout.setStyleSheet("text-align:center;\n"
"border:1px solid black;\n"
"background:rgb(15,73,61);\n"
"color:white;")
        self.logout.setObjectName("logout")
        self.logout.setDefault(True)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        optionPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(optionPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        optionPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(optionPage)
        self.statusbar.setObjectName("statusbar")
        optionPage.setStatusBar(self.statusbar)
        self.optionPage=optionPage
        self.retranslateUi(optionPage)
        QtCore.QMetaObject.connectSlotsByName(optionPage)

    def retranslateUi(self, optionPage):
        _translate = QtCore.QCoreApplication.translate
        optionPage.setWindowTitle(_translate("optionPage", "Manage"))
        self.addTrainee.setText(_translate("optionPage", "Add employee"))
        self.heading.setText(_translate("optionPage", "Options"))
        self.manageTrainee.setText(_translate("optionPage", "Manage employees"))
        self.manageUsers.setText(_translate("optionPage", "Manage Users"))
        self.searchTrainee.setText(_translate("optionPage", "Search employee"))
        self.updateTrainee.setText(_translate("optionPage", "Update employee"))
        self.deleteTrainee.setText(_translate("optionPage", "Delete employee"))
        self.addUser.setText(_translate("optionPage", "Add User"))
        self.UpdateUser.setText(_translate("optionPage", "Update User"))
        self.deleteUser.setText(_translate("optionPage", "Delete User"))
        self.logout.setText(_translate("optionPage", "Logout"))

        #checking the user for access 
        self.checkUser()

        #button actions(clicked)
        self.addTrainee.clicked.connect(self.traineeWindow)
        self.searchTrainee.clicked.connect(self.searchTraineeWindow)
        self.updateTrainee.clicked.connect(self.updateTraineeWindow)
        self.deleteTrainee.clicked.connect(self.deleteTraineeWindow)
        self.addUser.clicked.connect(self.addUserWindow)
        self.UpdateUser.clicked.connect(self.updateUserWindow)
        self.deleteUser.clicked.connect(self.deleteUserWindow)
        self.logout.clicked.connect(self.logoutWindow)

    def checkUser(self):
        cur=self.db.cursor()
        cur.execute('show grants')
        grants=cur.fetchall()[0][0]
        #console.log(grants)

        if not "GRANT OPTION" in grants:
            self.addUser.hide()
            self.UpdateUser.hide()
            self.deleteUser.hide()
            self.manageUsers.hide()

        writeGrants=["ALL PRIVILEGES"]

        for grant in writeGrants:
            if not grant in grants:
                self.addTrainee.hide()
                self.updateTrainee.hide()
                self.deleteTrainee.hide()
                self.searchTrainee.setGeometry(QtCore.QRect(30, 130, 140, 31))
                break
            
            else:
                continue


    #add trainee window
    def traineeWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_addTrainee.Ui_MainWindow(self.db)
        self.ui.setupUi(self.window)
        self.window.show()

    #search trainee
    def searchTraineeWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_searchTrainee.Ui_MainWindow(self.db)
        self.ui.setupUi(self.window)
        self.window.show()

    #update trainee
    def updateTraineeWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_updateTrainee.Ui_MainWindow(self.db)
        self.ui.setupUi(self.window)
        self.window.show()
    
    #delete trainee
    def deleteTraineeWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_deleteTrainee.Ui_MainWindow(self.db)
        self.ui.setupUi(self.window)
        self.window.show()

    #add user for the database window
    def addUserWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_addUser.Ui_MainWindow(self.db)
        self.ui.setupUi(self.window)
        self.window.show()
    
    #update user for the database window
    def updateUserWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_updateUser.Ui_MainWindow(self.db)
        self.ui.setupUi(self.window)
        self.window.show()
    
    #delete user for the database
    def deleteUserWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_deleteUser.Ui_MainWindow(self.db)
        self.ui.setupUi(self.window)
        self.window.show()

    def logoutWindow(self):
        # os.chdir('temp')
        # for file in os.listdir():
        #     os.remove(file)
        from Login import Ui_MainWindow as adminWindow 
        self.db.close()
        self.window=QtWidgets.QMainWindow()
        self.ui=adminWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.optionPage.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    optionPage = QtWidgets.QMainWindow()
    ui=Ui_optionPage()
    ui.setupUi(optionPage)
    optionPage.show()
    sys.exit(app.exec_())
