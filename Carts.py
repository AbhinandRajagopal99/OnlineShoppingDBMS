
from PyQt5 import QtCore, QtGui, QtWidgets

import MySQLdb as mdb

from Payment import Ui_MainWindow

class Ui_Cart(object):

	
	def openWindow(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.window)
		self.window.showMaximized()
	

	def LoadData(self):
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur=conn.cursor()
			cur.execute("select cus_id from Customers where login=1")
			result=cur.fetchone()[0]
			cur.execute("select c.ord_no, pdt_id, qty from OrderDetails o,Cart c where o.ord_no = c.ord_no and cus_id ="+str(result))
			result=cur.fetchall()
			self.tableWidget.setRowCount(0)
			for row_number,row_data in enumerate (result):
				self.tableWidget.insertRow(row_number)
				for column_number,data in enumerate(row_data):
					self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
			
			cur.close()

	def check(self):
		
		ord=self.lineEdit.text()
		pro=self.lineEdit_2.text()
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur=conn.cursor()
			cur.execute('select *from OrderDetails where ord_no="'+str(ord)+'" and pdt_id="'+str(pro)+'"')
			#cur.fetchone()[0]
			count=cur.rowcount
		if count==0:      
		#if str(ord)=="" or str(pro)=="":
			self.label_3.setText("Invalid")
		else:
			conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
			with conn:
			
				cur2=conn.cursor()
				pid=self.lineEdit_2.text()
				ordno=self.lineEdit.text()
				cur2.execute("delete from PaymentDetails where ord_no="+str(ordno))
				cur2.execute("delete from OrderStatus where ord_no ="+str(ordno))
				cur2.execute("delete from ShippingDetails where ord_no = "+str(ordno))
				cur2.execute("delete from OrderDetails where ord_no="+str(ordno))
				cur2.execute("delete from Cart where ord_no="+str(ordno))
				
				cur2.close()    
			self.LoadData()
			

	def setupUi(self, Cart):
		Cart.setObjectName("Cart")
		Cart.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(Cart)
		self.centralwidget.setObjectName("centralwidget")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(380, 50, 71, 31))
		font = QtGui.QFont()
		font.setFamily("DejaVu Sans")
		font.setPointSize(20)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.frame_2 = QtWidgets.QFrame(self.centralwidget)
		self.frame_2.setGeometry(QtCore.QRect(10, 130, 421, 321))
		self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame_2.setObjectName("frame_2")
		self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
		self.tableWidget.setGeometry(QtCore.QRect(50, 30, 321, 191))
		self.tableWidget.setMaximumSize(QtCore.QSize(321, 191))
		self.tableWidget.setSizeIncrement(QtCore.QSize(5, 5))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.tableWidget.setFont(font)
		self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tableWidget.setRowCount(5)
		self.tableWidget.setColumnCount(6)
		self.tableWidget.setObjectName("tableWidget")
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setItem(0, 3, item)
		self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_2.setGeometry(QtCore.QRect(130, 280, 151, 28))
		font = QtGui.QFont()
		font.setFamily("DejaVu Serif")
		font.setPointSize(12)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.pushButton_2.setFont(font)
		self.pushButton_2.setObjectName("pushButton_2")

		self.pushButton_2.clicked.connect(self.openWindow)

		self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
		self.pushButton_4.setGeometry(QtCore.QRect(170, 230, 71, 31))
		font = QtGui.QFont()
		font.setFamily("DejaVu Serif")
		font.setPointSize(12)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.pushButton_4.setFont(font)
		self.pushButton_4.setObjectName("pushButton_4")

		self.pushButton_4.clicked.connect(self.LoadData)

		self.frame = QtWidgets.QFrame(self.centralwidget)
		self.frame.setGeometry(QtCore.QRect(470, 160, 321, 211))
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.label = QtWidgets.QLabel(self.frame)
		self.label.setGeometry(QtCore.QRect(90, 10, 141, 20))
		font = QtGui.QFont()
		font.setFamily("Century Schoolbook L")
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.frame)
		self.label_2.setGeometry(QtCore.QRect(50, 50, 62, 20))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.frame)
		self.label_3.setGeometry(QtCore.QRect(50, 130, 62, 20))
		self.label_3.setText("")
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.frame)
		self.label_4.setGeometry(QtCore.QRect(50, 90, 71, 20))
		self.label_4.setObjectName("label_4")
		self.lineEdit = QtWidgets.QLineEdit(self.frame)
		self.lineEdit.setGeometry(QtCore.QRect(150, 50, 113, 28))
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
		self.lineEdit_2.setGeometry(QtCore.QRect(150, 90, 113, 28))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.pushButton = QtWidgets.QPushButton(self.frame)
		self.pushButton.setGeometry(QtCore.QRect(110, 170, 83, 28))
		font = QtGui.QFont()
		font.setFamily("DejaVu Math TeX Gyre")
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")

		self.pushButton.clicked.connect(self.check)

		Cart.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(Cart)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
		self.menubar.setObjectName("menubar")
		Cart.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(Cart)
		self.statusbar.setObjectName("statusbar")
		Cart.setStatusBar(self.statusbar)

		self.retranslateUi(Cart)
		QtCore.QMetaObject.connectSlotsByName(Cart)

	def retranslateUi(self, Cart):
		_translate = QtCore.QCoreApplication.translate
		Cart.setWindowTitle(_translate("Cart", "MainWindow"))
		self.label_5.setText(_translate("Cart", "Cart"))
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("Cart", "Order_No"))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("Cart", "ProductID"))
		item = self.tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("Cart", "Quantity"))
		__sortingEnabled = self.tableWidget.isSortingEnabled()
		self.tableWidget.setSortingEnabled(False)
		self.tableWidget.setSortingEnabled(__sortingEnabled)
		self.pushButton_2.setText(_translate("Cart", "Proceed To Pay"))
		self.pushButton_4.setText(_translate("Cart", "Load"))
		self.label.setText(_translate("Cart", "REMOVE ITEMS"))
		self.label_2.setText(_translate("Cart", "OrderNo"))
		self.label_4.setText(_translate("Cart", "ProductID"))
		self.pushButton.setText(_translate("Cart", "Remove"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Cart = QtWidgets.QMainWindow()
	ui = Ui_Cart()
	ui.setupUi(Cart)
	Cart.show()
	sys.exit(app.exec_())

