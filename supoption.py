
from PyQt5 import QtCore, QtGui, QtWidgets

from supaddrem import Ui_Suppliers
from feedsup import Ui_SupFeedback
from shipsup import Ui_Shipsup

import MySQLdb as mdb

class Ui_SupOption(object):

	
	def openAdd(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_Suppliers()
		self.ui.setupUi(self.window)
		self.window.show()
	
	def openShip(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_Shipsup()
		self.ui.setupUi(self.window)
		self.window.show()
	
	def logout(self):
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur=conn.cursor()
			cur.execute("update Suppliers set login=0 where login=1")

			self.addremoptbutton.setText("LoggedOut")
			self.shipoptbutton.setText("LoggedOut")
			self.supfeedoptbutton.setText("LoggedOut")

			self.addremoptbutton.setEnabled(False)
			self.shipoptbutton.setEnabled(False)
			self.supfeedoptbutton.setEnabled(False)
		
	
	def feedsup(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_SupFeedback()
		self.ui.setupUi(self.window)
		self.window.show()
	
	def setupUi(self, SupOption):
		SupOption.setObjectName("SupOption")
		SupOption.resize(338, 376)
		self.centralwidget = QtWidgets.QWidget(SupOption)
		self.centralwidget.setObjectName("centralwidget")
		self.addremoptbutton = QtWidgets.QPushButton(self.centralwidget)
		self.addremoptbutton.setGeometry(QtCore.QRect(90, 90, 161, 25))
		self.addremoptbutton.setObjectName("addremoptbutton")
		
		self.addremoptbutton.clicked.connect(self.openAdd)
		
		self.shipoptbutton = QtWidgets.QPushButton(self.centralwidget)
		self.shipoptbutton.setGeometry(QtCore.QRect(90, 140, 161, 25))
		self.shipoptbutton.setObjectName("shipoptbutton")
		
		self.shipoptbutton.clicked.connect(self.openShip)
		
		self.suplogoutbutton = QtWidgets.QPushButton(self.centralwidget)
		self.suplogoutbutton.setGeometry(QtCore.QRect(130, 270, 89, 25))
		self.suplogoutbutton.setObjectName("suplogoutbutton")
		
		self.suplogoutbutton.clicked.connect(self.logout)
		
		self.supfeedoptbutton = QtWidgets.QPushButton(self.centralwidget)
		self.supfeedoptbutton.setGeometry(QtCore.QRect(98, 190, 151, 25))
		self.supfeedoptbutton.setObjectName("supfeedoptbutton")
		
		self.supfeedoptbutton.clicked.connect(self.feedsup)
		
		SupOption.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(SupOption)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 338, 22))
		self.menubar.setObjectName("menubar")
		SupOption.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(SupOption)
		self.statusbar.setObjectName("statusbar")
		SupOption.setStatusBar(self.statusbar)

		self.retranslateUi(SupOption)
		QtCore.QMetaObject.connectSlotsByName(SupOption)

	def retranslateUi(self, SupOption):
		_translate = QtCore.QCoreApplication.translate
		SupOption.setWindowTitle(_translate("SupOption", "SupOption"))
		self.addremoptbutton.setText(_translate("SupOption", "Add/Remove"))
		self.shipoptbutton.setText(_translate("SupOption", "Shipment"))
		self.suplogoutbutton.setText(_translate("SupOption", "Log Out"))
		self.supfeedoptbutton.setText(_translate("SupOption", "See Feedbacks"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	SupOption = QtWidgets.QMainWindow()
	ui = Ui_SupOption()
	ui.setupUi(SupOption)
	SupOption.show()
	sys.exit(app.exec_())

