from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_View_Comp(object):
    def Loaddata(self):
        db = pymysql.connect(host='localhost', user='root', password='23032001moiz', db='complaint_data')
        cur = db.cursor()
        query = ('SELECT * from complaint_tb')
        result = cur.execute(query)
        res = cur.fetchall()
        self.tableWidget.setRowCount(0)
        db.commit()
        for row_number, row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
    def setupUi(self, View_Comp):
        View_Comp.setObjectName("View_Comp")
        View_Comp.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(View_Comp)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Loaddata)

        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        View_Comp.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(View_Comp)
        self.statusbar.setObjectName("statusbar")
        View_Comp.setStatusBar(self.statusbar)

        self.retranslateUi(View_Comp)
        QtCore.QMetaObject.connectSlotsByName(View_Comp)

    def retranslateUi(self, View_Comp):
        _translate = QtCore.QCoreApplication.translate
        View_Comp.setWindowTitle(_translate("View_Comp", "MainWindow"))
        self.pushButton.setText(_translate("View_Comp", "Load complaints"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_View_Comp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())