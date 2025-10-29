from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from av_call import av_client

class NewWindow(QMainWindow):
    def __init__(self,id, password):
        super().__init__()
        self.resize(640,480)
        self.setWindowTitle("New Window")

        self.display_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.display_width, self.display_height)

        button=QPushButton('Conectar con médico')
        button.clicked.connect(self.call_doctor)
        
        label=QLabel(f'Ingrese IP')
        self.text=QLineEdit()
        layout=QGridLayout()

        layout.addWidget(self.image_label, 0, 0, 2, 2)
        layout.addWidget(label, 2, 0,1,1,Qt.AlignCenter)
        layout.addWidget(self.text, 2, 1,1,1,Qt.AlignCenter)
        layout.addWidget(button, 3, 0,1,2,Qt.AlignCenter)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
    
    
    def call_doctor(self):
        call=av_client(self.text.text(), self.image_label, self.display_width, self.display_height)
        print('Conectando a médico en IP:', self.text.text())
        call.connect()
