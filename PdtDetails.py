from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb
from profile import Ui_profile 
from Orders import Ui_MainWindow5 
from Carts import Ui_Cart

class Ui_MainWindow3(object):

	def hitler(self):
		conn=mdb.connect("localhost","onshop","mysql","onlineshop")
		with conn:
			cur=conn.cursor()
			cur.execute("select pdt_id,product_name,price,category_name,availability from ProductDetails")
			result=cur.fetchall()

		self.Ord_tableWidget.setRowCount(0)
		for row_number,row_data in enumerate(result):
			self.Ord_tableWidget.insertRow(row_number)
			for column_number,data in enumerate(row_data):
				cell=QtWidgets.QTableWidgetItem(str(data))
				cell.setFlags(QtCore.Qt.ItemIsEnabled)
				self.Ord_tableWidget.setItem(row_number,column_number,cell)
		

	def statue(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_MainWindow5()
		self.ui.setupUi(self.window)
		self.window.show()

	def game(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_profile()
		self.ui.setupUi(self.window)
		self.window.show()	

	def stallone(self):
		pdtid=self.Ord_lineEdit.text()
		qtyspin=QDoubleSpinBox()
		# cur.execute('update Customers set login=1 where cus_id= "'+str(custID)+'"')

	def gotoCart(self):
		self.window = QtWidgets.QMainWindow()
		self.ui = Ui_Cart()
		self.ui.setupUi(self.window)
		self.window.show()

	def LoadDatatoCart(self):
		conn=mdb.connect("localhost", "onshop", "mysql", "onlineshop")
		with conn:
			cur1=conn.cursor()
			pid=self.Ord_lineEdit.text()
			qty=self.Ord_qty.text()
		   
			stmt="select *from ProductDetails where pdt_id=%(pdt_id)s"
			cur1.execute(stmt,{'pdt_id':str(pid)})

			count=cur1.rowcount
			
			if count==0:
				self.label.setText("ProductID not found")
			elif str(qty)=="0":
				self.label.setText("Enter Quantity")
			else:
				
				st="select availability from ProductDetails where pdt_id=%(pdt_id)s"
				cur1.execute(st,{'pdt_id':str(pid)})
				q=cur1.fetchone()[0]
				#self.label.setText(str(q))
				#q1=int(qty)
				#q2=float(q)
				if int(q)<int(qty):
					self.label.setText("Not in Stock")
					#self.label.setText(str(q2))
				else:
					cur1.execute("select cus_id from Customers where login=1")
					cid=cur1.fetchone()[0]
					#cur1.execute("insert into Cart (cus_id,order_date) values ("+str(cid)+",'"2019-04-07"')")
					
					insert_stmt = ()
					#now = datetime.date.today()
					#data = str(cid)
					cur1.execute("insert into Cart (cus_id) VALUES ("+str(cid)+")")

					cur1.execute("select max(ord_no) from Cart")
					result=cur1.fetchone()[0]
					self.label.setText(str(result))
					
					cur1.execute("update Cart set order_date = (select date(sysdate())) where ord_no = "+str(result))
					

					#cur1.execute("insert into OrderDetails(ord_no,pdt_id,qty) values("+str(result)+","+str(pid)+","+str(qty)+")")
					
					insert_stm = ("insert into OrderDetails (ord_no,pdt_id,qty) VALUES (%s, %s, %s)")
					dataa = (str(result), str(pid), str(qty))
					cur1.execute(insert_stm, dataa)

					cur1.execute("insert into OrderStatus (ord_no,status) values("+str(result)+",'pending')")
					cur1.execute("update OrderStatus set Date = (select date(sysdate())) where ord_no = "+str(result))
					#conn.commit()
					cur1.execute("insert into ShippingDetails (ord_no, tracking) values("+str(result)+",'pending')")
					
					cur1.execute("update ShippingDetails set date = (select date(sysdate())) where ord_no = "+str(result))
					#conn.commit()
					
					if int(q)==int(qty):
						cur1.execute('delete from ProductDetails where pdt_id='+str(pid)+'')
					else:
						q=int(q)-int(qty)
						cur1.execute('update ProductDetails set availability="'+str(q)+'"where pdt_id="'+str(pid)+'"')
						conn.commit()
						self.hitler()
					
					cur1.close()

	def setupUi(self, MainWindow3):
		MainWindow3.setObjectName("MainWindow3")
		MainWindow3.resize(861, 682)
		self.centralwidget = QtWidgets.QWidget(MainWindow3)
		self.centralwidget.setObjectName("centralwidget")
		# self.Ord_pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		# self.Ord_pushButton_2.setGeometry(QtCore.QRect(70, 80, 89, 25))
		# font = QtGui.QFont()
		# font.setFamily("URW Bookman L")
		# font.setPointSize(14)
		# font.setBold(True)
		# font.setWeight(75)
		# self.Ord_pushButton_2.setFont(font)
		# self.Ord_pushButton_2.setObjectName("Ord_pushButton_2")
		self.Ord_label_5 = QtWidgets.QLabel(self.centralwidget)
		self.Ord_label_5.setGeometry(QtCore.QRect(120, 510, 181, 20))
		font = QtGui.QFont()
		font.setFamily("URW Bookman L")
		font.setPointSize(13)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.Ord_label_5.setFont(font)
		self.Ord_label_5.setObjectName("Ord_label_5")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(310, 510, 371, 21))
		font = QtGui.QFont()
		font.setFamily("URW Bookman L")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setText("")
		self.label.setObjectName("label")
		self.Ord_frame = QtWidgets.QFrame(self.centralwidget)
		self.Ord_frame.setGeometry(QtCore.QRect(70, 330, 311, 161))
		self.Ord_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.Ord_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.Ord_frame.setObjectName("Ord_frame")
		self.Ord_label = QtWidgets.QLabel(self.Ord_frame)
		self.Ord_label.setGeometry(QtCore.QRect(60, 10, 181, 20))
		font = QtGui.QFont()
		font.setFamily("URW Bookman L")
		font.setPointSize(14)
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		self.Ord_label.setFont(font)
		self.Ord_label.setObjectName("Ord_label")
		self.Ord_label_2 = QtWidgets.QLabel(self.Ord_frame)
		self.Ord_label_2.setGeometry(QtCore.QRect(30, 40, 91, 20))
		font = QtGui.QFont()
		font.setFamily("URW Bookman L")
		font.setPointSize(13)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.Ord_label_2.setFont(font)
		self.Ord_label_2.setObjectName("Ord_label_2")
		self.Ord_label_3 = QtWidgets.QLabel(self.Ord_frame)
		self.Ord_label_3.setGeometry(QtCore.QRect(30, 80, 91, 21))
		font = QtGui.QFont()
		font.setFamily("URW Bookman L")
		font.setPointSize(13)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.Ord_label_3.setFont(font)
		self.Ord_label_3.setObjectName("Ord_label_3")
		self.Ord_lineEdit = QtWidgets.QLineEdit(self.Ord_frame)
		self.Ord_lineEdit.setGeometry(QtCore.QRect(130, 40, 113, 28))
		self.Ord_lineEdit.setObjectName("Ord_lineEdit")
		self.Ord_pushButton = QtWidgets.QPushButton(self.Ord_frame)
		self.Ord_pushButton.setGeometry(QtCore.QRect(80, 120, 131, 28))
		font = QtGui.QFont()
		font.setFamily("URW Bookman L")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.Ord_pushButton.setFont(font)
		self.Ord_pushButton.setObjectName("Ord_pushButton")

		self.Ord_pushButton.clicked.connect(self.LoadDatatoCart)

		self.Ord_qty = QtWidgets.QDoubleSpinBox(self.Ord_frame)
		self.Ord_qty.setGeometry(QtCore.QRect(150, 80, 69, 26))
		self.Ord_qty.setDecimals(0)
		self.Ord_qty.setObjectName("Ord_qty")
		self.Ord_frame_5 = QtWidgets.QFrame(self.centralwidget)
		self.Ord_frame_5.setGeometry(QtCore.QRect(550, 330, 301, 161))
		self.Ord_frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.Ord_frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
		self.Ord_frame_5.setObjectName("Ord_frame_5")
		self.Ord_label_6 = QtWidgets.QLabel(self.Ord_frame_5)
		self.Ord_label_6.setGeometry(QtCore.QRect(30, 50, 251, 17))
		font = QtGui.QFont()
		font.setFamily("URW Bookman L")
		font.setPointSize(16)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.Ord_label_6.setFont(font)
		self.Ord_label_6.setObjectName("Ord_label_6")
		self.Ord_pushButton_3 = QtWidgets.QPushButton(self.Ord_frame_5)
		self.Ord_pushButton_3.setGeometry(QtCore.QRect(100, 90, 101, 31))
		font = QtGui.QFont()
		font.setFamily("URW Bookman L")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.Ord_pushButton_3.setFont(font)
		self.Ord_pushButton_3.setObjectName("Ord_pushButton_3")

		self.Ord_pushButton_3.clicked.connect(self.statue)

		self.Ord_label_4 = QtWidgets.QLabel(self.centralwidget)
		self.Ord_label_4.setGeometry(QtCore.QRect(240, 10, 331, 41))
		font = QtGui.QFont()
		font.setFamily("Abyssinica SIL")
		font.setPointSize(20)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.Ord_label_4.setFont(font)
		self.Ord_label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.Ord_label_4.setObjectName("Ord_label_4")
		self.Ord_pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
		self.Ord_pushButton_4.setGeometry(QtCore.QRect(420, 320, 101, 31))
		font = QtGui.QFont()
		font.setFamily("URW Bookman L")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.Ord_pushButton_4.setFont(font)
		self.Ord_pushButton_4.setObjectName("Ord_pushButton_4")

		self.Ord_pushButton_4.clicked.connect(self.hitler)

		self.Ord_pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
		self.Ord_pushButton_5.setGeometry(QtCore.QRect(410, 580, 101, 31))
		font = QtGui.QFont()
		font.setFamily("URW Bookman L")
		font.setPointSize(14)
		font.setBold(True)
		font.setWeight(75)
		self.Ord_pushButton_5.setFont(font)
		self.Ord_pushButton_5.setObjectName("Ord_pushButton_5")

		self.Ord_pushButton_5.clicked.connect(self.gotoCart)

		self.Ord_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
		self.Ord_tableWidget.setGeometry(QtCore.QRect(180, 100, 531, 201))
		self.Ord_tableWidget.setRowCount(5)
		self.Ord_tableWidget.setColumnCount(5)
		self.Ord_tableWidget.setObjectName("Ord_tableWidget")
		item = QtWidgets.QTableWidgetItem()
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setItalic(True)
		item.setFont(font)
		self.Ord_tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setItalic(True)
		item.setFont(font)
		self.Ord_tableWidget.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setItalic(True)
		item.setFont(font)
		self.Ord_tableWidget.setHorizontalHeaderItem(2, item)
		item = QtWidgets.QTableWidgetItem()
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setItalic(True)
		item.setFont(font)
		self.Ord_tableWidget.setHorizontalHeaderItem(3, item)
		item = QtWidgets.QTableWidgetItem()
		font = QtGui.QFont()
		font.setPointSize(14)
		font.setItalic(True)
		item.setFont(font)
		self.Ord_tableWidget.setHorizontalHeaderItem(4, item)
		self.profilepushButton = QtWidgets.QPushButton(self.centralwidget)
		self.profilepushButton.setGeometry(QtCore.QRect(700, 20, 111, 31))
		self.profilepushButton.setObjectName("profilepushButton")

		self.profilepushButton.clicked.connect(self.game)


		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(640, 10, 41, 41))
		self.label_2.setText("")
		self.label_2.setPixmap(QtGui.QPixmap("usericon.png"))
		self.label_2.setScaledContents(True)
		self.label_2.setObjectName("label_2")
		MainWindow3.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow3)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 22))
		self.menubar.setObjectName("menubar")
		MainWindow3.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow3)
		self.statusbar.setObjectName("statusbar")
		MainWindow3.setStatusBar(self.statusbar)

		# self.hitler()

		self.retranslateUi(MainWindow3)
		QtCore.QMetaObject.connectSlotsByName(MainWindow3)

	def retranslateUi(self, MainWindow3):
		_translate = QtCore.QCoreApplication.translate
		MainWindow3.setWindowTitle(_translate("MainWindow3", "MainWindow"))
		# self.Ord_pushButton_2.setText(_translate("MainWindow3", "Back"))
		self.Ord_label_5.setText(_translate("MainWindow3", "Your Order Number:"))
		self.Ord_label.setText(_translate("MainWindow3", "Place your order"))
		self.Ord_label_2.setText(_translate("MainWindow3", "ProductID"))
		self.Ord_label_3.setText(_translate("MainWindow3", "Quantity"))
		self.Ord_pushButton.setText(_translate("MainWindow3", "Add To Cart"))
		self.Ord_label_6.setText(_translate("MainWindow3", "My Orders"))
		self.Ord_pushButton_3.setText(_translate("MainWindow3", "View"))
		self.Ord_label_4.setText(_translate("MainWindow3", "AVAILABLE PRODUCTS"))
		self.Ord_pushButton_4.setText(_translate("MainWindow3", "Load"))
		self.Ord_pushButton_5.setText(_translate("MainWindow3", "Proceed"))
		item = self.Ord_tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow3", "Pdt_Id"))
		item = self.Ord_tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow3", "Pdt_Name"))
		item = self.Ord_tableWidget.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow3", "Price"))
		item = self.Ord_tableWidget.horizontalHeaderItem(3)
		item.setText(_translate("MainWindow3", "Category"))
		item = self.Ord_tableWidget.horizontalHeaderItem(4)
		item.setText(_translate("MainWindow3", "Availability"))
		self.profilepushButton.setText(_translate("MainWindow3", "MY PROFILE"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow3 = QtWidgets.QMainWindow()
	ui = Ui_MainWindow3()
	ui.setupUi(MainWindow3)
	MainWindow3.show()
	sys.exit(app.exec_())

