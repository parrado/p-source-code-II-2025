from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test other widgets")
       
        self.lw = QListWidget()
        self.lw.insertItem(0, "Circle")
        self.lw.insertItem(1, "Square")
        self.lw.insertItem(2, "Rectangle")
        self.lw.insertItem(3, "Triangle")

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lw.setFont(font)

        self.lw.itemClicked.connect(self.onClick)

        
        self.pixmap = QPixmap(400, 300)
        self.pixmap.fill(Qt.white)

        self.canvas=QLabel()
        self.canvas.setPixmap(self.pixmap)

        layout=QGridLayout()

        layout.addWidget(self.lw,0,0,4,1)
        layout.addWidget(self.canvas,4,0,3,1)
        

        widget = QWidget()
        widget.setLayout(layout)
        #QMainWindow requiere un widget central
        self.setCentralWidget(widget)

        
        # Deshabilita el botón de maximizar
        self.setWindowFlags( Qt.MSWindowsFixedSizeDialogHint)
        

    def drawCircle(self):
        painter=QPainter(self.canvas.pixmap())
        painter.setBrush(QBrush(QColor("red")))
        painter.setPen(QPen(QColor("red")))
        painter.drawEllipse(200-30,150-30,60,60)
        painter.end()
        self.canvas.repaint()

    def drawSquare(self):
        painter=QPainter(self.canvas.pixmap())
        painter.setBrush(QBrush(QColor("yellow")))
        painter.setPen(QPen(QColor("yellow")))
        painter.drawRect(200-30,150-30,60,60)
        painter.end()
        self.canvas.repaint()

    def drawRectangle(self):
        painter=QPainter(self.canvas.pixmap())
        painter.setBrush(QBrush(QColor("blue")))
        painter.setPen(QPen(QColor("blue")))
        painter.drawRect(200-30,150-20,60,40)
        painter.end()
        self.canvas.repaint()

    def drawTriangle(self):
        painter=QPainter(self.canvas.pixmap())
        painter.setBrush(QBrush(QColor("green")))
        painter.setPen(QPen(QColor("green")))
        painter.drawPolygon([QPoint(200,150-30),QPoint(200-30,150+30),QPoint(200+30,150+30)])
        painter.end()
        self.canvas.repaint()


    def onClick(self,selected): 
        self.pixmap.fill(Qt.white)   
        self.canvas.setPixmap(self.pixmap)
    
        match selected.text():
            case 'Circle':
                self.drawCircle()
            case 'Square':
                self.drawSquare()
            case 'Rectangle':
                self.drawRectangle()
            case 'Triangle':
                self.drawTriangle()



app = QApplication([])
ex = MainWindow()
ex.show()
app.exec()