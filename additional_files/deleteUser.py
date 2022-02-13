from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import MySQLConnection ,Error

class Ui_MainWindow(object):

    def __init__(self,db):
            self.db=db
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 331)
        MainWindow.setMaximumSize(QtCore.QSize(953, 331))
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
        self.usernameEdit = QtWidgets.QLineEdit(self.frame)
        self.usernameEdit.setGeometry(QtCore.QRect(200, 90, 301, 29))
        self.usernameEdit.setObjectName("usernameEdit")
        self.deleteUser = QtWidgets.QPushButton(self.frame)
        self.deleteUser.setGeometry(QtCore.QRect(200, 160, 85, 31))
        self.deleteUser.setStyleSheet("color:white;\n"
"background:rgb(15,73,61)")
        self.deleteUser.setObjectName("deleteUser")
        self.status = QtWidgets.QLabel(self.frame)
        self.status.setGeometry(QtCore.QRect(5, 362, 931, 31))
        self.status.setStyleSheet("color:white;\n"
"background:rgb(15,73,61)")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.Status = QtWidgets.QLabel(self.frame)
        self.Status.setGeometry(QtCore.QRect(0, 240, 931, 31))
        self.Status.setStyleSheet("color:white;\n"
"background:rgb(15,73,61)")
        self.Status.setAlignment(QtCore.Qt.AlignCenter)
        self.Status.setObjectName("Status")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heading.setText(_translate("MainWindow", "Delete User"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.deleteUser.setText(_translate("MainWindow", "Delete"))
        self.status.setText(_translate("MainWindow", "Status"))
        self.Status.setText(_translate("MainWindow", "Status"))
        self.Status.hide()
        self.usernameEdit.returnPressed.connect(self.onSubmit)

    def onSubmit(self):
        if(self.usernameEdit.text()!=''):
                try:
                        cur=self.db.cursor()
                        cur.execute('select user from mysql.user where user="{}"'.format(self.usernameEdit.text()))
                        user=cur.fetchone()

                        if user:
                                user=user[0]
                                cur.execute('drop user "{}"@"localhost"'.format(user))
                                self.db.commit()

                                #status gui
                                self.Status.show()
                                self.Status.setStyleSheet('background:rgb(15,73,61);color:white;')
                                self.Status.setText('{} deleted successfully!!'.format(user))
                                self.usernameEdit.setText('')
                                
                        else:
                                self.Status.show()
                                self.Status.setStyleSheet('background:rgb(212,115,70)')
                                self.Status.setText('no user found!!')
                                self.usernameEdit.setText('')
                                
                        self.usernameEdit.setFocus()

                except Error as e:
                        self.Status.show()
                        self.Status.setStyleSheet("background:rgb(212,115,70)")
                        self.Status.setText(e)

        else:
                self.Status.show()
                self.Status.setStyleSheet('background:rgb(212,115,70)')
                self.Status.setText("enter a username")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

