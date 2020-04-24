
from PyQt5 import QtCore, QtGui, QtWidgets

from OnlineRegister import Ui_LoginWindow
import MySQLdb as mdb 

class Ui_OnlineShop(object):

	def LoadData(self):
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur=conn.cursor()
			
			name=self.Reg_lineEdit_25.text()
			address=self.Reg_lineEdit_27.text()
			phoneNo=self.Reg_lineEdit_28.text()
			Password = self.Reg_lineEdit_26.text()
			if str(name)== ""  or str(Password)=="" or str(address)=="" or str(phoneNo)=="":
				self.Reg_label_10.setText("Invalid entry")
			elif len(Password)<3:
				self.Reg_label_10.setText("Weak Password")
			elif len(phoneNo)!=10:
				self.Reg_label_10.setText("Invalid Phone No")
			else:

			
			#if str(name)=="" or str(address)=="" or str(phoneNo)=="" or str(Password)=="":
			#self.blanklabel.setText("Please enter again")
				cur.execute("insert into Customers(customer_name,phone_no,customer_address,login,password) values('"+name+"','"+str(phoneNo)+"','"+address+"',1,'"+str(Password)+"')")
				cur.execute("select max(cus_id) from Customers")
				result=cur.fetchone()[0]
				self.Reg_label_10.setText(str(result))
				cur.close()


	def LoadData2(self):
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur1=conn.cursor()
			
			name=self.Reg_lineEdit_29.text()
			address=self.Reg_lineEdit_31.text()
			phoneNo=self.Reg_lineEdit_32.text()
			Password = self.Reg_lineEdit_30.text()
			if str(name)== ""  or str(Password)=="" or str(address)=="" or str(phoneNo)=="":
				self.Reg_label_34.setText("Invalid entry")
			elif len(Password)<3:
				self.Reg_label_34.setText("Weak Password")
			elif len(phoneNo)!=10:
				self.Reg_label_34.setText("Invalid Phone No")
			else:
			#if str(name)=="" or str(address)=="" or str(phoneNo)=="" or str(Password)=="":
			#self.blanklabel.setText("Please enter again")
				cur1.execute("insert into Suppliers(sup_add,supplier_name,login,password) values('"+address+"','"+name+"',0,'"+str(Password)+"')")
				cur1.execute("select max(sup_id) from Suppliers")
				result=cur1.fetchone()[0]
				self.Reg_label_34.setText(str(result))
				cur1.close()




	def ButtonState(self):
		if self.Reg_radioButton_6.isChecked() ==True:
			self.Reg_groupBox_3.setEnabled(False)
			self.Reg_groupBox_4.setEnabled(True)
			
		if self.Reg_radioButton_5.isChecked()==True:
			self.Reg_groupBox_4.setEnabled(False)
			self.Reg_groupBox_3.setEnabled(True)

	def OpenRegister(self):
		self.RegistergroupBox.show()
		self.HomePageGroupBox.hide()

	def OpenLogin(self):
		self.HomePageGroupBox.show()
		self.RegistergroupBox.hide()

	def BacktoFront(self):
		self.RegistergroupBox.hide()
		self.HomePageGroupBox.show()

	def setupUi(self, OnlineShop):
		OnlineShop.setObjectName("OnlineShop")
		OnlineShop.resize(962, 738)
		self.centralwidget = QtWidgets.QWidget(OnlineShop)
		self.centralwidget.setObjectName("centralwidget")

		# oImage = QImage("online-shopping-back.png")
		# sImage = oImage.scaled(QSize(900, 720))

		# palette =QPalette()
		# palette.setBrush(10, QBrush(sImage))
		# self.setPalette(palette)
		# self.label_i = QLabel('Test',self)
		# self.label_i.setGeometry(50,50,200,50)

		self.Logotext = QtWidgets.QTextEdit(self.centralwidget)
		self.Logotext.setGeometry(QtCore.QRect(30, 30, 900, 700))
		self.Logotext.setReadOnly(True)
		self.Logotext.setObjectName("Logotext")

		self.HomePageGroupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.HomePageGroupBox.setGeometry(QtCore.QRect(30, 30, 900, 700))
		self.HomePageGroupBox.setTitle("")
		self.HomePageGroupBox.setObjectName("HomePageGroupBox")
		
		#self.Logotext.
		self.framefront = QtWidgets.QFrame(self.HomePageGroupBox)
		self.framefront.setGeometry(QtCore.QRect(30, 30, 900, 700))
		self.framefront.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.framefront.setFrameShadow(QtWidgets.QFrame.Raised)
		self.framefront.setObjectName("framefront")
		self.WelcometextEdit = QtWidgets.QTextEdit(self.framefront)
		self.WelcometextEdit.setGeometry(QtCore.QRect(240, 170, 191, 61))
		font = QtGui.QFont()
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.WelcometextEdit.setFont(font)
		self.WelcometextEdit.setReadOnly(True)
		self.WelcometextEdit.setObjectName("WelcometextEdit")
		self.verticalWidget = QtWidgets.QWidget(self.framefront)
		self.verticalWidget.setGeometry(QtCore.QRect(240, 240, 211, 101))
		self.verticalWidget.setObjectName("verticalWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.loginFrontButton = QtWidgets.QPushButton(self.verticalWidget)
		self.loginFrontButton.setObjectName("loginFrontButton")

		self.loginFrontButton.clicked.connect(self.OpenLogin)

		self.verticalLayout.addWidget(self.loginFrontButton)
		self.FrontregisterButton = QtWidgets.QPushButton(self.verticalWidget)
		self.FrontregisterButton.setObjectName("FrontregisterButton")

		self.FrontregisterButton.clicked.connect(self.OpenRegister)

		self.verticalLayout.addWidget(self.FrontregisterButton)
		# self.loggedincheckBox = QtWidgets.QCheckBox(self.framefront)
		# self.loggedincheckBox.setGeometry(QtCore.QRect(70, 250, 151, 26))
		# self.loggedincheckBox.setObjectName("loggedincheckBox")
		self.RegistergroupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.RegistergroupBox.setGeometry(QtCore.QRect(20, 10, 881, 591))
		self.RegistergroupBox.setTitle("")
		self.RegistergroupBox.setObjectName("RegistergroupBox")

		self.RegistergroupBox.hide()

		self.Reg_radioButton_6 = QtWidgets.QRadioButton(self.RegistergroupBox)
		self.Reg_radioButton_6.setGeometry(QtCore.QRect(480, 130, 121, 26))
		self.Reg_radioButton_6.setStyleSheet("")
		self.Reg_radioButton_6.setObjectName("Reg_radioButton_6")

		self.Reg_radioButton_6.clicked.connect(self.ButtonState)

		self.Reg_groupBox_3 = QtWidgets.QGroupBox(self.RegistergroupBox)
		self.Reg_groupBox_3.setGeometry(QtCore.QRect(40, 160, 391, 391))
		self.Reg_groupBox_3.setStyleSheet("")
		self.Reg_groupBox_3.setTitle("")
		self.Reg_groupBox_3.setObjectName("Reg_groupBox_3")

		self.Reg_groupBox_3.setEnabled(False)

		self.Reg_label_26 = QtWidgets.QLabel(self.Reg_groupBox_3)
		self.Reg_label_26.setGeometry(QtCore.QRect(30, 140, 81, 20))
		self.Reg_label_26.setStyleSheet("")
		self.Reg_label_26.setObjectName("Reg_label_26")
		self.Reg_label_27 = QtWidgets.QLabel(self.Reg_groupBox_3)
		self.Reg_label_27.setGeometry(QtCore.QRect(30, 190, 101, 20))
		self.Reg_label_27.setStyleSheet("")
		self.Reg_label_27.setObjectName("Reg_label_27")
		self.Reg_lineEdit_25 = QtWidgets.QLineEdit(self.Reg_groupBox_3)
		self.Reg_lineEdit_25.setGeometry(QtCore.QRect(160, 100, 171, 28))
		self.Reg_lineEdit_25.setObjectName("Reg_lineEdit_25")
		self.Reg_label_28 = QtWidgets.QLabel(self.Reg_groupBox_3)
		self.Reg_label_28.setGeometry(QtCore.QRect(30, 230, 101, 20))
		self.Reg_label_28.setStyleSheet("")
		self.Reg_label_28.setObjectName("Reg_label_28")
		self.Reg_pushButton_8 = QtWidgets.QPushButton(self.Reg_groupBox_3)
		self.Reg_pushButton_8.setGeometry(QtCore.QRect(130, 270, 91, 28))
		self.Reg_pushButton_8.setStyleSheet("")
		self.Reg_pushButton_8.setObjectName("Reg_pushButton_8")

		self.Reg_pushButton_8.clicked.connect(self.LoadData)

		self.Reg_lineEdit_26 = QtWidgets.QLineEdit(self.Reg_groupBox_3)
		self.Reg_lineEdit_26.setGeometry(QtCore.QRect(160, 220, 171, 28))
		self.Reg_lineEdit_26.setEchoMode(QtWidgets.QLineEdit.Password)
		self.Reg_lineEdit_26.setObjectName("Reg_lineEdit_26")
		self.Reg_label_29 = QtWidgets.QLabel(self.Reg_groupBox_3)
		self.Reg_label_29.setGeometry(QtCore.QRect(30, 100, 70, 20))
		self.Reg_label_29.setStyleSheet("")
		self.Reg_label_29.setObjectName("Reg_label_29")
		self.Reg_lineEdit_27 = QtWidgets.QLineEdit(self.Reg_groupBox_3)
		self.Reg_lineEdit_27.setGeometry(QtCore.QRect(160, 140, 171, 28))
		self.Reg_lineEdit_27.setObjectName("Reg_lineEdit_27")
		self.Reg_lineEdit_28 = QtWidgets.QLineEdit(self.Reg_groupBox_3)
		self.Reg_lineEdit_28.setGeometry(QtCore.QRect(160, 180, 171, 28))
		self.Reg_lineEdit_28.setObjectName("Reg_lineEdit_28")
		self.Reg_label_9 = QtWidgets.QLabel(self.Reg_groupBox_3)
		self.Reg_label_9.setGeometry(QtCore.QRect(51, 330, 131, 20))
		self.Reg_label_9.setStyleSheet("")
		self.Reg_label_9.setObjectName("Reg_label_9")
		self.Reg_label_10 = QtWidgets.QLabel(self.Reg_groupBox_3)
		self.Reg_label_10.setGeometry(QtCore.QRect(190, 330, 151, 20))
		self.Reg_label_10.setText("")
		self.Reg_label_10.setObjectName("Reg_label_10")
		self.Reg_pushButton_7 = QtWidgets.QPushButton(self.RegistergroupBox)
		self.Reg_pushButton_7.setGeometry(QtCore.QRect(400, 560, 83, 28))
		self.Reg_pushButton_7.setStyleSheet("")
		self.Reg_pushButton_7.setObjectName("Reg_pushButton_7")

		self.Reg_pushButton_7.clicked.connect(self.BacktoFront)

		self.Reg_radioButton_5 = QtWidgets.QRadioButton(self.RegistergroupBox)
		self.Reg_radioButton_5.setGeometry(QtCore.QRect(50, 130, 141, 26))
		self.Reg_radioButton_5.setStyleSheet("")
		self.Reg_radioButton_5.setObjectName("Reg_radioButton_5")

		self.Reg_radioButton_5.clicked.connect(self.ButtonState)

		self.Reg_pushButton_2 = QtWidgets.QPushButton(self.RegistergroupBox)
		self.Reg_pushButton_2.setGeometry(QtCore.QRect(0, 50, 71, 21))
		self.Reg_pushButton_2.setStyleSheet("")
		self.Reg_pushButton_2.setObjectName("Reg_pushButton_2")

		self.Reg_pushButton_2.clicked.connect(self.BacktoFront)

		self.Reg_label_5 = QtWidgets.QLabel(self.RegistergroupBox)
		self.Reg_label_5.setGeometry(QtCore.QRect(320, 30, 311, 51))
		font = QtGui.QFont()
		font.setFamily("DejaVu Math TeX Gyre")
		font.setPointSize(20)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.Reg_label_5.setFont(font)
		self.Reg_label_5.setObjectName("Reg_label_5")
		self.Reg_groupBox_4 = QtWidgets.QGroupBox(self.RegistergroupBox)
		self.Reg_groupBox_4.setGeometry(QtCore.QRect(460, 160, 401, 391))
		self.Reg_groupBox_4.setTitle("")
		self.Reg_groupBox_4.setObjectName("Reg_groupBox_4")

		self.Reg_groupBox_4.setEnabled(False)

		self.Reg_label_30 = QtWidgets.QLabel(self.Reg_groupBox_4)
		self.Reg_label_30.setGeometry(QtCore.QRect(50, 140, 81, 20))
		self.Reg_label_30.setStyleSheet("")
		self.Reg_label_30.setObjectName("Reg_label_30")
		self.Reg_label_31 = QtWidgets.QLabel(self.Reg_groupBox_4)
		self.Reg_label_31.setGeometry(QtCore.QRect(51, 190, 101, 20))
		self.Reg_label_31.setStyleSheet("")
		self.Reg_label_31.setObjectName("Reg_label_31")
		self.Reg_lineEdit_29 = QtWidgets.QLineEdit(self.Reg_groupBox_4)
		self.Reg_lineEdit_29.setGeometry(QtCore.QRect(160, 100, 171, 28))
		self.Reg_lineEdit_29.setObjectName("Reg_lineEdit_29")
		self.Reg_label_32 = QtWidgets.QLabel(self.Reg_groupBox_4)
		self.Reg_label_32.setGeometry(QtCore.QRect(50, 230, 101, 20))
		self.Reg_label_32.setStyleSheet("")
		self.Reg_label_32.setObjectName("Reg_label_32")
		self.Reg_pushButton_9 = QtWidgets.QPushButton(self.Reg_groupBox_4)
		self.Reg_pushButton_9.setGeometry(QtCore.QRect(130, 270, 101, 28))
		self.Reg_pushButton_9.setStyleSheet("")
		self.Reg_pushButton_9.setObjectName("Reg_pushButton_9")

		self.Reg_pushButton_9.clicked.connect(self.LoadData2)

		self.Reg_lineEdit_30 = QtWidgets.QLineEdit(self.Reg_groupBox_4)
		self.Reg_lineEdit_30.setGeometry(QtCore.QRect(160, 220, 171, 28))
		self.Reg_lineEdit_30.setEchoMode(QtWidgets.QLineEdit.Password)
		self.Reg_lineEdit_30.setObjectName("Reg_lineEdit_30")
		self.Reg_label_33 = QtWidgets.QLabel(self.Reg_groupBox_4)
		self.Reg_label_33.setGeometry(QtCore.QRect(50, 100, 61, 20))
		self.Reg_label_33.setStyleSheet("")
		self.Reg_label_33.setObjectName("Reg_label_33")
		self.Reg_lineEdit_31 = QtWidgets.QLineEdit(self.Reg_groupBox_4)
		self.Reg_lineEdit_31.setGeometry(QtCore.QRect(160, 140, 171, 28))
		self.Reg_lineEdit_31.setObjectName("Reg_lineEdit_31")
		self.Reg_lineEdit_32 = QtWidgets.QLineEdit(self.Reg_groupBox_4)
		self.Reg_lineEdit_32.setGeometry(QtCore.QRect(160, 180, 171, 28))
		self.Reg_lineEdit_32.setObjectName("Reg_lineEdit_32")
		self.Reg_label_11 = QtWidgets.QLabel(self.Reg_groupBox_4)
		self.Reg_label_11.setGeometry(QtCore.QRect(50, 330, 111, 20))
		self.Reg_label_11.setStyleSheet("")
		self.Reg_label_11.setObjectName("Reg_label_11")
		self.Reg_label_34 = QtWidgets.QLabel(self.Reg_groupBox_4)
		self.Reg_label_34.setGeometry(QtCore.QRect(180, 330, 151, 20))
		self.Reg_label_34.setText("")
		self.Reg_label_34.setObjectName("Reg_label_34")
		OnlineShop.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(OnlineShop)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 22))
		self.menubar.setObjectName("menubar")
		OnlineShop.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(OnlineShop)
		self.statusbar.setObjectName("statusbar")
		OnlineShop.setStatusBar(self.statusbar)

		self.retranslateUi(OnlineShop)
		QtCore.QMetaObject.connectSlotsByName(OnlineShop)

	def retranslateUi(self, OnlineShop):
		_translate = QtCore.QCoreApplication.translate
		OnlineShop.setWindowTitle(_translate("OnlineShop", "MainWindow"))

		
		self.WelcometextEdit.setHtml(_translate("OnlineShop", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; font-style:italic;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:20pt; color:#5c3566;\">OnlineRUs </span></p></body></html>"))
		self.loginFrontButton.setText(_translate("OnlineShop", "Log In"))
		self.FrontregisterButton.setText(_translate("OnlineShop", "Register"))
		#self.loggedincheckBox.setText(_translate("OnlineShop", "Keep me Logged in"))
		self.Reg_radioButton_6.setText(_translate("OnlineShop", "Supplier"))
		self.Reg_label_26.setText(_translate("OnlineShop", "Address"))
		self.Reg_label_27.setText(_translate("OnlineShop", "Phone No."))
		self.Reg_label_28.setText(_translate("OnlineShop", "Password"))
		self.Reg_pushButton_8.setText(_translate("OnlineShop", "Register"))
		self.Reg_label_29.setText(_translate("OnlineShop", "Name"))
		self.Reg_label_9.setText(_translate("OnlineShop", "CustomerID"))
		self.Reg_pushButton_7.setText(_translate("OnlineShop", "Next"))
		self.Reg_radioButton_5.setText(_translate("OnlineShop", "Customer"))
		self.Reg_pushButton_2.setText(_translate("OnlineShop", "Back"))
		self.Reg_label_5.setText(_translate("OnlineShop", "Registration Details"))
		self.Reg_label_30.setText(_translate("OnlineShop", "Address"))
		self.Reg_label_31.setText(_translate("OnlineShop", "Phone No."))
		self.Reg_label_32.setText(_translate("OnlineShop", "Password"))
		self.Reg_pushButton_9.setText(_translate("OnlineShop", "Register"))
		self.Reg_label_33.setText(_translate("OnlineShop", "Name"))
		self.Reg_label_11.setText(_translate("OnlineShop", "SupplierID"))
		self.Logotext.setHtml(_translate("view1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>HTML  Tag</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"/home/arr/Desktop/DBMS Lab/OnlineShopProject/final/online-shopping-back.png\" width=\"800\" height=\"600\" /></p></body></html>"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	OnlineShop = QtWidgets.QMainWindow()
	ui = Ui_OnlineShop()
	ui.setupUi(OnlineShop)
	OnlineShop.show()
	sys.exit(app.exec_())

