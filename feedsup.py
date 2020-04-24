
from PyQt5 import QtCore, QtGui, QtWidgets

import MySQLdb as mdb

class Ui_SupFeedback(object):

	def Retrivepdtdetails(self):

		self.tablesupfeed.setEnabled(False)
		
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur=conn.cursor()
			cur.execute("select sup_id from Suppliers where login=1")
			result=cur.fetchone()[0]
			
			cur.execute("select pdt_id, product_name from ProductDetails where sup_id = "+str(result))
			result=cur.fetchall()
			self.tablepdtfeed.setRowCount(0)
			
			for rcount, row in enumerate(result):
				self.tablepdtfeed.insertRow(rcount)
				for ccount, data in enumerate(row):
					self.tablepdtfeed.setItem(rcount,ccount,QtWidgets.QTableWidgetItem(str(data)))

			self.tablesupfeed.setRowCount(0)
	
	def displayfeedpdtid(self):
		itemindex = self.tablepdtfeed.currentRow()
		if itemindex==-1:
			self.disfeedpdtid.setText("Select")
		else: 
			item = self.tablepdtfeed.item(itemindex,0).text()
			
			self.disfeedpdtid.setText(item)

	def displayfeedback(self):

		self.tablesupfeed.setEnabled(True)

		pdtid=self.disfeedpdtid.text()
		
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			
			if str(pdtid)=="Select" or str(pdtid)=="":
				pdtid=self.disfeedpdtid.text()
			else:
				cur=conn.cursor()
				cur.execute("select sup_id from Suppliers where login=1")
				resultsup=cur.fetchone()[0]
				
				cur.execute("select rating, description from Feedbacks f, ProductDetails s where s.pdt_id=f.pdt_id and s.pdt_id="+str(pdtid)+" and sup_id="+str(resultsup))
				
				result=cur.fetchall()
				resultcount=cur.rowcount
				
				self.tablesupfeed.setRowCount(0)
			
				for rcount, row in enumerate(result):
					self.tablesupfeed.insertRow(rcount)
					for ccount, data in enumerate(row):
						self.tablesupfeed.setItem(rcount,ccount,QtWidgets.QTableWidgetItem(str(data)))

	def setupUi(self, SupFeedback):
		SupFeedback.setObjectName("SupFeedback")
		SupFeedback.resize(633, 531)
		self.centralwidget = QtWidgets.QWidget(SupFeedback)
		self.centralwidget.setObjectName("centralwidget")
		self.tablesupfeed = QtWidgets.QTableWidget(self.centralwidget)
		self.tablesupfeed.setGeometry(QtCore.QRect(200, 190, 281, 241))
		self.tablesupfeed.setRowCount(7)
		self.tablesupfeed.setColumnCount(2)
		self.tablesupfeed.setObjectName("tablesupfeed")
		item = QtWidgets.QTableWidgetItem()
		self.tablesupfeed.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tablesupfeed.setHorizontalHeaderItem(1, item)
		self.tablesupfeed.horizontalHeader().setDefaultSectionSize(125)
		self.tablesupfeed.horizontalHeader().setMinimumSectionSize(30)

		self.tablesupfeed.setEnabled(False)

		self.seeFeedbutton = QtWidgets.QPushButton(self.centralwidget)
		self.seeFeedbutton.setGeometry(QtCore.QRect(430, 150, 111, 25))
		self.seeFeedbutton.setObjectName("seeFeedbutton")

		self.seeFeedbutton.clicked.connect(self.displayfeedback)

		# self.feedsupbackbutton = QtWidgets.QPushButton(self.centralwidget)
		# self.feedsupbackbutton.setGeometry(QtCore.QRect(80, 450, 89, 25))
		# self.feedsupbackbutton.setObjectName("feedsupbackbutton")
		self.labelfeedpdt = QtWidgets.QLabel(self.centralwidget)
		self.labelfeedpdt.setGeometry(QtCore.QRect(350, 60, 121, 17))
		self.labelfeedpdt.setObjectName("labelfeedpdt")
		self.disfeedpdtid = QtWidgets.QLabel(self.centralwidget)
		self.disfeedpdtid.setGeometry(QtCore.QRect(470, 60, 131, 17))
		self.disfeedpdtid.setText("")
		self.disfeedpdtid.setObjectName("disfeedpdtid")
		self.tablepdtfeed = QtWidgets.QTableWidget(self.centralwidget)
		self.tablepdtfeed.setGeometry(QtCore.QRect(110, 20, 221, 151))
		self.tablepdtfeed.setRowCount(4)
		self.tablepdtfeed.setColumnCount(2)
		self.tablepdtfeed.setObjectName("tablepdtfeed")
		item = QtWidgets.QTableWidgetItem()
		self.tablepdtfeed.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tablepdtfeed.setHorizontalHeaderItem(1, item)
		self.disfeedbutton = QtWidgets.QPushButton(self.centralwidget)
		self.disfeedbutton.setGeometry(QtCore.QRect(10, 50, 89, 25))
		self.disfeedbutton.setObjectName("disfeedbutton")

		self.disfeedbutton.clicked.connect(self.Retrivepdtdetails)

		self.selectfeedButton = QtWidgets.QPushButton(self.centralwidget)
		self.selectfeedButton.setGeometry(QtCore.QRect(350, 30, 89, 20))
		self.selectfeedButton.setObjectName("selectfeedButton")

		self.selectfeedButton.clicked.connect(self.displayfeedpdtid)

		SupFeedback.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(SupFeedback)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 22))
		self.menubar.setObjectName("menubar")
		SupFeedback.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(SupFeedback)
		self.statusbar.setObjectName("statusbar")
		SupFeedback.setStatusBar(self.statusbar)

		self.retranslateUi(SupFeedback)
		QtCore.QMetaObject.connectSlotsByName(SupFeedback)

	def retranslateUi(self, SupFeedback):
		_translate = QtCore.QCoreApplication.translate
		SupFeedback.setWindowTitle(_translate("SupFeedback", "SupFeedback"))
		item = self.tablesupfeed.horizontalHeaderItem(0)
		item.setText(_translate("SupFeedback", "Rating"))
		item = self.tablesupfeed.horizontalHeaderItem(1)
		item.setText(_translate("SupFeedback", "Description"))
		self.seeFeedbutton.setText(_translate("SupFeedback", "See Feedback"))
		#self.feedsupbackbutton.setText(_translate("SupFeedback", "Back"))
		self.labelfeedpdt.setText(_translate("SupFeedback", "ProductId"))
		item = self.tablepdtfeed.horizontalHeaderItem(0)
		item.setText(_translate("SupFeedback", "ProductId"))
		item = self.tablepdtfeed.horizontalHeaderItem(1)
		item.setText(_translate("SupFeedback", "ProductName"))
		self.disfeedbutton.setText(_translate("SupFeedback", "Display"))
		self.selectfeedButton.setText(_translate("SupFeedback", "Select"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	SupFeedback = QtWidgets.QMainWindow()
	ui = Ui_SupFeedback()
	ui.setupUi(SupFeedback)
	SupFeedback.show()
	sys.exit(app.exec_())

