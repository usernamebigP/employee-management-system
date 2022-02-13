from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import MySQLConnection,Error
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from datetime import datetime
from mysql.connector import Error
import ctypes
from additional_files import utilities as u
 
class Ui_MainWindow(object):
    def __init__(self,db):
        self.db=db
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        #MainWindow.resize(ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
        MainWindow.resize(1366,768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 1349, 702))
        self.frame.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 217);\n"
"font-family:century gothic;\n"
"font-size:15px;\n"
"}\n"
"QPushButton{\n"
"background:white;\n"
"border:1px solid black;\n"
"border-style:inset;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style:outset;\n"
"    border:2px solid black;\n"
"}\n"
"    ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(10, 30, 41, 31))
        self.id.setStyleSheet("font-weight:bold")
        self.id.setObjectName("id")
        self.idEdit = QtWidgets.QLineEdit(self.frame)
        self.idEdit.setGeometry(QtCore.QRect(60, 30, 501, 31))
        self.idEdit.setStyleSheet("background:white;")
        self.idEdit.setObjectName("idEdit")
        self.search = QtWidgets.QPushButton(self.frame)
        self.search.setGeometry(QtCore.QRect(570, 30, 111, 31))
        self.search.setStyleSheet("background:rgb(15,73,61);\n"
"color:white;")
        self.search.setObjectName("search")
        self.traineeDetails = QtWidgets.QFrame(self.frame)
        self.traineeDetails.setGeometry(QtCore.QRect(90, 90, 1121, 531))
        self.traineeDetails.setStyleSheet("*{\n"
"background-color: rgb(201, 230,202 );\n"
"font-family:century gothic;\n"
"font-size:15px;\n"
"}\n"
"QLineEdit{\n"
"background:white;\n"
"}\n"
"QGroupBox{\n"
"border:1px solid black;\n"
"}")
        self.traineeDetails.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.traineeDetails.setFrameShadow(QtWidgets.QFrame.Raised)
        self.traineeDetails.setObjectName("traineeDetails")
        self.Name = QtWidgets.QLabel(self.traineeDetails)
        self.Name.setGeometry(QtCore.QRect(30, 120, 71, 41))
        self.Name.setStyleSheet("font-weight:bold;")
        self.Name.setObjectName("Name")
        self.idLabel = QtWidgets.QLabel(self.traineeDetails)
        self.idLabel.setGeometry(QtCore.QRect(30, 80, 51, 31))
        self.idLabel.setStyleSheet("font-weight:bold;")
        self.idLabel.setObjectName("idLabel")
        self.imageText = QtWidgets.QLabel(self.traineeDetails)
        self.imageText.setGeometry(QtCore.QRect(890, 70, 161, 171))
        self.imageText.setStyleSheet("border:1px solid black;\n"
"background:rgb(191, 191, 191);\n"
"border-style:dotted;")
        self.imageText.setText("")
        self.imageText.setObjectName("imageText")
        self.sigText = QtWidgets.QLabel(self.traineeDetails)
        self.sigText.setGeometry(QtCore.QRect(890, 470, 171, 51))
        self.sigText.setStyleSheet("border:1px solid black;\n"
"background:rgb(189, 189, 189);\n"
"border-style:dotted;")
        self.sigText.setText("")
        self.sigText.setObjectName("sigText")
        self.label = QtWidgets.QLabel(self.traineeDetails)
        self.label.setGeometry(QtCore.QRect(30, 300, 81, 16))
        self.label.setStyleSheet("font-weight:bold;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.traineeDetails)
        self.label_3.setGeometry(QtCore.QRect(30, 360, 91, 21))
        self.label_3.setStyleSheet("font-weight:bold;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.traineeDetails)
        self.label_4.setGeometry(QtCore.QRect(30, 430, 121, 16))
        self.label_4.setStyleSheet("font-weight:bold;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.traineeDetails)
        self.label_5.setGeometry(QtCore.QRect(30, 490, 101, 16))
        self.label_5.setStyleSheet("font-weight:bold;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.traineeDetails)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 1121, 51))
        self.label_6.setStyleSheet("font-size:40px;\n"
"background:rgb(15,73,61);\n"
"color:white;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.dob = QtWidgets.QLabel(self.traineeDetails)
        self.dob.setGeometry(QtCore.QRect(30, 180, 101, 21))
        self.dob.setStyleSheet("font-weight:bold;")
        self.dob.setObjectName("dob")
        self.doj = QtWidgets.QLabel(self.traineeDetails)
        self.doj.setGeometry(QtCore.QRect(30, 240, 121, 20))
        self.doj.setStyleSheet("font-weight:bold;")
        self.doj.setObjectName("doj")
        self.idText = QtWidgets.QLabel(self.traineeDetails)
        self.idText.setGeometry(QtCore.QRect(210, 80, 241, 31))
        self.idText.setText("")
        self.idText.setObjectName("idText")
        self.nameText = QtWidgets.QLabel(self.traineeDetails)
        self.nameText.setGeometry(QtCore.QRect(210, 120, 251, 41))
        self.nameText.setText("")
        self.nameText.setObjectName("nameText")
        self.dobText = QtWidgets.QLabel(self.traineeDetails)
        self.dobText.setGeometry(QtCore.QRect(210, 180, 241, 21))
        self.dobText.setText("")
        self.dobText.setObjectName("dobText")
        self.dojText = QtWidgets.QLabel(self.traineeDetails)
        self.dojText.setGeometry(QtCore.QRect(210, 240, 261, 21))
        self.dojText.setText("")
        self.dojText.setObjectName("dojText")
        self.address1Text = QtWidgets.QLabel(self.traineeDetails)
        self.address1Text.setGeometry(QtCore.QRect(210, 290, 711, 41))
        self.address1Text.setText("")
        self.address1Text.setWordWrap(True)
        self.address1Text.setObjectName("address1Text")
        self.address2Text = QtWidgets.QLabel(self.traineeDetails)
        self.address2Text.setGeometry(QtCore.QRect(210, 350, 711, 41))
        self.address2Text.setText("")
        self.address2Text.setWordWrap(True)
        self.address2Text.setObjectName("address2Text")
        self.phone1Text = QtWidgets.QLabel(self.traineeDetails)
        self.phone1Text.setGeometry(QtCore.QRect(210, 423, 121, 31))
        self.phone1Text.setText("")
        self.phone1Text.setObjectName("phone1Text")
        self.phone2Text = QtWidgets.QLabel(self.traineeDetails)
        self.phone2Text.setGeometry(QtCore.QRect(360, 420, 111, 41))
        self.phone2Text.setText("")
        self.phone2Text.setObjectName("phone2Text")
        self.phone3Text = QtWidgets.QLabel(self.traineeDetails)
        self.phone3Text.setGeometry(QtCore.QRect(506, 423, 101, 31))
        self.phone3Text.setText("")
        self.phone3Text.setObjectName("phone3Text")
        self.departmentText = QtWidgets.QLabel(self.traineeDetails)
        self.departmentText.setGeometry(QtCore.QRect(210, 490, 381, 21))
        self.departmentText.setText("")
        self.departmentText.setObjectName("departmentText")
        self.dateEdit = QtWidgets.QLabel(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(1332, 161, 16, 21))
        self.dateEdit.setText("")
        self.dateEdit.setObjectName("dateEdit")
        self.dojEdit = QtWidgets.QLabel(self.frame)
        self.dojEdit.setGeometry(QtCore.QRect(1332, 281, 16, 21))
        self.dojEdit.setText("")
        self.dojEdit.setObjectName("dojEdit")
        self.Status = QtWidgets.QLabel(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(10, 650, 1331, 31))
        self.Status.setStyleSheet("background:rgb(212, 115, 70);\n"
"color:black;\n"
"padding-left:10px;\n"
"font-weight:bold;")
        self.Status.setObjectName("Status")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Search Employee"))
        self.id.setText(_translate("MainWindow", "Id:"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.Name.setText(_translate("MainWindow", "Name:"))
        self.idLabel.setText(_translate("MainWindow", "ID :"))
        self.label.setText(_translate("MainWindow", "Address 1:"))
        self.label_3.setText(_translate("MainWindow", "Address 2:"))
        self.label_4.setText(_translate("MainWindow", "Phone Numbers :"))
        self.label_5.setText(_translate("MainWindow", "Department:"))
        self.label_6.setText(_translate("MainWindow", "Details"))
        self.dob.setText(_translate("MainWindow", "Date of Birth:"))
        self.doj.setText(_translate("MainWindow", "Date of Joining:"))
        self.Status.setText(_translate("MainWindow", "Not a valid id"))

        
        #id flag for validation
        self.idFlag=False
    
        #validation
        self.idEdit.textChanged.connect(self.validation_id)

        #automating searching on pressing enter
        self.idEdit.returnPressed.connect(self.search.click)
        self.search.clicked.connect(self.onSearch)

        #initial settings
        self.shouldSubmit=False
        self.Status.hide()

    #checking before submission
    def onSearch(self):
        if(self.idFlag==True):
            self.shouldSubmit=True
        else:
            self.shouldSubmit=False

        self.connectDatabase()

    #connecting to database
    def connectDatabase(self):
        if(self.shouldSubmit==True):
            cur=self.db.cursor()

            #getting the trainee id before executing other queries
            cur.execute('select eno from employee where eno={}'.format(self.idEdit.text()))
            id=cur.fetchone()

            if(id):
            #queries
                id=id[0] #extracting id from tuple
                employeeQuery="select name , dob, doj from employee where eno = %s "
                employeeAddress="select address from employeeAddress where eno= %s"
                employeeTelephone="select telephone from employeeTelephone where eno= %s"
                employeeDepartment="select department from employeeDepartment where eno= %s"
                employeePhoto ='select photo from employeePhoto where eno = %s'
                employeeSig='select signature from employeeSig where eno = %s'

                #execution
                try:
                    cur.execute(employeeQuery,(id,)) #employeeTable
                    row1=cur.fetchone()

                    cur.execute(employeeAddress,(id,)) #address table
                    row2=cur.fetchall()

                    cur.execute(employeeTelephone,(id,)) #telephone table
                    row3=cur.fetchall()

                    cur.execute(employeeDepartment,(id,)) #department table
                    row4=cur.fetchone()

                    cur.execute(employeePhoto,(id,)) #photo table
                    photo=cur.fetchone()[0]

                    cur.execute(employeeSig,(id,))  #signature table
                    sig=cur.fetchone()[0]

                    
                    #putting data in trainee Details

                    #Name
                    date=row1[1].strftime("%d %b %Y") #formatting date of birth
                    doj=row1[2].strftime("%d %b %Y")  #formatting date of joining
                    
                    self.idText.setText(str(id))     #setting id
                    self.nameText.setText(row1[0])   #setting name
                    self.dobText.setText(date)       #setting date of birth
                    self.dojText.setText(doj)        #setting date of joining

                    #address
                    self.address1Text.setText((row2[0])[0]) #setting address1 

                        #if more than one address is present
                    if(len(row2)>1):
                        self.address2Text.setText((row2[1])[0]) #setting address2
                    else:
                        self.address2Text.setText('Not Available')


                    #phone
                    self.phone1Text.setText(str((row3[0])[0])) #setting phone1

                        #if 2nd phone number is present
                    if(len(row3)>1):
                        self.phone2Text.setText(str((row3[1])[0]))
                    else:
                        self.phone2Text.setText('Not Available')
                    
                        #if 3rd phone number is present
                    if(len(row3)>2):
                        self.phone3Text.setText(str((row3[2])[0]))
                    else:
                        self.phone3Text.setText('Not Available')
                    
                    
                    #setting department
                    self.departmentText.setText(row4[0])

                    #setting photo temporarily
                    u.write_file(photo,"temp/searchPhoto.jpg")

                    #setting signature temporarily
                    u.write_file(sig,"temp/searchSig.jpg")


                    #setting photo in gui
                    pixmap=QtGui.QPixmap("temp/searchPhoto.jpg")
                    pixmap=pixmap.scaled(100,200,QtCore.Qt.KeepAspectRatio)
                    self.imageText.setPixmap(pixmap)
                    self.imageText.setScaledContents(True)

                    #setting signature in gui
                    pixmap=QtGui.QPixmap("temp/searchSig.jpg")
                    pixmap=pixmap.scaled(100,200,QtCore.Qt.KeepAspectRatio)
                    self.sigText.setPixmap(pixmap)
                    self.sigText.setScaledContents(True)

                    #status GUI
                    self.Status.show()
                    self.Status.setStyleSheet("background:rgb(15,73,61);color:white;")
                    self.Status.setText('Found a Employee')
                    self.idEdit.setText('')
                    self.idEdit.setStyleSheet('background:rgb(255,255,217')

                except Error as e:
                    self.Status.setStyleSheet('background:rgb(212,115,70)')
                    if e.errno==1146:
                        self.Status.setText('Problem with the Database (table does not exist)')
                    elif e.errno==1054:
                        self.Status.setText('Problem with the Database (column does not exist)')

            else:
                self.Status.show()
                self.Status.setStyleSheet("background:rgb(212,115,70);color:black;")
                self.Status.setText('No employee with this ID!!')
                self.clearData()

        else:
            self.Status.show()
            self.Status.setStyleSheet("background:rgb(212,115,70);color:black;")
            self.Status.setText("Not a valid id!!")

    def clearData(self):
        self.nameText.setText('')
        self.idText.setText('')
        self.dobText.setText('')
        self.dojText.setText('')
        self.address1Text.setText('')
        self.address2Text.setText('')
        self.phone1Text.setText('')
        self.phone2Text.setText('')
        self.phone3Text.setText('')
        self.departmentText.setText('')
        self.imageText.setPixmap(QtGui.QPixmap(""))
        self.sigText.setPixmap(QtGui.QPixmap(""))

    #validation for id
    def validation_id(self):
        regName=QRegExp("\d{1,9}")
        input_validator = QRegExpValidator(regName, self.idEdit)
        result=input_validator.validate(self.idEdit.text(),0)
        self.idEdit.setValidator(input_validator)
        if(result[0]==2):
            self.idEdit.setStyleSheet("background:rgb(255,255,217)")
            self.idFlag=True
        else:
            self.idEdit.setStyleSheet('background:rgb(212, 115, 70)')
            self.idFlag=False



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
