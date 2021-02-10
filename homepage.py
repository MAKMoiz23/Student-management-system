from PyQt5 import QtCore, QtGui, QtWidgets
from registration import Ui_Registration
from studentdata import Ui_MainWindow
from complaint_st import Ui_Complain_st
from view_complaints import Ui_View_Comp

class Ui_HomePage(object):
    def registration(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Registration()
        self.ui.setupUi(self.window)
        self.window.show()
    def studentsdata(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def complaints(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Complain_st()
        self.ui.setupUi(self.window)
        self.window.show()
    def view_complaints(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_View_Comp()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, HomePage):
        HomePage.setObjectName("HomePage")
        HomePage.resize(763, 600)
        self.centralwidget = QtWidgets.QWidget(HomePage)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(260, 30, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Javanese Text")
        font.setPointSize(24)
        self.label_1.setFont(font)
        self.label_1.setMouseTracking(False)
        self.label_1.setObjectName("label_1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 360, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.registration)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 360, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.complaints)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 360, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.studentsdata)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 360, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.view_complaints)


        HomePage.setCentralWidget(self.centralwidget)
        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        _translate = QtCore.QCoreApplication.translate
        HomePage.setWindowTitle(_translate("HomePage", "MainWindow"))
        self.label_1.setText(_translate("HomePage", "Army public School"))
        self.pushButton.setText(_translate("HomePage", "Registration"))
        self.pushButton_2.setText(_translate("HomePage", "Add Complaints"))
        self.pushButton_3.setText(_translate("HomePage", "Students Registered"))
        self.pushButton_4.setText(_translate("HomePage", "view complaints"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomePage = QtWidgets.QMainWindow()
    ui = Ui_HomePage()
    ui.setupUi(HomePage)
    HomePage.show()
    sys.exit(app.exec_())
