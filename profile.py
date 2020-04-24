
from PyQt5 import QtCore, QtGui, QtWidgets

import MySQLdb as mdb
from Orders import Ui_MainWindow5 

class Ui_profile(object):

	def OpenData(self):
		conn=mdb.connect("localhost","onshop","mysql","onlineshop")
		with conn:
			cur=conn.cursor()
			cur.execute("select customer_name , phone_no , customer_address from Customers where login = 1")
			result=cur.fetchall()

			self.mobnolineEdit.setEnabled(True)
			self.addrlineEdit.setEnabled(True)

			for rows in result:
				self.usernamelabel.setText(str(rows[0]))
				self.mobnolineEdit.setText(str(rows[1]))
				self.addrlineEdit.setText(str(rows[2]))


	def state(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_MainWindow5()
		self.ui.setupUi(self.window)
		self.window.show()


	def updateProfile(self):
		conn=mdb.connect("localhost","onshop","mysql","onlineshop")
		with conn:
			cur=conn.cursor()

			pno=self.mobnolineEdit.text()
			addr=self.addrlineEdit.text()
			cur.execute("update Customers set phone_no ='"+str(pno)+"' where login=1")
			cur.execute("update Customers set customer_address = '"+str(addr)+"' where login=1")

			self.addrlineEdit.setText("Updated")
			self.mobnolineEdit.setText("Updated")
			self.mobnolineEdit.setEnabled(False)
			self.addrlineEdit.setEnabled(False)
			self.orderpushButton.setEnabled(False)


	def changepassword(self):
		self.okpushButton.show()
		self.newpasslineedit.show()
		self.newpasslabel.show()

	def updatepassword(self):
		conn=mdb.connect("localhost","onshop","mysql","onlineshop")
		with conn:
			cur=conn.cursor()
			pas=self.newpasslineedit.text()

			cur.execute("update Customers set password ='"+str(pas)+"' where login=1")

	def logout(self):
		conn=mdb.connect("localhost","onshop","mysql","onlineshop")
		with conn:
			cur=conn.cursor()
			cur.execute("update Customers set login = 0 where login=1")

			self.newpasslineedit.hide()
			self.addrlineEdit.setText("LoggedOut")
			self.mobnolineEdit.setText("LoggedOut")
			self.mobnolineEdit.setEnabled(False)
			self.addrlineEdit.setEnabled(False)
			self.updatepushButton.setEnabled(False)
			self.okpushButton.setEnabled(False)
			self.changepasspushButton_2.setEnabled(False)
			#app.quit()
			#profile.hide()

	def setupUi(self, profile):
		profile.setObjectName("profile")
		profile.resize(572, 492)
		self.centralwidget = QtWidgets.QWidget(profile)
		self.centralwidget.setObjectName("centralwidget")
		self.mobnolineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.mobnolineEdit.setGeometry(QtCore.QRect(170, 190, 171, 20))
		self.mobnolineEdit.setReadOnly(False)
		self.mobnolineEdit.setObjectName("mobnolineEdit")
		self.mobilenolabel = QtWidgets.QLabel(self.centralwidget)
		self.mobilenolabel.setGeometry(QtCore.QRect(50, 190, 81, 21))
		font = QtGui.QFont()
		font.setFamily("Narkisim")
		font.setPointSize(11)
		self.mobilenolabel.setFont(font)
		self.mobilenolabel.setObjectName("mobilenolabel")
		self.addrlineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.addrlineEdit.setGeometry(QtCore.QRect(170, 230, 241, 20))
		self.addrlineEdit.setReadOnly(False)
		self.addrlineEdit.setObjectName("addrlineEdit")
		self.addrlabel = QtWidgets.QLabel(self.centralwidget)
		self.addrlabel.setGeometry(QtCore.QRect(50, 230, 81, 21))
		font = QtGui.QFont()
		font.setFamily("Narkisim")
		font.setPointSize(11)
		self.addrlabel.setFont(font)
		self.addrlabel.setObjectName("addrlabel")
		self.updatepushButton = QtWidgets.QPushButton(self.centralwidget)
		self.updatepushButton.setGeometry(QtCore.QRect(440, 220, 91, 31))
		self.updatepushButton.setObjectName("updatepushButton")

		self.updatepushButton.setEnabled(True)

		self.updatepushButton.clicked.connect(self.updateProfile)

		self.welcomelabel = QtWidgets.QLabel(self.centralwidget)
		self.welcomelabel.setGeometry(QtCore.QRect(200, 20, 181, 51))
		font = QtGui.QFont()
		font.setFamily("Narkisim")
		font.setPointSize(14)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.welcomelabel.setFont(font)
		self.welcomelabel.setAlignment(QtCore.Qt.AlignCenter)
		self.welcomelabel.setObjectName("welcomelabel")
		self.usernamelabel = QtWidgets.QLabel(self.centralwidget)
		self.usernamelabel.setGeometry(QtCore.QRect(160, 70, 261, 61))
		font = QtGui.QFont()
		font.setFamily("Narkisim")
		font.setPointSize(22)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.usernamelabel.setFont(font)
		self.usernamelabel.setText("")
		self.usernamelabel.setAlignment(QtCore.Qt.AlignCenter)
		self.usernamelabel.setObjectName("usernamelabel")
		self.changepasspushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.changepasspushButton_2.setGeometry(QtCore.QRect(50, 330, 131, 31))
		self.changepasspushButton_2.setObjectName("changepasspushButton_2")

		self.changepasspushButton_2.setEnabled(True)
		self.changepasspushButton_2.clicked.connect(self.changepassword)

		self.okpushButton = QtWidgets.QPushButton(self.centralwidget)
		self.okpushButton.setGeometry(QtCore.QRect(450, 360, 31, 31))
		self.okpushButton.setObjectName("okpushButton")

		self.okpushButton.setEnabled(True)
		self.okpushButton.hide()
		self.okpushButton.clicked.connect(self.updatepassword)

		self.newpasslineedit = QtWidgets.QLineEdit(self.centralwidget)
		self.newpasslineedit.setGeometry(QtCore.QRect(180, 370, 241, 20))
		self.newpasslineedit.setReadOnly(False)
		self.newpasslineedit.setEchoMode(QtWidgets.QLineEdit.Password)
		self.newpasslineedit.setObjectName("newpasslineedit")

		self.newpasslineedit.hide()

		self.newpasslabel = QtWidgets.QLabel(self.centralwidget)
		self.newpasslabel.setGeometry(QtCore.QRect(50, 370, 111, 31))
		self.newpasslabel.setObjectName("newpasslabel")

		self.newpasslabel.hide()

		self.orderpushButton = QtWidgets.QPushButton(self.centralwidget)
		self.orderpushButton.setGeometry(QtCore.QRect(210, 270, 161, 41))
		font = QtGui.QFont()
		font.setFamily("Narkisim")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.orderpushButton.setFont(font)
		self.orderpushButton.setObjectName("orderpushButton")

		self.orderpushButton.clicked.connect(self.state)
		
		self.logoutpushButton = QtWidgets.QPushButton(self.centralwidget)
		self.logoutpushButton.setGeometry(QtCore.QRect(240, 400, 111, 41))
		font = QtGui.QFont()
		font.setFamily("Narkisim")
		font.setPointSize(12)
		self.logoutpushButton.setFont(font)
		self.logoutpushButton.setObjectName("logoutpushButton")

		self.logoutpushButton.clicked.connect(self.logout)

		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(50, 20, 121, 111))
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("../../../../../../Desktop/DBMS project/usericon.png"))
		self.label.setScaledContents(True)
		self.label.setObjectName("label")
		profile.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(profile)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 22))
		self.menubar.setObjectName("menubar")
		profile.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(profile)
		self.statusbar.setObjectName("statusbar")
		profile.setStatusBar(self.statusbar)

		self.retranslateUi(profile)
		QtCore.QMetaObject.connectSlotsByName(profile)

		self.OpenData()

	def retranslateUi(self, profile):
		_translate = QtCore.QCoreApplication.translate
		profile.setWindowTitle(_translate("profile", "MainWindow"))
		self.mobilenolabel.setText(_translate("profile", "Mobile No :"))
		self.addrlabel.setText(_translate("profile", "Address :"))
		self.updatepushButton.setText(_translate("profile", "Update "))
		self.welcomelabel.setText(_translate("profile", "WELCOME"))
		self.changepasspushButton_2.setText(_translate("profile", "Change Password"))
		self.okpushButton.setText(_translate("profile", ">"))
		self.newpasslabel.setText(_translate("profile", "New Password  :"))
		self.orderpushButton.setText(_translate("profile", "YOUR ORDERS"))
		self.logoutpushButton.setText(_translate("profile", "LOGOUT"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	profile = QtWidgets.QMainWindow()
	ui = Ui_profile()
	ui.setupUi(profile)
	profile.show()
	sys.exit(app.exec_())

