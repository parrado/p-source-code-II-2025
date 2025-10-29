from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from av_call import av_server

class NewWindow(QMainWindow):
    def __init__(self,id, password):
        super().__init__()       
        self.setWindowTitle("New Window")

        self.display_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.display_width, self.display_height)

        button=QPushButton('Atender paciente')
        button.clicked.connect(self.receive_patient)
        
        layout=QGridLayout()

        layout.addWidget(self.image_label, 0, 0, 2, 2)
        layout.addWidget(button, 1, 0,2,2,Qt.AlignCenter)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    
    
    def receive_patient(self):
        server=av_server(self.image_label)
        server.start_server()
