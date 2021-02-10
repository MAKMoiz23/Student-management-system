from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Complain_st(object):
    def messagebox(self, title, message):
        mes = QtWidgets.QMessageBox()
        mes.setWindowTitle(title)
        mes.setText(message)
        mes.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mes.exec_()

    def submit_com(self):
        try:
            student_name = self.entry.text()
            add_complaint = self.entry_1.text()
            conn = pymysql.connect(host='localhost', user='root', password='23032001moiz', db='complaint_data')
            cur = conn.cursor()
            query = ('INSERT INTO complaint_tb(student_name, complaint) VALUES(%s, %s)')
            data = cur.execute(query, (student_name, add_complaint))
            conn.commit()
            if (data):
                 self.messagebox('Congrats', 'you have registered a complaint')
        except:
            self.messagebox('Error', "Could'nt perform the following task")

    def messagebox_del_com(self, title_1, message_1):
        mes = QtWidgets.QMessageBox()
        mes.setWindowTitle(title_1)
        mes.setText(message_1)
        mes.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mes.exec_()

    def delete_com(self):
        student_name = self.entry_1.text()
        try:
            conn = pymysql.connect(host='localhost', user='root', password='23032001moiz', db='complaint_data')
            cur = conn.cursor()
            query = ('DELETE FROM complaint_tb WHERE student_name=%s')
            data = cur.execute(query, (student_name))
            conn.commit()
            if (data):
                self.messagebox_del_com('Congrats', 'Complain deleted sucessfully!!')
        except:
            self.messagebox_del_com('Error', 'No such data avilable..!!')
        
    def setupUi(self, Complain_st):
        Complain_st.setObjectName("Complain_st")
        Complain_st.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Complain_st)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 130, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 170, 91, 31))
        self.label_2.setObjectName("label_2")
        self.entry = QtWidgets.QLineEdit(self.centralwidget)
        self.entry.setGeometry(QtCore.QRect(230, 140, 181, 20))
        self.entry.setObjectName("entry")
        self.entry_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_1.setGeometry(QtCore.QRect(230, 180, 181, 101))
        self.entry_1.setObjectName("entry_1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 290, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submit_com)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 140, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.delete_com)

        Complain_st.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Complain_st)
        self.statusbar.setObjectName("statusbar")
        Complain_st.setStatusBar(self.statusbar)

        self.retranslateUi(Complain_st)
        QtCore.QMetaObject.connectSlotsByName(Complain_st)

    def retranslateUi(self, Complain_st):
        _translate = QtCore.QCoreApplication.translate
        Complain_st.setWindowTitle(_translate("Complain_st", "MainWindow"))
        self.label.setText(_translate("Complain_st", "Student Name :"))
        self.label_2.setText(_translate("Complain_st", "Enter Complaint :"))
        self.pushButton.setText(_translate("Complain_st", "Submit"))
        self.pushButton_2.setText(_translate("Complain_st", "Delete existing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Complain_st = QtWidgets.QMainWindow()
    ui = Ui_Complain_st()
    ui.setupUi(Complain_st)
    Complain_st.show()
    sys.exit(app.exec_())
