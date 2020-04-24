
from PyQt5 import QtCore, QtGui, QtWidgets


import MySQLdb as mdb

class Ui_Suppliers(object):

	def LoadData(self):
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur=conn.cursor()
			cur.execute("select sup_id from Suppliers where login=1")
			result=cur.fetchone()[0]
			
			name = self.lineEditaddprod.text()
			avail= self.lineEditaddavail.text()
			category = self.lineEditaddcat.text()
			price= self.lineEditaddprice.text()
			
			i=0
			fl=False
			for char in str(avail):
				flag = char.isdigit()
				if flag==True:
					i=i+1
			if i==len(str(avail)):
				fl=True

			i=0
			fl2=False
			for char in str(price):
				flag = char.isdigit()
				if flag==True:
					i=i+1
			if i==len(str(price)):
				fl2=True

			#print(fl)

			if str(name)=="" or str(avail)=="" or str(category)=="" or str(price)=="" or fl==False or fl2==False or len(str(name))>25:
				self.blanklabel.setText("Please enter Appropriately")
			else:
				self.blanklabel.setText("")
				cur.execute("insert into ProductDetails(product_name,price,category_name,availability,sup_id) values('"+name+"',"+str(price)+",'"+category+"',"+str(avail)+","+str(result)+")")
				cur.execute("select max(pdt_id) from ProductDetails")
				result=cur.fetchone()[0]
				self.pdtidDislabel.setText(str(result))
			

	def ButtonState(self):
		if self.radioButtonadd.isChecked() ==True:
			self.groupBoxrem.setEnabled(False)
			self.groupBoxadd.show()
			self.groupBoxrem.hide()
			self.groupBoxadd.setEnabled(True)
		if self.radioButtonremove.isChecked()==True:
			self.groupBoxadd.setEnabled(False)
			self.groupBoxrem.show()
			self.groupBoxadd.hide()
			self.groupBoxrem.setEnabled(True)
		self.Retrive

	def Retrive(self):
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur=conn.cursor()
			cur.execute("select sup_id from Suppliers where login=1")
			result=cur.fetchone()[0]
			
			cur.execute("select pdt_id, product_name from ProductDetails where sup_id = "+str(result))
			result=cur.fetchall()
			self.tablepdtrem.setRowCount(0)
			
			for rcount, row in enumerate(result):
				self.tablepdtrem.insertRow(rcount)
				for ccount, data in enumerate(row):
					self.tablepdtrem.setItem(rcount,ccount,QtWidgets.QTableWidgetItem(str(data)))
	
	def displaypdtid(self):
		itemindex = self.tablepdtrem.currentRow()
		if itemindex==-1:
			self.pdtiddisrem.setText("Select")
		else: 
			item = self.tablepdtrem.item(itemindex,0).text()
			
			self.pdtiddisrem.setText(item)

	def RemoveData(self):
		
		pdid=self.pdtiddisrem.text()
		if str(pdid)!="Select":
			conn= mdb.connect("localhost","onshop","mysql","onlineshop")
			with conn:
				cur=conn.cursor()
				cur.execute("delete from ProductDetails where pdt_id = "+str(pdid))
				
				cur.execute("select sup_id from Suppliers where login=1")
				result=cur.fetchone()[0]
			
				cur.execute("select pdt_id, product_name from ProductDetails where sup_id = "+str(result))
				result=cur.fetchall()
				self.tablepdtrem.setRowCount(0)
				
				for rcount, row in enumerate(result):
					self.tablepdtrem.insertRow(rcount)
					for ccount, data in enumerate(row):
						self.tablepdtrem.setItem(rcount,ccount,QtWidgets.QTableWidgetItem(str(data)))


	
	# def Return(self):
	# 	Suppliers.hide()
	

	def setupUi(self, Suppliers):
		Suppliers.setObjectName("Suppliers")
		Suppliers.setEnabled(True)
		Suppliers.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(Suppliers)
		self.centralwidget.setObjectName("centralwidget")
		self.groupBoxselect = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBoxselect.setGeometry(QtCore.QRect(40, 30, 171, 80))
		self.groupBoxselect.setObjectName("groupBoxselect")
		self.radioButtonadd = QtWidgets.QRadioButton(self.groupBoxselect)
		self.radioButtonadd.setEnabled(True)
		self.radioButtonadd.setGeometry(QtCore.QRect(0, 20, 112, 23))
		self.radioButtonadd.setObjectName("radioButtonadd")
		self.radioButtonremove = QtWidgets.QRadioButton(self.groupBoxselect)
		self.radioButtonremove.setGeometry(QtCore.QRect(0, 50, 151, 20))
		self.radioButtonremove.setObjectName("radioButtonremove")
		self.groupBoxadd = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBoxadd.setEnabled(True)
		self.groupBoxadd.setGeometry(QtCore.QRect(150, 110, 571, 181))
		self.groupBoxadd.setObjectName("groupBoxadd")

		self.groupBoxadd.setEnabled(False)
		self.groupBoxadd.hide()

		self.lineEditaddprod = QtWidgets.QLineEdit(self.groupBoxadd)
		self.lineEditaddprod.setGeometry(QtCore.QRect(180, 30, 351, 25))
		self.lineEditaddprod.setObjectName("lineEditaddprod")

		self.lineEditaddprod.setMaxLength(25)

		self.labeladdpdtname = QtWidgets.QLabel(self.groupBoxadd)
		self.labeladdpdtname.setGeometry(QtCore.QRect(10, 30, 151, 17))
		self.labeladdpdtname.setObjectName("labeladdpdtname")
		self.labeladdavail = QtWidgets.QLabel(self.groupBoxadd)
		self.labeladdavail.setGeometry(QtCore.QRect(10, 70, 131, 17))
		self.labeladdavail.setObjectName("labeladdavail")
		self.lineEditaddavail = QtWidgets.QLineEdit(self.groupBoxadd)
		self.lineEditaddavail.setGeometry(QtCore.QRect(180, 70, 113, 25))
		self.lineEditaddavail.setObjectName("lineEditaddavail")
		self.addpdtbutton = QtWidgets.QPushButton(self.groupBoxadd)
		self.addpdtbutton.setGeometry(QtCore.QRect(190, 150, 101, 25))
		self.addpdtbutton.setObjectName("addpdtbutton")

		self.addpdtbutton.clicked.connect(self.LoadData)

		self.pdtidaddlabel = QtWidgets.QLabel(self.groupBoxadd)
		self.pdtidaddlabel.setGeometry(QtCore.QRect(350, 150, 101, 20))
		self.pdtidaddlabel.setObjectName("pdtidaddlabel")
		self.pdtidDislabel = QtWidgets.QLabel(self.groupBoxadd)
		self.pdtidDislabel.setGeometry(QtCore.QRect(450, 150, 67, 17))
		self.pdtidDislabel.setText("")
		self.pdtidDislabel.setObjectName("pdtidDislabel")
		self.clearaddbutton = QtWidgets.QPushButton(self.groupBoxadd)
		self.clearaddbutton.setGeometry(QtCore.QRect(30, 150, 89, 25))
		self.clearaddbutton.setObjectName("clearaddbutton")
		self.labeladdprice = QtWidgets.QLabel(self.groupBoxadd)
		self.labeladdprice.setGeometry(QtCore.QRect(10, 110, 121, 17))
		self.labeladdprice.setObjectName("labeladdprice")
		self.lineEditaddprice = QtWidgets.QLineEdit(self.groupBoxadd)
		self.lineEditaddprice.setGeometry(QtCore.QRect(180, 110, 113, 25))
		self.lineEditaddprice.setObjectName("lineEditaddprice")
		self.labeladdcat = QtWidgets.QLabel(self.groupBoxadd)
		self.labeladdcat.setGeometry(QtCore.QRect(320, 110, 67, 17))
		self.labeladdcat.setObjectName("labeladdcat")
		self.lineEditaddcat = QtWidgets.QLineEdit(self.groupBoxadd)
		self.lineEditaddcat.setGeometry(QtCore.QRect(420, 110, 113, 25))
		self.lineEditaddcat.setObjectName("lineEditaddcat")

		self.blanklabel = QtWidgets.QLabel(self.groupBoxadd)
		self.blanklabel.setGeometry(QtCore.QRect(330, 70, 201, 17))
		self.blanklabel.setText("")
		self.blanklabel.setObjectName("blanklabel")
		self.groupBoxrem = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBoxrem.setGeometry(QtCore.QRect(150, 300, 571, 211))
		self.groupBoxrem.setObjectName("groupBoxrem")

		self.groupBoxrem.setEnabled(False)
		self.groupBoxrem.hide()

		self.rempdtbutton = QtWidgets.QPushButton(self.groupBoxrem)
		self.rempdtbutton.setGeometry(QtCore.QRect(440, 150, 131, 25))
		self.rempdtbutton.setObjectName("rempdtbutton")

		self.rempdtbutton.clicked.connect(self.RemoveData)

		self.pdtidremlabel = QtWidgets.QLabel(self.groupBoxrem)
		self.pdtidremlabel.setGeometry(QtCore.QRect(340, 80, 81, 17))
		self.pdtidremlabel.setObjectName("pdtidremlabel")
		self.clearrembutton = QtWidgets.QPushButton(self.groupBoxrem)
		self.clearrembutton.setGeometry(QtCore.QRect(340, 150, 89, 25))
		self.clearrembutton.setObjectName("clearrembutton")
		self.tablepdtrem = QtWidgets.QTableWidget(self.groupBoxrem)
		self.tablepdtrem.setGeometry(QtCore.QRect(110, 30, 221, 151))
		self.tablepdtrem.setRowCount(4)
		self.tablepdtrem.setColumnCount(2)
		self.tablepdtrem.setObjectName("tablepdtrem")
		item = QtWidgets.QTableWidgetItem()
		self.tablepdtrem.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tablepdtrem.setHorizontalHeaderItem(1, item)
		self.pdtiddisrem = QtWidgets.QLabel(self.groupBoxrem)
		self.pdtiddisrem.setGeometry(QtCore.QRect(450, 80, 67, 17))
		self.pdtiddisrem.setText("")
		self.pdtiddisrem.setObjectName("pdtiddisrem")
		self.disrembutton = QtWidgets.QPushButton(self.groupBoxrem)
		self.disrembutton.setGeometry(QtCore.QRect(20, 80, 89, 25))
		self.disrembutton.setObjectName("disrembutton")

		self.disrembutton.clicked.connect(self.Retrive)

		self.selectpdtButton = QtWidgets.QPushButton(self.groupBoxrem)
		self.selectpdtButton.setGeometry(QtCore.QRect(340, 40, 89, 25))
		self.selectpdtButton.setObjectName("selectpdtButton")

		self.selectpdtButton.clicked.connect(self.displaypdtid)

		# self.addremokbutton = QtWidgets.QPushButton(self.centralwidget)
		# self.addremokbutton.setGeometry(QtCore.QRect(520, 510, 89, 25))
		# self.addremokbutton.setObjectName("addremokbutton")



		# self.canceladdrembutton = QtWidgets.QPushButton(self.centralwidget)
		# self.canceladdrembutton.setGeometry(QtCore.QRect(390, 510, 89, 25))
		# self.canceladdrembutton.setObjectName("canceladdrembutton")

		# self.canceladdrembutton.clicked.connect(self.Return)

		self.selectaddrembutton = QtWidgets.QPushButton(self.centralwidget)
		self.selectaddrembutton.setGeometry(QtCore.QRect(240, 70, 89, 25))
		self.selectaddrembutton.setObjectName("selectaddrembutton")

		self.selectaddrembutton.clicked.connect(self.ButtonState)

		Suppliers.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(Suppliers)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
		self.menubar.setObjectName("menubar")
		Suppliers.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(Suppliers)
		self.statusbar.setObjectName("statusbar")
		Suppliers.setStatusBar(self.statusbar)

		self.retranslateUi(Suppliers)
		self.clearaddbutton.clicked.connect(self.lineEditaddavail.clear)
		self.clearaddbutton.clicked.connect(self.lineEditaddprod.clear)
		self.clearaddbutton.clicked.connect(self.lineEditaddprice.clear)
		self.clearaddbutton.clicked.connect(self.lineEditaddcat.clear)
		self.clearrembutton.clicked.connect(self.tablepdtrem.clear)
		self.clearaddbutton.clicked.connect(self.pdtidDislabel.clear)
		QtCore.QMetaObject.connectSlotsByName(Suppliers)

	def retranslateUi(self, Suppliers):
		_translate = QtCore.QCoreApplication.translate
		Suppliers.setWindowTitle(_translate("Suppliers", "Suppliers"))
		self.groupBoxselect.setTitle(_translate("Suppliers", "Select your Choice"))
		self.radioButtonadd.setText(_translate("Suppliers", "Add Product"))
		self.radioButtonremove.setText(_translate("Suppliers", "Remove Product"))
		self.groupBoxadd.setTitle(_translate("Suppliers", "Add Product"))
		self.labeladdpdtname.setText(_translate("Suppliers", "Enter Product Name"))
		self.labeladdavail.setText(_translate("Suppliers", "Enter Availability"))
		self.addpdtbutton.setText(_translate("Suppliers", "Add Product"))
		self.pdtidaddlabel.setText(_translate("Suppliers", "Product Id:"))
		self.clearaddbutton.setText(_translate("Suppliers", "Clear"))
		self.labeladdprice.setText(_translate("Suppliers", "Price Per Quanity"))
		self.labeladdcat.setText(_translate("Suppliers", "Category"))
		self.groupBoxrem.setTitle(_translate("Suppliers", "Remove Product"))
		self.rempdtbutton.setText(_translate("Suppliers", "Remove Product"))
		self.pdtidremlabel.setText(_translate("Suppliers", "Product Id:"))
		self.clearrembutton.setText(_translate("Suppliers", "Clear"))
		item = self.tablepdtrem.horizontalHeaderItem(0)
		item.setText(_translate("Suppliers", "ProductId"))
		item = self.tablepdtrem.horizontalHeaderItem(1)
		item.setText(_translate("Suppliers", "ProductName"))
		self.disrembutton.setText(_translate("Suppliers", "Display"))
		self.selectpdtButton.setText(_translate("Suppliers", "Select"))
		#self.addremokbutton.setText(_translate("Suppliers", "Ok"))
		#self.canceladdrembutton.setText(_translate("Suppliers", "Cancel"))
		self.selectaddrembutton.setText(_translate("Suppliers", "Select"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Suppliers = QtWidgets.QMainWindow()
	ui = Ui_Suppliers()
	ui.setupUi(Suppliers)
	Suppliers.show()
	sys.exit(app.exec_())

