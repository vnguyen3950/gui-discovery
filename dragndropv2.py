from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QHBoxLayout, QListWidgetItem, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        #self.label=InitialCard("initial", self)
        self.myListWidget1 = QListWidget()
        self.myListWidget2 = QListWidget()
        self.lineEdit = QLineEdit("Enter Text Here and press enter!")
        self.myListWidget1.setDefaultDropAction(Qt.MoveAction)
        self.myListWidget2.setDefaultDropAction(Qt.MoveAction)
        self.myListWidget1.setAcceptDrops(True)
        self.myListWidget1.setDragEnabled(True)

        self.myListWidget2.setAcceptDrops(True)
        self.myListWidget2.setDragEnabled(True)

        self.setGeometry(500, 500, 1000, 300)
        
        self.hboxlayout = QHBoxLayout()
        self.hboxlayout.addWidget(self.myListWidget1)
        self.hboxlayout.addWidget(self.myListWidget2)
        self.hboxlayout.addWidget(self.lineEdit)

        l1 = QListWidgetItem("Item 1", self.myListWidget1)
        l2 = QListWidgetItem("Item 2", self.myListWidget1)
        l3 = QListWidgetItem("Item 3", self.myListWidget2)
        l4 = QListWidgetItem("Item 4", self.myListWidget2)

        '''self.myListWidget1.insertItem(1, l1)
        self.myListWidget1.insertItem(2, l2)
        self.myListWidget2.insertItem(3, l3)
        self.myListWidget2.insertItem(4, l4)'''

        self.setWindowTitle("Drag n Drop")
        self.setLayout(self.hboxlayout)
        self.lineEdit.returnPressed.connect(self.addCard)
        self.show()

    def addCard(self):
        txt = str(self.lineEdit.text())
        item = QListWidgetItem(txt, self.myListWidget1)
        self.lineEdit.setText("Enter Text Here and press enter to add cards!")
    '''def createCardTxt_fn(self):
        cardTxt=str(self.lineEdit.text())
        self.label.setText(cardTxt)'''

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())



