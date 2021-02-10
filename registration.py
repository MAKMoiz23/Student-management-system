from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Registration(object):
    def messagebox(self, title, message):
        mes = QtWidgets.QMessageBox()
        mes.setWindowTitle(title)
        mes.setText(message)
        mes.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mes.exec_()

    def submit_rec(self):
        student_name = self.entry_1.text()
        father_name = self.entry_2.text()
        try:
            email = self.entry_3.text()
            app_for = self.entry_4.text()
            fee_sel_program = self.entry_5.text()
            conn = pymysql.connect(host='localhost', user='root', password='23032001moiz', db='students_data_sheet')
            cur = conn.cursor()
            query = ('INSERT INTO students_data(student_name, father_name, email, class, fees) VALUES(%s, %s, %s, %s, %s)')
            data = cur.execute(query, (student_name, father_name, email, app_for, fee_sel_program))
            conn.commit()
            if (data):
                self.messagebox('Congrats', 'you have successfully entred the data')
        except:
            self.messagebox('Error', 'No data entered')

    def messagebox_del(self, title_1, message_1):
        mes = QtWidgets.QMessageBox()
        mes.setWindowTitle(title_1)
        mes.setText(message_1)
        mes.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mes.exec_()

    def delete_rec(self):
        student_name = self.entry_1.text()
        father_name = self.entry_2.text()
        try:
            conn = pymysql.connect(host='localhost', user='root', password='23032001moiz', db='students_data_sheet')
            cur = conn.cursor()
            query = ('DELETE FROM students_data WHERE student_name=%s and father_name=%s')
            data = cur.execute(query, (student_name, father_name))
            conn.commit()
            if (data):
                self.messagebox_del('Congrats', 'Data successfully deleted')
        except:
            self.messagebox_del('Error', 'No such data avilable..!!')
        
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(757, 697)
        self.Registeration = QtWidgets.QWidget(Registration)
        self.Registeration.setObjectName("Registeration")
        self.Label_1 = QtWidgets.QLabel(self.Registeration)
        self.Label_1.setGeometry(QtCore.QRect(150, 30, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(24)
        font.setUnderline(True)
        self.Label_1.setFont(font)
        self.Label_1.setObjectName("Label_1")
        self.label_2 = QtWidgets.QLabel(self.Registeration)
        self.label_2.setGeometry(QtCore.QRect(180, 110, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Registeration)
        self.label_3.setGeometry(QtCore.QRect(180, 170, 81, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Registeration)
        self.label_4.setGeometry(QtCore.QRect(180, 210, 47, 21))
        self.label_4.setObjectName("label_4")
        self.entry_1 = QtWidgets.QLineEdit(self.Registeration)
        self.entry_1.setGeometry(QtCore.QRect(330, 110, 113, 20))
        self.entry_1.setObjectName("entry_1")
        self.entry_2 = QtWidgets.QLineEdit(self.Registeration)
        self.entry_2.setGeometry(QtCore.QRect(330, 170, 113, 20))
        self.entry_2.setObjectName("entry_2")
        self.entry_3 = QtWidgets.QLineEdit(self.Registeration)
        self.entry_3.setGeometry(QtCore.QRect(330, 210, 113, 20))
        self.entry_3.setObjectName("entry_3")
        self.submit = QtWidgets.QPushButton(self.Registeration)
        self.submit.setGeometry(QtCore.QRect(180, 420, 281, 23))
        self.submit.setObjectName("submit")
        self.submit.clicked.connect(self.submit_rec)

        self.line = QtWidgets.QFrame(self.Registeration)
        self.line.setGeometry(QtCore.QRect(-40, 340, 831, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.del_rec = QtWidgets.QPushButton(self.Registeration)
        self.del_rec.setGeometry(QtCore.QRect(180, 460, 281, 23))
        self.del_rec.setObjectName("del_rec")
        self.del_rec.clicked.connect(self.delete_rec)

        self.male_ck = QtWidgets.QCheckBox(self.Registeration)
        self.male_ck.setGeometry(QtCore.QRect(190, 140, 70, 17))
        self.male_ck.setObjectName("male_ck")
        self.female_ck = QtWidgets.QCheckBox(self.Registeration)
        self.female_ck.setGeometry(QtCore.QRect(360, 140, 70, 17))
        self.female_ck.setObjectName("female_ck")

        self.label_5 = QtWidgets.QLabel(self.Registeration)
        self.label_5.setGeometry(QtCore.QRect(180, 250, 91, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Registeration)
        self.label_6.setGeometry(QtCore.QRect(180, 290, 131, 20))
        self.label_6.setObjectName("label_6")
        self.entry_5 = QtWidgets.QLineEdit(self.Registeration)
        self.entry_5.setGeometry(QtCore.QRect(330, 290, 113, 20))
        self.entry_5.setObjectName("entry_5")
        self.entry_4 = QtWidgets.QLineEdit(self.Registeration)
        self.entry_4.setGeometry(QtCore.QRect(330, 250, 113, 20))
        self.entry_4.setObjectName("entry_4")
        Registration.setCentralWidget(self.Registeration)
        self.menubar = QtWidgets.QMenuBar(Registration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName("menubar")
        Registration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Registration)
        self.statusbar.setObjectName("statusbar")
        Registration.setStatusBar(self.statusbar)

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "MainWindow"))
        self.Label_1.setText(_translate("Registration", "Registration Form"))
        self.label_2.setText(_translate("Registration", "Student Name :"))
        self.label_3.setText(_translate("Registration", "Father name :"))
        self.label_4.setText(_translate("Registration", "E-mail :"))
        self.submit.setText(_translate("Registration", "Submit"))
        self.del_rec.setText(_translate("Registration", "Delete"))
        self.male_ck.setText(_translate("Registration", "Male"))
        self.female_ck.setText(_translate("Registration", "Fe-Male"))
        self.label_5.setText(_translate("Registration", "Applying For :"))
        self.label_6.setText(_translate("Registration", "Fess of selected program :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QMainWindow()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())
