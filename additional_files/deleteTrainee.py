from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import Error
from additional_files import utilities as u

class Ui_MainWindow(object):
    def __init__(self,db):
        self.db=db

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 420)
        MainWindow.setMaximumSize(QtCore.QSize(953, 420))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("*{\n"
"background:rgb(255,255,217)\n"
"}\n"
"QPushButton{\n"
"    background:rgb(15,73,61);\n"
"    color:white;\n"
"    font-weight:bold;\n"
"    font-size:20px;\n"
"}\n"
"QLabel{\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.heading = QtWidgets.QLabel(self.frame)
        self.heading.setGeometry(QtCore.QRect(0, 0, 931, 51))
        self.heading.setStyleSheet("background:rgb(15,73,61);\n"
"color:white;\n"
"font-weight:bold;\n"
"font-size:30px;")
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.idEdit = QtWidgets.QLineEdit(self.frame)
        self.idEdit.setGeometry(QtCore.QRect(100, 100, 441, 41))
        self.idEdit.setObjectName("idEdit")
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(26, 102, 71, 41))
        self.id.setObjectName("id")
        self.image = QtWidgets.QLabel(self.frame)
        self.image.setGeometry(QtCore.QRect(730, 100, 131, 161))
        self.image.setText("")
        self.image.setObjectName("image")
        self.deleteButton = QtWidgets.QPushButton(self.frame)
        self.deleteButton.setGeometry(QtCore.QRect(260, 250, 121, 41))
        self.deleteButton.setObjectName("deleteButton")
        self.searchButton = QtWidgets.QPushButton(self.frame)
        self.searchButton.setGeometry(QtCore.QRect(560, 100, 111, 41))
        self.searchButton.setObjectName("searchButton")
        self.status = QtWidgets.QLabel(self.frame)
        self.status.setGeometry(QtCore.QRect(0, 320, 931, 41))
        self.status.setStyleSheet("font-size:15px;\n"
"background:rgb(15,73,61);\n"
"color:white;\n"
"")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 170, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 170, 431, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Delete Employee"))
        self.heading.setText(_translate("MainWindow", "Delete Employee"))
        self.id.setText(_translate("MainWindow", "Id:"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.status.setText(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.currentId=''
        self.status.hide()
        
        #events
        self.idEdit.returnPressed.connect(self.searchButton.click)
        self.searchButton.clicked.connect(self.onSearch)
        self.deleteButton.clicked.connect(self.onDelete)

    def onSearch(self):
        cur=self.db.cursor()

        if(self.idEdit.text()!=''):
            try:
                cur.execute('select eno , name from employee where eno="{}"'.format(self.idEdit.text()))
                trainee=cur.fetchone()
                if(trainee):
                    cur.execute('select photo from employeePhoto where eno="{}"'.format(trainee[0]))
                    photo=cur.fetchone()[0]
                    u.write_file(photo,"temp/deletedTrainee.jpg")
                    self.currentId=trainee[0]

                    #updating status
                    self.status.show()
                    self.status.setStyleSheet('background:rgb(15,73,61)')
                    self.status.setText('One trainee found with the id {}'.format(trainee[0]))

                    #updating image
                    pixmap=QtGui.QPixmap("temp/deletedTrainee.jpg")
                    pixmap=pixmap.scaled(100,200,QtCore.Qt.KeepAspectRatio)
                    self.image.setPixmap(pixmap)
                    self.image.setScaledContents(True)

                    #updating name
                    self.label_2.setText(trainee[1])
                    self.label_2.setStyleSheet('font-size:15px;font-weight:normal')
                    self.idEdit.setText('')

                else:
                    self.status.show()
                    self.status.setStyleSheet('background:rgb(212,115,70);')
                    self.idEdit.setText('')
                    self.status.setText('No Employee found with the id {}'.format(self.idEdit.text()))
                    self.idEdit.setFocus()

            except Error as e:
                self.status.setText(str(e))

        else:
            self.status.show()
            self.status.setStyleSheet("background:rgb(212,115,70)")
            self.status.setText('enter an id first')
            self.idEdit.setFocus()

    def onDelete(self):
        cur=self.db.cursor()      
        if(self.currentId!=''):
            try:
                cur.execute('delete from employee where eno="{}"'.format(self.currentId))
                self.db.commit()
                
                #updating status
                self.status.show()
                self.status.setText('Employee deleted successfully')
                self.status.setStyleSheet('background:rgb(15,73,61)')

                #updating ui
                self.label_2.setText('')
                self.image.setPixmap(QtGui.QPixmap(''))
                self.idEdit.setFocus()
                self.currentId=''

            except Error as e:
                self.status.setText(str(e))

        else:
            self.status.show()
            self.status.setText('Search for a employee first')
            self.status.setStyleSheet('background:rgb(212,115,70)')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

