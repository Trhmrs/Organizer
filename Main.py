import sys
from PyQt5 import QtWidgets
import Organizer as Org
class ExampleApp(QtWidgets.QMainWindow,Org.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lok=[]
        self.lok2=[]
        self.pushButton.clicked.connect(self.knopka)

    def knopka(self):
        if (not self.plainTextEdit.toPlainText() == '') and (not self.textEdit_2.toPlainText()== ''):
            a={'text':self.plainTextEdit.toPlainText(),'data':self.textEdit_2.toPlainText()}
            print(a)
            self.lok.append(a)
            self.lok2.append(str(a))
            self.listWidget.clear()
            self.listWidget.insertItems(0,self.lok2)
            self.plainTextEdit.setPlainText('')
            self.textEdit_2.setPlainText('')









app=QtWidgets.QApplication(sys.argv)
window=ExampleApp()
window.show()
app.exec_()