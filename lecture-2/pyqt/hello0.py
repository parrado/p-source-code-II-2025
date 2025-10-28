from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QWidget):
   def __init__(self):
      super().__init__()
      self.resize(320,240)
      self.setWindowTitle("My first Window")
      self.label = QLabel(self)
      self.label.setText("Hello Cruel World")
      self.label.move(100,100)  
      self.show()    

app = QApplication([])
ex = window()
app.exec()