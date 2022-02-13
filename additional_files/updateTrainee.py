from PyQt5 import QtCore, QtGui, QtWidgets
from mysql.connector import MySQLConnection, Error
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from datetime import datetime,timedelta
import ctypes
from additional_files import utilities

class Ui_MainWindow(QtWidgets.QFileDialog):

    def __init__(self,db):
        super().__init__()
        self.db=db
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
        MainWindow.resize(1366,768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 1348, 671))
        self.frame.setStyleSheet("*{\n"
"background-color: rgb(255, 255, 217);\n"
"font-family:century gothic;\n"
"font-size:15px;\n"
"}\n"
"\n"
"\n"
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
        self.traineeDetails.setGeometry(QtCore.QRect(90, 70, 1121, 561))
        self.traineeDetails.setStyleSheet("*{\n"
"background-color: rgb(201, 230,202 );\n"
"font-family:century gothic;\n"
"font-size:15px;\n"
"}\n"
"QLineEdit{\n"
"background:white;\n"
"}\n"
"QComboBox{\n"
"border:1px solid black;\n"
"}"
"QPushButton#update:pressed{\n"
"font-size:20px;\n"
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
        self.imageText.setGeometry(QtCore.QRect(920, 70, 161, 171))
        self.imageText.setStyleSheet("border:1px solid black;\n"
"background:rgb(191, 191, 191);\n"
"border-style:dotted;")
        self.imageText.setText("")
        self.imageText.setObjectName("imageText")
        self.sigText = QtWidgets.QLabel(self.traineeDetails)
        self.sigText.setGeometry(QtCore.QRect(920, 470, 171, 51))
        self.sigText.setStyleSheet("border:1px solid black;\n"
"background:rgb(189, 189, 189);\n"
"border-style:dotted;")
        self.sigText.setText("")
        self.sigText.setObjectName("sigText")
        self.label = QtWidgets.QLabel(self.traineeDetails)
        self.label.setGeometry(QtCore.QRect(30, 210, 81, 16))
        self.label.setStyleSheet("font-weight:bold;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.traineeDetails)
        self.label_3.setGeometry(QtCore.QRect(30, 330, 91, 21))
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
        self.dob.setGeometry(QtCore.QRect(590, 80, 101, 21))
        self.dob.setStyleSheet("font-weight:bold;")
        self.dob.setObjectName("dob")
        self.doj = QtWidgets.QLabel(self.traineeDetails)
        self.doj.setGeometry(QtCore.QRect(590, 130, 121, 20))
        self.doj.setStyleSheet("font-weight:bold;")
        self.doj.setObjectName("doj")
        self.idEdit_2 = QtWidgets.QLineEdit(self.traineeDetails)
        self.idEdit_2.setEnabled(False)
        self.idEdit_2.setGeometry(QtCore.QRect(160, 80, 361, 31))
        self.idEdit_2.setObjectName("idEdit_2")
        self.nameEdit = QtWidgets.QLineEdit(self.traineeDetails)
        self.nameEdit.setGeometry(QtCore.QRect(160, 130, 361, 31))
        self.nameEdit.setObjectName("nameEdit")
        self.dobEdit = QtWidgets.QDateEdit(self.traineeDetails)
        self.dobEdit.setGeometry(QtCore.QRect(710, 80, 110, 22))
        self.dobEdit.setObjectName("dobEdit")
        self.dobEdit.setMinimumDate(datetime.today()-timedelta(365*60))
        self.dobEdit.setMaximumDate(datetime.today()-timedelta(365*20))
        self.dojEdit = QtWidgets.QDateEdit(self.traineeDetails)
        self.dojEdit.setGeometry(QtCore.QRect(710, 130, 110, 22))
        self.dojEdit.setObjectName("dojEdit")
        self.dojEdit.setMinimumDate(datetime(1932,10,15))
        self.dojEdit.setMaximumDate(datetime.today())
        self.address1Edit = QtWidgets.QLineEdit(self.traineeDetails)
        self.address1Edit.setGeometry(QtCore.QRect(160, 190, 591, 81))
        self.address1Edit.setObjectName("address1Edit")
        self.address2Edit = QtWidgets.QLineEdit(self.traineeDetails)
        self.address2Edit.setGeometry(QtCore.QRect(160, 310, 591, 71))
        self.address2Edit.setObjectName("address2Edit")
        self.phone1Edit = QtWidgets.QLineEdit(self.traineeDetails)
        self.phone1Edit.setGeometry(QtCore.QRect(160, 420, 121, 31))
        self.phone1Edit.setObjectName("phone1Edit")
        self.phone2Edit = QtWidgets.QLineEdit(self.traineeDetails)
        self.phone2Edit.setGeometry(QtCore.QRect(300, 420, 121, 31))
        self.phone2Edit.setObjectName("phone2Edit")
        self.phone3Edit = QtWidgets.QLineEdit(self.traineeDetails)
        self.phone3Edit.setGeometry(QtCore.QRect(440, 420, 121, 31))
        self.phone3Edit.setObjectName("phone3Edit")
        self.departmentEdit = QtWidgets.QComboBox(self.traineeDetails)
        self.departmentEdit.setGeometry(QtCore.QRect(160, 491, 271, 21))
        self.departmentEdit.setObjectName("departmentEdit")
        self.departmentEdit.addItem("")
        self.departmentEdit.addItem("")
        self.departmentEdit.addItem("")
        self.departmentEdit.addItem("")
        self.imageButton = QtWidgets.QPushButton(self.traineeDetails)
        self.imageButton.setGeometry(QtCore.QRect(940, 260, 111, 23))
        self.imageButton.setStyleSheet("background:rgb(15,73,61);\n"
"color:white;\n"
"font-weight:bold;\n"
"")
        self.imageButton.setObjectName("imageButton")
        self.sigButton = QtWidgets.QPushButton(self.traineeDetails)
        self.sigButton.setGeometry(QtCore.QRect(934, 440, 141, 23))
        self.sigButton.setStyleSheet("background:rgb(15,73,61);\n"
"color:white;\n"
"font-weight:bold;\n"
"")
        self.sigButton.setObjectName("sigButton")
        self.update = QtWidgets.QPushButton(self.traineeDetails)
        self.update.setGeometry(QtCore.QRect(514, 522, 101, 31))
        self.update.setStyleSheet("background:rgb(15,73,61);\n"
"color:white;\n"
"font-weight:bold;\n"
"")
        self.update.setObjectName("update")
        self.Status = QtWidgets.QLabel(self.frame)
        self.Status.setGeometry(QtCore.QRect(0, 640, 1331, 31))
        self.Status.setStyleSheet("background:rgb(212, 115, 70);\n"
"color:black;\n"
"padding-left:10px;\n"
"font-weight:bold;")
        self.Status.setObjectName("Status")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Update Employee Information"))
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
        self.dobEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.dojEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.departmentEdit.setItemText(0, _translate('MainWindow',"Select Department"))
        self.departmentEdit.setItemText(1, _translate("MainWindow", "Information Technology"))
        self.departmentEdit.setItemText(2, _translate("MainWindow", "Mechanical Department"))
        self.departmentEdit.setItemText(3, _translate("MainWindow", "Electrical Department"))
        self.departmentEdit.setEditable(True)
        self.imageButton.setText(_translate("MainWindow", "change image"))
        self.sigButton.setText(_translate("MainWindow", "change signature"))
        self.update.setText(_translate("MainWindow", "Update"))
        self.Status.setText(_translate("MainWindow", "Not a valid id"))
        self.search.setEnabled(False)
        self.Status.hide()
        self.shouldSubmit=False
        self.toggleEnable(False)
        #self.db=MySQLConnection(host="localhost",user='root',password="prateek@2103",database="airindia")

        #flags
        self.idFlag=False
        self.flags={
            "name":True,
            "address1":True,  
            "address2":True,   
            "phone1":True,    
            "phone2":True,     
            "phone3":True,     
            "department":True,  
            "image":True,
            "sig":True
        }

        #events
        self.idEdit.returnPressed.connect(self.search.click)
        self.search.clicked.connect(self.onSearch)
        self.imageButton.clicked.connect(self.fileExplorer)
        self.sigButton.clicked.connect(self.fileExplorerSig)
        self.update.clicked.connect(self.onUpdate)

        #validation
        self.idEdit.textChanged.connect(self.validation_id)
        self.nameEdit.editingFinished.connect(self.validation_name)
        self.nameEdit.textChanged.connect(self.validation_name)
        self.phone1Edit.editingFinished.connect(self.validation_phone1)
        self.phone1Edit.textChanged.connect(self.validation_phone1)
        self.phone2Edit.editingFinished.connect(self.validation_phone2)
        self.phone2Edit.textChanged.connect(self.validation_phone2)
        self.phone3Edit.editingFinished.connect(self.validation_phone3)
        self.phone3Edit.textChanged.connect(self.validation_phone3)
        self.address1Edit.editingFinished.connect(self.validation_address1)
        self.address1Edit.textChanged.connect(self.validation_address1)
        self.address2Edit.editingFinished.connect(self.validation_address2)
        self.address2Edit.textChanged.connect(self.validation_address2)
        self.departmentEdit.lineEdit().textChanged.connect(self.validation_department)

        #going to new entry on pressing enter
        self.nameEdit.returnPressed.connect(self.dobEdit.setFocus)
        self.dobEdit.editingFinished.connect(self.dojEdit.setFocus)
        self.dojEdit.editingFinished.connect(self.address1Edit.setFocus)
        self.address1Edit.returnPressed.connect(self.address2Edit.setFocus)
        self.address2Edit.returnPressed.connect(self.phone1Edit.setFocus)
        self.phone1Edit.returnPressed.connect(self.phone2Edit.setFocus)
        self.phone2Edit.returnPressed.connect(self.phone3Edit.setFocus)
        self.phone3Edit.returnPressed.connect(self.imageButton.click)
        self.departmentEdit.lineEdit().returnPressed.connect(self.update.click)

    def onSearch(self):
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
                self.idEdit_2.setText(str(id))      #setting id
                self.nameEdit.setText(row1[0])      #setting name
                self.dobEdit.setDate(row1[1])       #setting date of birth
                self.dojEdit.setDate(row1[2])       #setting date of joining

                #address
                self.address1Edit.setText((row2[0])[0]) #setting address1 

                    #if more than one address is present
                if(len(row2)>1):
                    self.address2Edit.setText((row2[1])[0]) #setting address2
                else:
                    self.address2Edit.setText('')


                #phone
                self.phone1Edit.setText(str((row3[0])[0])) #setting phone1

                    #if 2nd phone number is present
                if(len(row3)>1):
                    self.phone2Edit.setText(str((row3[1])[0]))
                else:
                    self.phone2Edit.setText('')
                
                    #if 3rd phone number is present
                if(len(row3)>2):
                    self.phone3Edit.setText(str((row3[2])[0]))
                else:
                    self.phone3Edit.setText('')
                
               
                #setting department
                self.departmentEdit.setCurrentText(row4[0])

                #setting photo temporarily
                utilities.write_file(photo,"temp/UpdatePhoto.jpg")

                #setting signature temporarily
                utilities.write_file(sig,"temp/UpdateSig.jpg")

                self.photo=photo
                self.sig=sig

                #setting photo in gui
                pixmap=QtGui.QPixmap("temp/UpdatePhoto.jpg")
                pixmap=pixmap.scaled(100,200,QtCore.Qt.KeepAspectRatio)
                self.imageText.setPixmap(pixmap)
                self.imageText.setScaledContents(True)

                #setting signature in gui
                pixmap=QtGui.QPixmap("temp/UpdateSig.jpg")
                pixmap=pixmap.scaled(100,200,QtCore.Qt.KeepAspectRatio)
                self.sigText.setPixmap(pixmap)
                self.sigText.setScaledContents(True)

                #status GUI
                self.Status.show()
                self.Status.setStyleSheet("background:rgb(15,73,61);color:white;")
                self.Status.setText('Found a employee')
                self.idEdit.setText('')
                self.idEdit.setStyleSheet('background:rgb(255,255,217')
                self.search.setEnabled(False)
                self.toggleEnable(True)


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
            self.search.setEnabled(False)
            self.clearData()
            self.toggleEnable(False)
    
    def onUpdate(self):
        if self.photo!='':
            self.flags['image']=True
        else:
            self.flags['image']=False

        if self.sig!='':
            self.flags['sig']=True   
        else:
            self.flags['sig']=False

        for flag in self.flags:
            if(self.flags[flag]==False):
                self.shouldSubmit=False
                break
            else:
                self.shouldSubmit=True
                continue

        if(self.shouldSubmit):
            confirmBox = QtWidgets.QMessageBox.question(self, 'Update details', "Are you sure you want to update?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            if(confirmBox==QtWidgets.QMessageBox.Yes):
                self.updateDetails()

            elif(confirmBox==QtWidgets.QMessageBox.No):
                self.departmentEdit.lineEdit().setFocus()
        else:
            self.Status.setText('Form is incomplete')
            self.Status.setStyleSheet('background:rgb(212,115,70)')

    def updateDetails(self):
        cur=self.db.cursor()

        #saving all the texts in small words for ease
        info={
                "id":int(self.idEdit_2.text()),
                "name":self.nameEdit.text(),
                "dob":str(self.dobEdit.text()),
                "doj":str(self.dojEdit.text()),
                "address":[self.address1Edit.text(),self.address2Edit.text()],
                "phone":[self.phone1Edit.text(),self.phone2Edit.text(),self.phone3Edit.text()],
                "department":str(self.departmentEdit.currentText()),
                "photo":self.photo,
                "sig":self.sig
                }

        #queries for updating data
        employeeQuery="update employee set dob = %s, name= %s , doj = %s where eno = %s"
        employeeAddressQuery="insert into employeeAddress values (%s,%s);"
        employeeTelephoneQuery="insert into employeeTelephone values (%s,%s);"
        employeePhotoquery = "update employeePhoto set photo = %s where eno = %s;"
        employeeSigquery = "update employeeSig set signature= %s where eno= %s;"
        employeeDepartmentQuery="update employeeDepartment set department =%s where eno=%s;"


        #inserting data
        
        #adding name, date of birth , date of joining
        try:
            cur.execute(employeeQuery,(info['dob'],info['name'],info['doj'],info['id']))
            self.db.commit()

            #adding addresses 
            cur.execute("delete from employeeAddress where eno=%s",(info['id'],))
            self.db.commit()

            for addr in info['address']:
                if(addr!=''):
                    cur.execute(employeeAddressQuery,(info['id'],addr))
                    self.db.commit()

            #adding phone numbers
            cur.execute('delete from employeeTelephone where eno = %s',(info['id'],))
            for num in info['phone']:
                if(num!=''):
                    cur.execute(employeeTelephoneQuery,(info['id'],int(num)))
                    self.db.commit()

            #adding department
            cur.execute(employeeDepartmentQuery,(info['department'],info['id']))
            self.db.commit()

            #adding photo
            cur.execute(employeePhotoquery,(info['photo'],info['id']))
            self.db.commit()

            #adding signature
            cur.execute(employeeSigquery,(info['sig'],info['id']))
            self.db.commit()

            #GUI
            self.Status.setStyleSheet(
            "background:rgb(15, 73, 61);\n"
            "color:white;\n"
            "padding:5px;\n"
            "font-size:12px;\n"
            "font-weight:bold")
        
            self.Status.setText("Employee Information updated successfully")
            self.clearData()

        except Error as e:
            self.Status.setStyleSheet('background:rgb(212,115,70)')

            if e.errno==1146:
                self.Status.setText('Problem with the Database (table does not exist)')

            elif e.errno==1054:
                self.Status.setText('Problem with the Database (column does not exist)')
            else:
                self.Status.setText(str(e))


    #adding image
    def fileExplorer(self):
        name=QtWidgets.QFileDialog.getOpenFileName(self,'Open file','c\\','Image files (*.jpg *.png *.jpeg)')
        if name[0]!='':
            imagePath=name[0]
            self.photo=utilities.read_file(imagePath)
            
            #GUI
            pixmap=QtGui.QPixmap(imagePath)
            pixmap=pixmap.scaled(100,200,QtCore.Qt.KeepAspectRatio)
            self.imageText.setPixmap(pixmap)
            self.imageText.setScaledContents(True)

    #adding signature
    def fileExplorerSig(self):
        name=QtWidgets.QFileDialog.getOpenFileName(self,'Open file','c\\','Image files (*.jpg)')
        if name[0]!='':
            imagePath=name[0]
            self.sig=utilities.read_file(imagePath)
            
            #GUI
            pixmap=QtGui.QPixmap(imagePath)
            pixmap=pixmap.scaled(200, 100, QtCore.Qt.KeepAspectRatio)
            self.sigText.setPixmap(pixmap)
            self.sigText.setScaledContents(True)
            self.departmentEdit.setFocus()


    def toggleEnable(self,condition):
        self.traineeDetails.setEnabled(condition)

    def clearData(self):
        style='background:rgb(255,255,217)'
        self.idEdit.setText('')
        self.idEdit_2.setText('')
        self.nameEdit.setText('')
        self.nameEdit.setStyleSheet(style)
        self.dobEdit.setDate(datetime.today()-timedelta(365*19))
        self.dojEdit.setDate(datetime.today())
        self.address1Edit.setText('')
        self.address1Edit.setStyleSheet(style)
        self.address2Edit.setText('')
        self.phone1Edit.setText('')
        self.phone1Edit.setStyleSheet(style)
        self.phone2Edit.setText('')
        self.phone3Edit.setText('')
        self.departmentEdit.setCurrentIndex(0)
        self.departmentEdit.setStyleSheet(style)
        self.imageText.setPixmap(QtGui.QPixmap(''))
        self.sigText.setPixmap(QtGui.QPixmap(''))


    def validation_id(self):
        regName=QRegExp("\d{8,9}")
        input_validator = QRegExpValidator(regName, self.idEdit)
        result=input_validator.validate(self.idEdit.text(),0)
        self.idEdit.setValidator(input_validator)
        if(result[0]==2):
            self.idEdit.setStyleSheet("background:rgb(255,255,217)")
            self.search.setEnabled(True)
        else:
            self.idEdit.setStyleSheet('background:rgb(212, 115, 70)')
            self.search.setEnabled(False)

    #setting up color for onchange validation
    def validation_color(self,result,name):
        if(result[0]==2): 
            name.setStyleSheet("background:rgb(255, 255, 217)")
        else:
            name.setStyleSheet('background:rgb(212, 115, 70)')


    #validation for name
    def validation_name(self):
        regName=QRegExp("[\w\s]{3,}")
        input_validator = QRegExpValidator(regName, self.nameEdit)
        result=input_validator.validate(self.nameEdit.text(),0)
        self.nameEdit.setValidator(input_validator)
        self.validation_color(result,self.nameEdit)
        if(result[0]==2):
            self.flags['name']=True
        else:
            self.flags['name']=False


    #validation for addresses
    def validation_address1(self):
        #address1edit
        regAddress=QRegExp("[\w\s-.,:]{15,120}")
        input_validator = QRegExpValidator(regAddress, self.address1Edit)
        result=input_validator.validate(self.address1Edit.text(),0)
        self.address1Edit.setValidator(input_validator)
        if(result[0]==2):
            self.flags['address1']=True
        else:
            self.flags['address1']=False

        #colors
        self.validation_color(result,self.address1Edit)


    def validation_address2(self):
        #address2Edit
        regAddress=QRegExp("([\w{15,120}\s-.,:]{15,120}|\w{0})")
        input_validator=QRegExpValidator(regAddress,self.address2Edit)
        result=input_validator.validate(self.address2Edit.text(),0)
        self.address2Edit.setValidator(input_validator)

        #colors
        self.validation_color(result,self.address2Edit)
        if(result[0]==2):
            self.flags['address2']=True
        else:
            self.flags['address2']=False

    #validation for phones
    def validation_phone1(self):
        #Phone
        regPhone=QRegExp("\d{10}")
        input_validator=QRegExpValidator(regPhone,self.phone1Edit)
        result=input_validator.validate(self.phone1Edit.text(),0)
        self.phone1Edit.setValidator(input_validator)
        self.validation_color(result,self.phone1Edit)
        if(result[0]==2):
            self.flags['phone1']=True
        else:
            self.flags['phone1']=False


    def validation_phone2(self):
        regPhone=QRegExp('(\d{10}|\d{0})')
        input_validator=QRegExpValidator(regPhone,self.phone2Edit)
        result=input_validator.validate(self.phone2Edit.text(),0)
        self.phone2Edit.setValidator(input_validator)
        self.validation_color(result,self.phone2Edit)
        if(result[0]==2):
            self.flags['phone2']=True
        else:
            self.flags['phone2']=False

    def validation_phone3(self):
        regPhone=QRegExp('(\d{10}|\d{0})')
        input_validator=QRegExpValidator(regPhone,self.phone3Edit)
        result=input_validator.validate(self.phone3Edit.text(),0)
        self.phone3Edit.setValidator(input_validator)
        self.validation_color(result,self.phone3Edit)
        if(result[0]==2):
            self.flags['phone3']=True
        else:
            self.flags['phone3']=False

    #validation for department
    def validation_department(self):
        regDepartment=QRegExp("^((?!Select Department).)*$")
        input_validator=QRegExpValidator(regDepartment,self.departmentEdit)
        result=input_validator.validate(self.departmentEdit.currentText(),0)
        self.departmentEdit.setValidator(input_validator)
        self.validation_color(result,self.departmentEdit)
        if(result[0]==2):
            self.flags['department']=True
        else:
            self.flags['department']=False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

