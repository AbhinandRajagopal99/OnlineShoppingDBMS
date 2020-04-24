

from PyQt5 import QtCore, QtGui, QtWidgets

import MySQLdb as mdb
from PdtDetails import Ui_MainWindow3
#from Place_OrderFinal import Ui_Place_Order
from supoption import Ui_SupOption

class Ui_LoginWindow(object):

	def ButtonState(self):
		if self.cuslogradioButton.isChecked() ==True:
			self.supplierloginBox.setEnabled(False)
			self.customerlogBox.setEnabled(True)
		if self.suplogradioButton.isChecked()==True:
			self.customerlogBox.setEnabled(False)
			self.supplierloginBox.setEnabled(True)

	def check1(self):
		custID=self.cusidlogline.text()
		Password=self.cuspassline.text()
		if str(custID)== ""  or str(Password)=="" or len(Password)<3:
			self.displayloginlabel1.setText("Invalid entry")
			#self.pushButton.setEnabled(False)
			#self.label_7.setText("")
		else:
			count=0
			#self.pushButton.setEnabled(True)
			self.displayloginlabel1 .setText("") 
			#self.pushButton.clicked.connect(self.openWindow)
			#self.openWindow()
			conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
			with conn:
				cur=conn.cursor()
				stmt="select *from Customers where cus_id=%(cus_id)s"
				cur.execute(stmt,{'cus_id':str(custID)})

				count=cur.rowcount
			
				if count==0:
					self.displayloginlabel1.setText("CustID or Password not found")
				else :
					cur.execute('select Password from Customers where cus_id= '+str(custID)+'')
					result=cur.fetchone()[0]
					
					if str(result)==str(Password):
						#self.label_7.setText(str(result))
						cur.execute('update Customers set login=0')
						conn.commit()
						cur.execute('update Customers set login=1 where cus_id= "'+str(custID)+'"')
						conn.commit()
						self.openCusWindow()

						# query = """ UPDATE Customers
						# SET login = %s
						# WHERE cus_id = %s """
						# data = (1, str(custID))
						# cur.execute(query, data)
						#cur.execute('update Customers set login=1 where cus_id= "'+str(custID)+'"')
						#self.openWindow()
						
					else:
						self.displayloginlabel1.setText("Incorrect Password")
				cur.close()

	def check2(self):
		custID=self.supidloginline.text()
		Password=self.suppassline.text()
		if str(custID)== "" or str(Password)=="" or len(Password)<3:
			self.displayloginlabel2.setText("Invalid entry")
			#self.pushButton_2.setEnabled(False)
			#self.label_7.setText("")
		else:
			#self.pushButton_2.setEnabled(True)
			self.displayloginlabel2 .setText("") 
		   # self.anotherWindow()
		# if str(custID)== ""  or str(Password)=="" or len(Password)<4:
		#     self.label_7.setText("Invalid entry")
		#     self.pushButton.setEnabled(False)
		#     #self.label_7.setText("")
		# else:
		#     self.pushButton.setEnabled(True)
		#     self.label_7 .setText("") 
		#     #self.pushButton.clicked.connect(self.openWindow)
		#     self.openWindow()
			conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
			with conn:
				cur=conn.cursor()
				stmt="select *from Suppliers where sup_id=%(sup_id)s"
				cur.execute(stmt,{'sup_id':str(custID)})

				count=cur.rowcount
				
				if count==0:
					self.displayloginlabel2.setText("SupID or Password not found")
				else:
					cur.execute('select Password from Suppliers where sup_id= '+str(custID)+'')
					result=cur.fetchone()[0]
					
					if str(result)==str(Password):
						cur.execute('update Suppliers set login=0')
						conn.commit()
						cur.execute('update Suppliers set login=1 where sup_id= '+str(custID)+'')
						conn.commit()
						#self.label_7.setText(str(result))
						self.openSupWindow()
					else:
						self.displayloginlabel2.setText("Incorrect Password")
				cur.close()

	def openSupWindow(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_SupOption()
		self.ui.setupUi(self.window)
		self.window.show()
		#self.close

	def openCusWindow(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_MainWindow3()
		self.ui.setupUi(self.window)
		self.window.show()
		
	#def close(self):
		#app.quit()

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(898, 669)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.LoginPagegroupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.LoginPagegroupBox.setGeometry(QtCore.QRect(120, 30, 681, 551))
		self.LoginPagegroupBox.setTitle("")
		self.LoginPagegroupBox.setObjectName("LoginPagegroupBox")
		self.textEditlogin = QtWidgets.QTextEdit(self.LoginPagegroupBox)
		self.textEditlogin.setGeometry(QtCore.QRect(230, 50, 241, 61))
		font = QtGui.QFont()
		font.setPointSize(6)
		self.textEditlogin.setFont(font)
		self.textEditlogin.setReadOnly(True)
		self.textEditlogin.setObjectName("textEditlogin")
		self.suplogradioButton = QtWidgets.QRadioButton(self.LoginPagegroupBox)
		self.suplogradioButton.setGeometry(QtCore.QRect(420, 160, 121, 26))
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(12)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.suplogradioButton.setFont(font)
		self.suplogradioButton.setStyleSheet("background-color: rgb(238, 238, 236);\n""border-color: rgb(32, 74, 135);")
		self.suplogradioButton.setObjectName("suplogradioButton")

		self.suplogradioButton.clicked.connect(self.ButtonState)

		self.cuslogradioButton = QtWidgets.QRadioButton(self.LoginPagegroupBox)
		self.cuslogradioButton.setGeometry(QtCore.QRect(110, 160, 131, 26))
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(13)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.cuslogradioButton.setFont(font)
		self.cuslogradioButton.setStyleSheet("background-color: rgb(238, 238, 236);")
		self.cuslogradioButton.setObjectName("cuslogradioButton")

		self.cuslogradioButton.clicked.connect(self.ButtonState)

		self.supplierloginBox = QtWidgets.QGroupBox(self.LoginPagegroupBox)
		self.supplierloginBox.setGeometry(QtCore.QRect(360, 190, 301, 251))
		self.supplierloginBox.setTitle("")
		self.supplierloginBox.setObjectName("supplierloginBox")

		self.supplierloginBox.setEnabled(False)

		self.suploginbutton = QtWidgets.QPushButton(self.supplierloginBox)
		self.suploginbutton.setGeometry(QtCore.QRect(100, 150, 83, 28))
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(12)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.suploginbutton.setFont(font)
		self.suploginbutton.setObjectName("suploginbutton")

		self.suploginbutton.clicked.connect(self.check2)

		self.suppasslabel = QtWidgets.QLabel(self.supplierloginBox)
		self.suppasslabel.setGeometry(QtCore.QRect(10, 110, 101, 20))
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(12)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.suppasslabel.setFont(font)
		self.suppasslabel.setObjectName("suppasslabel")
		self.suppassline = QtWidgets.QLineEdit(self.supplierloginBox)
		self.suppassline.setGeometry(QtCore.QRect(140, 110, 113, 21))
		self.suppassline.setEchoMode(QtWidgets.QLineEdit.Password)
		self.suppassline.setObjectName("suppassline")
		self.supidloginlabel = QtWidgets.QLabel(self.supplierloginBox)
		self.supidloginlabel.setGeometry(QtCore.QRect(10, 80, 121, 20))
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(12)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.supidloginlabel.setFont(font)
		self.supidloginlabel.setObjectName("supidloginlabel")
		self.supidloginline = QtWidgets.QLineEdit(self.supplierloginBox)
		self.supidloginline.setGeometry(QtCore.QRect(140, 80, 113, 21))
		self.supidloginline.setObjectName("supidloginline")
		self.displayloginlabel2 = QtWidgets.QLabel(self.supplierloginBox)
		self.displayloginlabel2.setGeometry(QtCore.QRect(11, 190, 261, 20))
		self.displayloginlabel2.setText("")
		self.displayloginlabel2.setObjectName("displayloginlabel2")
		self.customerlogBox = QtWidgets.QGroupBox(self.LoginPagegroupBox)
		self.customerlogBox.setGeometry(QtCore.QRect(40, 190, 311, 251))
		self.customerlogBox.setTitle("")
		self.customerlogBox.setObjectName("customerlogBox")

		self.customerlogBox.setEnabled(False)

		self.cusloginbutton = QtWidgets.QPushButton(self.customerlogBox)
		self.cusloginbutton.setGeometry(QtCore.QRect(100, 150, 83, 28))
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(12)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.cusloginbutton.setFont(font)
		self.cusloginbutton.setObjectName("cusloginbutton")

		self.cusloginbutton.clicked.connect(self.check1)

		self.cusidlogline = QtWidgets.QLineEdit(self.customerlogBox)
		self.cusidlogline.setGeometry(QtCore.QRect(150, 80, 113, 21))
		self.cusidlogline.setObjectName("cusidlogline")
		self.cusidloglabel = QtWidgets.QLabel(self.customerlogBox)
		self.cusidloglabel.setGeometry(QtCore.QRect(10, 80, 131, 20))
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(12)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.cusidloglabel.setFont(font)
		self.cusidloglabel.setObjectName("cusidloglabel")
		self.cuspassline = QtWidgets.QLineEdit(self.customerlogBox)
		self.cuspassline.setGeometry(QtCore.QRect(150, 110, 113, 21))
		self.cuspassline.setEchoMode(QtWidgets.QLineEdit.Password)
		self.cuspassline.setObjectName("cuspassline")
		self.cuspasswordlabel = QtWidgets.QLabel(self.customerlogBox)
		self.cuspasswordlabel.setGeometry(QtCore.QRect(10, 110, 101, 20))
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(12)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.cuspasswordlabel.setFont(font)
		self.cuspasswordlabel.setObjectName("cuspasswordlabel")
		self.displayloginlabel1 = QtWidgets.QLabel(self.customerlogBox)
		self.displayloginlabel1.setGeometry(QtCore.QRect(10, 190, 271, 20))
		self.displayloginlabel1.setText("")
		self.displayloginlabel1.setObjectName("displayloginlabel1")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 22))
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
		self.textEditlogin.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:6pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:16pt; font-weight:600; font-style:italic;\">Login Details</span></p></body></html>"))
		self.suplogradioButton.setText(_translate("MainWindow", "Suppliers"))
		self.cuslogradioButton.setText(_translate("MainWindow", "Customers"))
		self.suploginbutton.setText(_translate("MainWindow", "Login"))
		self.suppasslabel.setText(_translate("MainWindow", "Password"))
		self.supidloginlabel.setText(_translate("MainWindow", "SupplierID"))
		self.cusloginbutton.setText(_translate("MainWindow", "Login"))
		self.cusidloglabel.setText(_translate("MainWindow", "CustomerID"))
		self.cuspasswordlabel.setText(_translate("MainWindow", "Password"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_LoginWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

