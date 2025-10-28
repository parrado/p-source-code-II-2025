from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from av_call import av_client

class NewWindow(QMainWindow):
    def __init__(self,id, password):
        super().__init__()
        self.resize(640,480)
        self.setWindowTitle("New Window")

        button=QPushButton('Conectar con médico')
        button.clicked.connect(self.call_doctor)
        
        label=QLabel(f'Ingrese IP')
        self.text=QLineEdit()
        layout=QGridLayout()

        layout.addWidget(label, 0, 0)
        layout.addWidget(self.text, 0, 1)
        layout.addWidget(button, 1, 0)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    
    
    def call_doctor(self):
        call=av_client(self.text.text())
        print('Conectando a médico en IP:', self.text.text())
        call.connect()
