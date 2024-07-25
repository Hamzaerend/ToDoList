from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

conn = sqlite3.connect('liste.db')
c = conn.cursor()
c.execute("""CREATE TABLE if not exists todo_list(list_item text)""")
conn.commit()
conn.close


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 721, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.itemekle_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.ekle())
        self.itemekle_Button.setGeometry(QtCore.QRect(10, 80, 171, 51))
        self.itemekle_Button.setObjectName("itemekle_Button")
        self.itemsil_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.sil())
        self.itemsil_Button.setGeometry(QtCore.QRect(190, 80, 181, 51))
        self.itemsil_Button.setObjectName("itemsil_Button")
        self.temizle_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.temizle())
        self.temizle_Button.setGeometry(QtCore.QRect(380, 80, 181, 51))
        self.temizle_Button.setObjectName("temizle_Button")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 140, 721, 301))
        self.listWidget.setObjectName("listWidget")
        self.save_db = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.kaydet())
        self.save_db.setGeometry(QtCore.QRect(570, 80, 161, 51))
        self.save_db.setObjectName("save_db")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.hepsini_al()

    def hepsini_al(self):
        conn = sqlite3.connect('liste.db')
        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        conn.commit()
        conn.close
        for record in records:
            self.listWidget.addItem(str(record[0]))

    def ekle(self):
        item = self.lineEdit.text()
        self.listWidget.addItem(item)
        self.lineEdit.setText("")

    def sil(self):
        clicked = self.listWidget.currentRow()
        self.listWidget.takeItem(clicked)

    def temizle(self):
        self.listWidget.clear()
    
    def kaydet(self):
        conn = sqlite3.connect('liste.db')
        c = conn.cursor()

        c.execute('DELETE FROM todo_list;',)

        items = []
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index))
        for item in items:
            c.execute("INSERT INTO todo_list VALUES (:item)",
            {
                'item': item.text(),
            })

        conn.commit()
        conn.close

        mesaj = QMessageBox()
        mesaj.setWindowTitle("Veri tabanına kaydedildi!")
        mesaj.setText("Görev listeniz kaydedildi!")
        mesaj.setIcon(QMessageBox.Information)
        x = mesaj.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDoList"))
        self.itemekle_Button.setText(_translate("MainWindow", "Görev Ekle"))
        self.itemsil_Button.setText(_translate("MainWindow", "Görev Sil"))
        self.temizle_Button.setText(_translate("MainWindow", "Listeyi Temizle"))
        self.save_db.setText(_translate("MainWindow", "Veri Tabanına Kaydet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
