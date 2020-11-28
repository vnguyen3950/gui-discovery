import sys
#import random
#from PySide2 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Hello World")
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("Hello World")
        layout.addWidget(label)

#print(PySide2.QtCore.__version__)
app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())


