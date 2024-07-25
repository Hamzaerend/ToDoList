from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 561, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.itemekle_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.ekle())
        self.itemekle_Button.setGeometry(QtCore.QRect(10, 80, 171, 51))
        self.itemekle_Button.setObjectName("itemekle_Button")
        self.itemsil_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.sil())
        self.itemsil_Button.setGeometry(QtCore.QRect(190, 80, 181, 51))
        self.itemsil_Button.setObjectName("itemsil_Button")
        self.temizle_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.temizle())
        self.temizle_Button.setGeometry(QtCore.QRect(380, 80, 191, 51))
        self.temizle_Button.setObjectName("temizle_Button")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 140, 561, 301))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def ekle(self):
        item = self.lineEdit.text()
        self.listWidget.addItem(item)
        self.lineEdit.setText("")

    def sil(self):
        clicked = self.listWidget.currentRow()
        self.listWidget.takeItem(clicked)

    def temizle(self):
        self.listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.itemekle_Button.setText(_translate("MainWindow", "Görev Ekle"))
        self.itemsil_Button.setText(_translate("MainWindow", "Görev Sil"))
        self.temizle_Button.setText(_translate("MainWindow", "Listeyi Temizle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
