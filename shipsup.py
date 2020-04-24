
from PyQt5 import QtCore, QtGui, QtWidgets

import MySQLdb as mdb

class Ui_Shipsup(object):

	def shipdisplay(self):
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur=conn.cursor()
			cur.execute("select sup_id from Suppliers where login=1")
			result=cur.fetchone()[0]
			
			cur.execute("select ship_id, s.ord_no, tracking, ship_add, date from ShippingDetails s, OrderDetails o, ProductDetails p where o.ord_no = s.ord_no and o.pdt_id=p.pdt_id and sup_id = "+str(result))
			result=cur.fetchall()
			self.tableShipSup.setRowCount(0)
			
			for rcount, row in enumerate(result):
				self.tableShipSup.insertRow(rcount)
				for ccount, data in enumerate(row):
					self.tableShipSup.setItem(rcount,ccount,QtWidgets.QTableWidgetItem(str(data)))

			self.tableOrdersup.setRowCount(0)

	def displayshipid(self):
		itemindex = self.tableShipSup.currentRow()
		if itemindex==-1:
			self.labeldhipdissup.setText("Select Please")
			self.labelOrdDissup.setText("Select Please")
		else: 
			item = self.tableShipSup.item(itemindex,0).text()
			item2 = self.tableShipSup.item(itemindex,1).text()
			self.labeldhipdissup.setText(item)
			self.labelOrdDissup.setText(item2)

	def shiporderdetails(self):
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur=conn.cursor()
			shid= self.labeldhipdissup.text()
			
			if str(shid) == "Select Please" or str(shid)=="Updated" or str(shid)=="":
				shid=self.labeldhipdissup.text()
			else:
				cur.execute("select sup_id from Suppliers where login=1")
				result=cur.fetchone()[0]

				cur.execute("select o.pdt_id, qty from OrderDetails o, ProductDetails p, ShippingDetails s where p.pdt_id = o.pdt_id and s.ord_no = o.ord_no and sup_id = "+str(result)+" and ship_id = "+str(shid))
				results=cur.fetchall()
				self.tableOrdersup.setRowCount(0)
				
				for rcount, row in enumerate(results):
					self.tableOrdersup.insertRow(rcount)
					for ccount, data in enumerate(row):
						self.tableOrdersup.setItem(rcount,ccount,QtWidgets.QTableWidgetItem(str(data)))

	def enableUpdate(self):
		self.groupUpdate.setEnabled(True)

	def updatedetails(self):
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur=conn.cursor()
			shid= self.labeldhipdissup.text()
			ordno= self.labelOrdDissup.text()

			if str(shid)!="Select Please" or str(shid)!="Updated":
				shipadd=self.linesupshipdd.text()
				stat=self.lineStatship.text()
				cur.execute("update ShippingDetails set ship_add = '"+str(shipadd)+"' where ship_id ="+ str(shid)+" and ord_no = "+str(ordno))
				cur.execute("update ShippingDetails set tracking= '"+str(stat)+"' where ship_id ="+ str(shid)+" and ord_no = "+str(ordno))
				self.labeldhipdissup.setText("Updated")

				cur.execute("select sup_id from Suppliers where login=1")
				result=cur.fetchone()[0]
				cur.execute("select ship_id, s.ord_no, tracking, ship_add, date from ShippingDetails s, OrderDetails o, ProductDetails p where o.ord_no = s.ord_no and o.pdt_id=p.pdt_id and sup_id = "+str(result))
				result=cur.fetchall()
				self.tableShipSup.setRowCount(0)
				
				for rcount, row in enumerate(result):
					self.tableShipSup.insertRow(rcount)
					for ccount, data in enumerate(row):
						self.tableShipSup.setItem(rcount,ccount,QtWidgets.QTableWidgetItem(str(data)))

				self.tableOrdersup.setRowCount(0)

				self.groupUpdate.setEnabled(False)

	# def Return(self):
	# 	app.quit()

	def setupUi(self, Shipsup):
		Shipsup.setObjectName("Shipsup")
		Shipsup.resize(681, 515)
		self.centralwidget = QtWidgets.QWidget(Shipsup)
		self.centralwidget.setObjectName("centralwidget")
		self.displayShipbutton = QtWidgets.QPushButton(self.centralwidget)
		self.displayShipbutton.setGeometry(QtCore.QRect(10, 10, 89, 25))
		self.displayShipbutton.setObjectName("displayShipbutton")

		self.displayShipbutton.clicked.connect(self.shipdisplay)

		self.tableShipSup = QtWidgets.QTableWidget(self.centralwidget)
		self.tableShipSup.setGeometry(QtCore.QRect(30, 40, 531, 181))
		self.tableShipSup.setRowCount(5)
		self.tableShipSup.setColumnCount(5)
		self.tableShipSup.setObjectName("tableShipSup")
		item = QtWidgets.QTableWidgetItem()
		self.tableShipSup.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableShipSup.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableShipSup.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableShipSup.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableShipSup.setHorizontalHeaderItem(4, item)
		self.labelordnoship = QtWidgets.QLabel(self.centralwidget)
		self.labelordnoship.setGeometry(QtCore.QRect(110, 260, 81, 20))
		self.labelordnoship.setObjectName("labelordnoship")
		self.labelOrdDissup = QtWidgets.QLabel(self.centralwidget)
		self.labelOrdDissup.setGeometry(QtCore.QRect(200, 260, 141, 17))
		self.labelOrdDissup.setText("")
		self.labelOrdDissup.setObjectName("labelOrdDissup")
		self.detailsshipbutton = QtWidgets.QPushButton(self.centralwidget)
		self.detailsshipbutton.setGeometry(QtCore.QRect(390, 230, 89, 25))
		self.detailsshipbutton.setObjectName("detailsshipbutton")

		self.detailsshipbutton.clicked.connect(self.shiporderdetails)

		self.tableOrdersup = QtWidgets.QTableWidget(self.centralwidget)
		self.tableOrdersup.setGeometry(QtCore.QRect(400, 270, 221, 121))
		self.tableOrdersup.setRowCount(3)
		self.tableOrdersup.setColumnCount(2)
		self.tableOrdersup.setObjectName("tableOrdersup")
		item = QtWidgets.QTableWidgetItem()
		self.tableOrdersup.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableOrdersup.setHorizontalHeaderItem(1, item)
		# self.shipsupbackbutton = QtWidgets.QPushButton(self.centralwidget)
		# self.shipsupbackbutton.setGeometry(QtCore.QRect(440, 430, 89, 25))
		# self.shipsupbackbutton.setObjectName("shipsupbackbutton")

		# self.shipsupbackbutton.clicked.connect(self.Return)

		self.selectpdtButton = QtWidgets.QPushButton(self.centralwidget)
		self.selectpdtButton.setGeometry(QtCore.QRect(10, 230, 89, 21))
		self.selectpdtButton.setObjectName("selectpdtButton")

		self.selectpdtButton.clicked.connect(self.displayshipid)

		self.labelShipnosup = QtWidgets.QLabel(self.centralwidget)
		self.labelShipnosup.setGeometry(QtCore.QRect(110, 230, 67, 17))
		self.labelShipnosup.setObjectName("labelShipnosup")
		self.labeldhipdissup = QtWidgets.QLabel(self.centralwidget)
		self.labeldhipdissup.setGeometry(QtCore.QRect(200, 230, 141, 17))
		self.labeldhipdissup.setText("")
		self.labeldhipdissup.setObjectName("labeldhipdissup")
		self.shipupdateButton = QtWidgets.QPushButton(self.centralwidget)
		self.shipupdateButton.setGeometry(QtCore.QRect(20, 300, 89, 25))
		self.shipupdateButton.setObjectName("shipupdateButton")

		self.shipupdateButton.clicked.connect(self.enableUpdate)

		self.groupUpdate = QtWidgets.QGroupBox(self.centralwidget)
		self.groupUpdate.setGeometry(QtCore.QRect(70, 340, 321, 141))
		self.groupUpdate.setTitle("")
		self.groupUpdate.setObjectName("groupUpdate")

		self.groupUpdate.setEnabled(False)

		self.labelshipaddr = QtWidgets.QLabel(self.groupUpdate)
		self.labelshipaddr.setGeometry(QtCore.QRect(10, 30, 71, 17))
		self.labelshipaddr.setObjectName("labelshipaddr")
		self.lineStatship = QtWidgets.QLineEdit(self.groupUpdate)
		self.lineStatship.setGeometry(QtCore.QRect(90, 80, 113, 25))
		self.lineStatship.setObjectName("lineStatship")
		self.labelshipstat = QtWidgets.QLabel(self.groupUpdate)
		self.labelshipstat.setGeometry(QtCore.QRect(10, 80, 67, 17))
		self.labelshipstat.setObjectName("labelshipstat")
		self.shipUpokButton = QtWidgets.QPushButton(self.groupUpdate)
		self.shipUpokButton.setGeometry(QtCore.QRect(240, 80, 51, 25))
		self.shipUpokButton.setObjectName("shipUpokButton")

		self.shipUpokButton.clicked.connect(self.updatedetails)

		self.linesupshipdd = QtWidgets.QLineEdit(self.groupUpdate)
		self.linesupshipdd.setGeometry(QtCore.QRect(90, 30, 211, 25))
		self.linesupshipdd.setObjectName("linesupshipdd")
		Shipsup.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(Shipsup)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 22))
		self.menubar.setObjectName("menubar")
		Shipsup.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(Shipsup)
		self.statusbar.setObjectName("statusbar")
		Shipsup.setStatusBar(self.statusbar)

		self.retranslateUi(Shipsup)
		QtCore.QMetaObject.connectSlotsByName(Shipsup)

	def retranslateUi(self, Shipsup):
		_translate = QtCore.QCoreApplication.translate
		Shipsup.setWindowTitle(_translate("Shipsup", "ShipSup"))
		self.displayShipbutton.setText(_translate("Shipsup", "Display"))
		item = self.tableShipSup.horizontalHeaderItem(0)
		item.setText(_translate("Shipsup", "Ship_id"))
		item = self.tableShipSup.horizontalHeaderItem(1)
		item.setText(_translate("Shipsup", "Ord_no"))
		item = self.tableShipSup.horizontalHeaderItem(2)
		item.setText(_translate("Shipsup", "Status"))
		item = self.tableShipSup.horizontalHeaderItem(3)
		item.setText(_translate("Shipsup", "Ship_Address"))
		item = self.tableShipSup.horizontalHeaderItem(4)
		item.setText(_translate("Shipsup", "Ship_date"))
		self.labelordnoship.setText(_translate("Shipsup", "Order No:"))
		self.detailsshipbutton.setText(_translate("Shipsup", "Details"))
		item = self.tableOrdersup.horizontalHeaderItem(0)
		item.setText(_translate("Shipsup", "Pdt_Id"))
		item = self.tableOrdersup.horizontalHeaderItem(1)
		item.setText(_translate("Shipsup", "Quantity"))
		#self.shipsupbackbutton.setText(_translate("Shipsup", "Back"))
		self.selectpdtButton.setText(_translate("Shipsup", "Select"))
		self.labelShipnosup.setText(_translate("Shipsup", "Ship Id:"))
		self.shipupdateButton.setText(_translate("Shipsup", "Update?"))
		self.labelshipaddr.setText(_translate("Shipsup", "Ship Addr:"))
		self.labelshipstat.setText(_translate("Shipsup", "Status:"))
		self.shipUpokButton.setText(_translate("Shipsup", "Ok"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Shipsup = QtWidgets.QMainWindow()
	ui = Ui_Shipsup()
	ui.setupUi(Shipsup)
	Shipsup.show()
	sys.exit(app.exec_())

