from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from datetime import datetime, timedelta
from mysql.connector import Error
from additional_files import utilities as u 
import uuid
import ctypes

class Ui_MainWindow(QtWidgets.QFileDialog):

    def __init__(self,db):
        super().__init__()
        self.db=db
    
    #GUI
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
        MainWindow.resize(1366,768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("*\n"
                                    "{\n"
                                    "    font-family:Century Gothic;\n"
                                    "    font-size:15px;\n"
                                    "}\n"
                                    "\n"
                                    "QFrame{\n"
                                        "background:rgb(255, 255, 217);\n"
                                        "border:2px solid black;\n"
                                    "}\n"
                                    "Qlabel#ImageLabel\n"
                                    "{    \n"
                                    "    border:1px solid black\n"
                                    "}\n"
                                    "QLabel{\n"
                                    "    font-weight:bold;\n"
                                    "    border:none\n"
                                    "}\n"
                                    "QLineEdit\n"
                                    "{\n"
                                    "    background:white;\n"
                                    "    padding:5px;\n"
                                    "    font-size:12px;\n"
                                    "}\n"
                                    "QPushButton{\n"
                                        "background:white;\n"
                                        "padding:2px;\n"
                                        "font-size:10px;\n"
                                        "border-style:inlet;\n"
                                        "border:1px solid black;\n"
                                    "}\n"
                                    "QPushButton#Submit{\n"
                                    "    background:rgb(15, 73, 61);\n"
                                    "    font-size:15px;\n"
                                    "    color:white;"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "    border-style:outlet;\n"
                                    "}\n"
                                    "QComboBox{\n"
                                    "    background:white;\n"
                                    "    border-style:inlet;\n"
                                    "    border:1px solid black;\n"
                                    "}\n"
                                    "QComboBox:focus{\n"
                                    "        border-style:outlet;\n"
                                    "}\n"
                                    "QDateEdit{\n"
                                    "    background:white;\n"
                                    "}\n"
                                    "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.NameEdit = QtWidgets.QLineEdit(self.frame)
        self.NameEdit.setGeometry(QtCore.QRect(280, 70, 371, 41))
        self.NameEdit.setObjectName("NameEdit")
        self.DOBEdit = QtWidgets.QDateEdit(self.frame)
        self.DOBEdit.setGeometry(QtCore.QRect(280, 150, 191, 24))
        self.DOBEdit.setObjectName("DOBEdit")
        self.minimumDateDob=datetime.today()-timedelta(days=365*20)
        self.DOBEdit.setMaximumDateTime(self.minimumDateDob)
        self.DOBEdit.setMinimumDateTime(datetime.today()-timedelta(days=365*60))
        self.DOJEdit = QtWidgets.QDateEdit(self.frame)
        self.DOJEdit.setGeometry(QtCore.QRect(960, 150, 191, 24))
        self.DOJEdit.setObjectName("DOJEdit")
        self.DOJEdit.setMaximumDateTime(datetime.today())
        self.minimumDateDoj=datetime(1932,10,15) 
        self.DOJEdit.setMinimumDateTime(self.minimumDateDoj)
        self.DOB = QtWidgets.QLabel(self.frame)
        self.DOB.setGeometry(QtCore.QRect(90, 150, 100, 21))
        self.DOB.setObjectName("DOB")
        self.ImageButton = QtWidgets.QPushButton(self.frame)
        self.ImageButton.setGeometry(QtCore.QRect(1160, 230, 91, 21))
        self.ImageButton.setObjectName("ImageButton")
        self.SignatureButton = QtWidgets.QPushButton(self.frame)
        self.SignatureButton.setGeometry(QtCore.QRect(1160, 410, 91, 21))
        self.SignatureButton.setObjectName("SignatureButton")
        self.DepartmentEdit = QtWidgets.QComboBox(self.frame)
        self.DepartmentEdit.setGeometry(QtCore.QRect(280, 540, 271, 24))
        self.DepartmentEdit.setAcceptDrops(False)
        self.DepartmentEdit.setEditable(True)
        self.DepartmentEdit.setObjectName("DepartmentEdit")
        self.DepartmentEdit.addItem("")
        self.DepartmentEdit.addItem("")
        self.DepartmentEdit.addItem("")
        self.DepartmentEdit.addItem("")
        self.Department = QtWidgets.QLabel(self.frame)
        self.Department.setGeometry(QtCore.QRect(90, 540, 147, 18))
        self.Department.setObjectName("Department")
        self.Submit = QtWidgets.QPushButton(self.frame)
        self.Submit.setGeometry(QtCore.QRect(610, 590, 101, 41))
        self.Submit.setObjectName("Submit")
        self.Status = QtWidgets.QLabel(self.frame)
        self.Status.setGeometry(QtCore.QRect(5, 650, 1341, 30))
        self.Status.setObjectName("Status")
        self.ImageLabel = QtWidgets.QLabel(self.frame)
        self.ImageLabel.setGeometry(QtCore.QRect(960, 220, 91, 111))
        self.ImageLabel.setText("")
        self.ImageLabel.setObjectName("ImageLabel")
        self.SigLabel = QtWidgets.QLabel(self.frame)
        self.SigLabel.setGeometry(QtCore.QRect(950, 400, 121, 41))
        self.SigLabel.setText("")
        self.SigLabel.setObjectName("SigLabel")
        self.Name = QtWidgets.QLabel(self.frame)
        self.Name.setGeometry(QtCore.QRect(90, 80, 71, 21))
        self.Name.setObjectName("Name")
        self.Address1 = QtWidgets.QLabel(self.frame)
        self.Address1.setGeometry(QtCore.QRect(90, 240, 91, 16))
        self.Address1.setObjectName("Address1")
        self.Address2 = QtWidgets.QLabel(self.frame)
        self.Address2.setGeometry(QtCore.QRect(90, 360, 81, 20))
        self.Address2.setObjectName("Address2")
        self.address1Edit = QtWidgets.QLineEdit(self.frame)
        self.address1Edit.setGeometry(QtCore.QRect(280, 220, 581, 71))
        self.address1Edit.setText("")
        self.address1Edit.setObjectName("address1Edit")
        self.address2Edit = QtWidgets.QLineEdit(self.frame)
        self.address2Edit.setGeometry(QtCore.QRect(280, 330, 581, 71))
        self.address2Edit.setObjectName("address2Edit")
        self.Phone = QtWidgets.QLabel(self.frame)
        self.Phone.setGeometry(QtCore.QRect(90, 460, 91, 16))
        self.Phone.setObjectName("Phone")
        self.phone1Edit = QtWidgets.QLineEdit(self.frame)
        self.phone1Edit.setGeometry(QtCore.QRect(280, 450, 121, 31))
        self.phone1Edit.setObjectName("phone1Edit")
        self.phone2Edit = QtWidgets.QLineEdit(self.frame)
        self.phone2Edit.setGeometry(QtCore.QRect(420, 450, 131, 31))
        self.phone2Edit.setObjectName("phone2Edit")
        self.phone3Edit = QtWidgets.QLineEdit(self.frame)
        self.phone3Edit.setGeometry(QtCore.QRect(570, 450, 141, 31))
        self.phone3Edit.setObjectName("phone3Edit")
        self.DOJ = QtWidgets.QLabel(self.frame)
        self.DOJ.setGeometry(QtCore.QRect(810, 150, 121, 21))
        self.DOJ.setObjectName("DOJ")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(280, 120, 261, 16))
        self.label.setStyleSheet("color:brown;\n"
"font-size:10px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(280, 300, 361, 16))
        self.label_2.setStyleSheet("color:brown;\n"
"font-size:10px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(280, 490, 271, 16))
        self.label_3.setStyleSheet("color:brown;\n"
"font-size:10px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(1170, 260, 71, 16))
        self.label_4.setStyleSheet("color:brown;\n"
"font-size:10px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(1180, 440, 71, 20))
        self.label_5.setStyleSheet("color:brown;\n"
"font-size:10px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.MainWindow=MainWindow
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Employee"))
        self.NameEdit.setPlaceholderText(_translate("MainWindow", "Enter the name "))
        self.DOB.setText(_translate("MainWindow", "Date of Birth *"))
        self.DOBEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.DOJEdit.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.ImageButton.setText(_translate("MainWindow", "Add Image"))
        self.SignatureButton.setText(_translate("MainWindow", "Add Signature"))
        self.DepartmentEdit.setItemText(0, _translate("MainWindow", "Select Department"))
        self.DepartmentEdit.setItemText(1, _translate("MainWindow", "Information Technology"))
        self.DepartmentEdit.setItemText(2, _translate("MainWindow", "Mechanical Deptartment"))
        self.DepartmentEdit.setItemText(3, _translate("MainWindow", "Electrical Department"))
        self.Department.setText(_translate("MainWindow", "Select Department *"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        self.Status.setText(_translate("MainWindow", ""))
        self.Name.setText(_translate("MainWindow", "Name *"))
        self.Address1.setText(_translate("MainWindow", "Address 1 *"))
        self.Address2.setText(_translate("MainWindow", "Address 2"))
        self.address1Edit.setPlaceholderText(_translate("MainWindow", "Add address"))
        self.address2Edit.setPlaceholderText(_translate("MainWindow", "Add address 2 (optional)"))
        self.phone2Edit.setPlaceholderText(_translate("MainWindow","(optional)"))
        self.phone3Edit.setPlaceholderText(_translate("MainWindow","(optional)"))
        self.Phone.setText(_translate("MainWindow", "Phone No. *"))
        self.DOJ.setText(_translate("MainWindow", "Date of Joining*"))
        self.label.setText(_translate("MainWindow", "Name should be atleast 3 characters long"))
        self.label_2.setText(_translate("MainWindow", "Address should be alteast 15 characters long "))
        self.label_3.setText(_translate("MainWindow", "A ten-digit phone number is required"))
        self.label_4.setText(_translate("MainWindow", "Required"))
        self.label_5.setText(_translate("MainWindow", "Required"))
        self.photo=''
        self.sig=''
        self.NameEdit.setFocus()
        self.Status.hide()

        #click events
        self.ImageButton.clicked.connect(self.fileExplorer)
        self.SignatureButton.clicked.connect(self.fileExplorerSig)
        self.Submit.clicked.connect(self.onSubmit)

        #return key
        self.NameEdit.returnPressed.connect(self.DOBEdit.setFocus)
        self.DOBEdit.editingFinished.connect(self.DOJEdit.setFocus)
        self.DOJEdit.editingFinished.connect(self.address1Edit.setFocus)
        self.address1Edit.returnPressed.connect(self.address2Edit.setFocus)
        self.address2Edit.returnPressed.connect(self.phone1Edit.setFocus)
        self.phone1Edit.returnPressed.connect(self.phone2Edit.setFocus)
        self.phone2Edit.returnPressed.connect(self.phone3Edit.setFocus)
        self.phone3Edit.returnPressed.connect(self.ImageButton.click)
        self.DepartmentEdit.lineEdit().returnPressed.connect(self.onSubmit)
       
        #flags for validation
        self.flags={
            "name":False,
            "address1":False,  
            "address2":True,   
            "phone1":False,    
            "phone2":True,     
            "phone3":True,     
            "department":False,  
            "image":False,
            "sig":False
        }

        #validation
        self.NameEdit.editingFinished.connect(self.validation_name)
        self.NameEdit.textChanged.connect(self.validation_name)
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
        self.DepartmentEdit.editTextChanged.connect(self.validation_department)


    def onSubmit(self):
        #if all the flags are true then the form can be submitted
        if(self.photo!=''):
            self.flags['image']=True
        else:
            self.flags['image']=False
        
        if(self.sig!=''):
            self.flags['sig']=True
        else:
            self.flags['sig']=False
        
        count=0
        for flag in self.flags:
            if(self.flags[flag]==True):
                count=count+1
        
        if count==9:
            self.shouldSubmit=True
            self.onChecking()

        else:
            self.shouldSubmit=False
      

    def onChecking(self):
        buttonBox = QtWidgets.QMessageBox.question(self, 'Submit details', "Are you sure you want to submit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        if(buttonBox==QtWidgets.QMessageBox.Yes):
            self.connectDatabase()
        elif(buttonBox==QtWidgets.QMessageBox.No):
            self.DepartmentEdit.lineEdit().setFocus()
       
    def generateUniqueId(self,size):
            #generates a unique id
            id=uuid.uuid1()

            #converting id into int and resizing it to given size
            id=id.int % (10**(size))

            return id


    def connectDatabase(self):
        if(self.shouldSubmit!=False):
            self.Submit.setText('Submitting...')
            cur=self.db.cursor()

            #generating a unique id for every employee
            id=self.generateUniqueId(9)

            #saving all the texts in small words for ease
            info={
                    "name":self.NameEdit.text(),
                    "dob":str(self.DOBEdit.text()),
                    "doj":str(self.DOJEdit.text()),
                    "address":[self.address1Edit.text(),self.address2Edit.text()],
                    "phone":[self.phone1Edit.text(),self.phone2Edit.text(),self.phone3Edit.text()],
                    "department":str(self.DepartmentEdit.currentText()),
                    "photo":self.photo,
                    "sig":self.sig
                    }

            #queries for inserting data
            employeeQuery="insert into employee values(%s,%s,%s,%s)"
            employeeAddressQuery="insert into employeeAddress values(%s,%s)"
            employeeTelephoneQuery="insert into employeeTelephone values(%s,%s)"
            employeePhotoquery = "Insert into employeePhoto values(%s,%s)"
            employeeSigquery = "Insert into employeeSig values(%s,%s)"
            employeeDepartmentQuery="insert into employeeDepartment values(%s,%s)"

            #inserting data
            
            #adding name, date of birth , date of joining
            try:
                cur.execute(employeeQuery,(id,info['dob'],info['name'],info['doj']))
                self.db.commit()

                #adding addresses 
                for addr in info['address']:
                    if(addr!=''):
                        cur.execute(employeeAddressQuery,(id,addr))
                        self.db.commit()

                #adding phone numbers
                for num in info['phone']:
                    if(num!=''):
                        cur.execute(employeeTelephoneQuery,(id,int(num)))
                        self.db.commit()

                #adding department
                cur.execute(employeeDepartmentQuery,(id,info['department']))
                self.db.commit()

                #adding photo
                cur.execute(employeePhotoquery,(id,info['photo']))
                self.db.commit()

                #adding signature
                cur.execute(employeeSigquery,(id,info['sig']))
                self.db.commit()

            except Error as e:
                self.status.setStyleSheet('background:rgb(212,115,70)')
                self.status.show()
                if e.errno==1062:
                    self.status.setText('Duplicate Id error : Try Submitting again')
 
                if e.errno==1146:
                    self.status.setText('Problem with the Database (table does not exist)')

                elif e.errno==1054:
                    self.status.setText('Problem with the Database (column does not exist)')


            #GUI
            self.Status.setStyleSheet(
                "background:rgb(15, 73, 61);\n"
                "color:white;\n"
                "padding:5px;\n"
                "font-size:12px;\n"
                "font-weight:bold")
            self.Status.show()
            self.Status.setText("New Employee added successfully")
            self.Submit.setText('Submitted')
            messageText="UserId : {}   (Note for future references)".format(id)    
            messageBox = QtWidgets.QMessageBox.question(self, 'Info', messageText, QtWidgets.QMessageBox.Ok , QtWidgets.QMessageBox.Ok)
                
            if(messageBox==QtWidgets.QMessageBox.Ok):
                self.clearData()

        else:
            self.Status.show()
            print('form is incomplete')
            self.Status.setStyleSheet(
                "background:rgb(212,115,70);\n"
                "color:black;\n"
                "padding:5px;\n"
                "font-size:12px;\n")
            self.Status.setText("Form is incomplete")

    def clearData(self):
        style='background:(255,255,217)'
        self.NameEdit.setText('')
        self.NameEdit.setStyleSheet(style)
        self.DOBEdit.setDate(self.minimumDateDob)
        self.DOJEdit.setDate(self.minimumDateDoj)
        self.address1Edit.setText('')
        self.address1Edit.setStyleSheet(style)
        self.address2Edit.setText('')
        self.phone1Edit.setText('')
        self.phone1Edit.setStyleSheet(style)
        self.phone2Edit.setText('')
        self.phone3Edit.setText('')
        self.DepartmentEdit.setCurrentIndex(0)
        self.DepartmentEdit.setStyleSheet(style)
        self.ImageLabel.setPixmap(QtGui.QPixmap(''))
        self.ImageButton.setStyleSheet(style)
        self.SigLabel.setPixmap(QtGui.QPixmap(''))
        self.SignatureButton.setStyleSheet(style)
        self.Status.setText('')
        self.Status.hide()
        self.NameEdit.setFocus()
        self.Submit.setText('Submit')


    #adding image
    def fileExplorer(self):
        name=QtWidgets.QFileDialog.getOpenFileName(self,'Open file','c\\','Image files (*.jpg *.png *.jpeg)')
        if name[0]!='':
            imagePath=name[0]
            self.photo=u.read_file(imagePath)
            
            #GUI
            pixmap=QtGui.QPixmap(imagePath)
            pixmap=pixmap.scaled(100,200,QtCore.Qt.KeepAspectRatio)
            self.ImageLabel.setPixmap(pixmap)
            self.ImageLabel.setScaledContents(True)
            self.fileExplorerSig()


    #adding signature
    def fileExplorerSig(self):
        name=QtWidgets.QFileDialog.getOpenFileName(self,'Open file','c\\','Image files (*.jpg)')
        if name[0]!='':
            imagePath=name[0]
            self.sig=u.read_file(imagePath)
            
            #GUI
            pixmap=QtGui.QPixmap(imagePath)
            pixmap=pixmap.scaled(200, 100, QtCore.Qt.KeepAspectRatio)
            self.SigLabel.setPixmap(pixmap)
            self.SigLabel.setScaledContents(True)
            self.DepartmentEdit.setFocus()


    #setting up color for onchange validation
    def validation_color(self,result,name):
        if(result[0]==2): 
            name.setStyleSheet("background:rgb(255, 255, 217)")
        else:
            name.setStyleSheet('background:rgb(212, 115, 70)')


    #validation for name
    def validation_name(self):
        regName=QRegExp("\w{3,}\s?\w*")
        input_validator = QRegExpValidator(regName, self.NameEdit)
        result=input_validator.validate(self.NameEdit.text(),0)
        self.NameEdit.setValidator(input_validator)
        self.validation_color(result,self.NameEdit)
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
        regAddress=QRegExp("([\w\s-.,:]{15,120}|\w{0})")
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
        input_validator=QRegExpValidator(regDepartment,self.DepartmentEdit)
        result=input_validator.validate(self.DepartmentEdit.currentText(),0)
        self.DepartmentEdit.setValidator(input_validator)
        self.validation_color(result,self.DepartmentEdit)
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
