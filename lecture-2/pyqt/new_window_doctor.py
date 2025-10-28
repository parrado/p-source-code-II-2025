from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from av_call import av_server

class NewWindow(QMainWindow):
    def __init__(self,id, password):
        super().__init__()
        self.resize(640,480)
        self.setWindowTitle("New Window")

        button=QPushButton('Atender paciente')
        button.clicked.connect(self.receive_patient)
        
        layout=QGridLayout()

        layout.addWidget(button, 1, 0)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    
    
    def receive_patient(self):
        server=av_server()
        server.start_server()
