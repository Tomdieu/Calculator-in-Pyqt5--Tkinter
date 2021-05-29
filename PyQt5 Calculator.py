import PyQt5
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QMessageBox
import sys
from PyQt5.QtGui import QIcon,QFont
import PyQt5.sip

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Calculator")
        self.setGeometry(500,500,150,250)
        self.setMaximumSize(QSize(400,500))
        self.txt = ""
        self.calc()

    def calc(self):
        vbox = QVBoxLayout()
        l=QHBoxLayout()
        l.alignment()
        l.setGeometry(QRect(0,0,150,20))
        t=QLabel("\t\tScientific Calculator")
        t.setStyleSheet("QLabel{"
                        "color:green;"
                        "position:relative;"
                        "text-align:center"
                        "}")
        t.setAlignment(Qt.AlignCenter)
        t.setMaximumWidth(100)

        l.addWidget(t)
        grid = QGridLayout()
        grid.setVerticalSpacing(10)
        grid.setHorizontalSpacing(5)
        grid.setRowStretch(1,2)

        #entry
        self.output = QLineEdit()
        grid.addWidget(self.output,0,0,1,4)
        self.output.setAlignment(Qt.AlignRight)
        self.output.setFont(QFont("consolas",19))
        self.output.setMaxLength(19)
        self.output.setStyleSheet("text-align:center")
        self.output.setDisabled(0)
        self.setMinimumHeight(25)
        #self.output.setText("hello world")

        #creating button

        b7=QPushButton("7")
        b7.clicked.connect(lambda: self.add_to(7))
        b8=QPushButton('8')
        b8.clicked.connect(lambda :self.add_to(8))
        b9=QPushButton('9')
        b9.clicked.connect(lambda :self.add_to(9))
        bm=QPushButton('-')
        bm.clicked.connect(lambda :self.add_to('-'))

        b4 = QPushButton("4")
        b4.clicked.connect(lambda :self.add_to(4))
        b5 = QPushButton('5')
        b5.clicked.connect(lambda :self.add_to(5))
        b6 = QPushButton('6')
        b6.clicked.connect(lambda :self.add_to(6))
        bp=QPushButton('+')
        bp.clicked.connect(lambda :self.add_to('+'))

        b1 = QPushButton("1")
        b1.clicked.connect(lambda :self.add_to(1))
        b2 = QPushButton('2')
        b2.clicked.connect(lambda :self.add_to(2))
        b3 = QPushButton('3')
        b3.clicked.connect(lambda :self.add_to(3))
        bM = QPushButton('*')
        bM.clicked.connect(lambda :self.add_to('*'))

        b0 = QPushButton("0")
        b0.clicked.connect(lambda :self.add_to(0))
        bc = QPushButton('C')
        bc.clicked.connect(self.clr_entry)
        bbs = QPushButton('<-')
        bbs.clicked.connect(self.bck_entry)
        bd = QPushButton('/')
        bd.clicked.connect(lambda :self.add_to("/"))
        be=QPushButton("=")
        be.clicked.connect(self.calculate)
        bsqrt = QPushButton("mod %")
        bsqrt.clicked.connect(lambda :self.add_to("%"))
        arr = [b7,b8,b9,b4,b5,b6,b1,b2,b3,b0,bc,bp,bc,bM,bbs,bd,bm,bsqrt,be]
        for i in arr:
            i.setFont(QFont('consolas',13))

        #ading the button to the grid

        grid.addWidget(b7,1,0)
        grid.addWidget(b8,1,1)
        grid.addWidget(b9,1,2)
        grid.addWidget(bp,1,3)

        grid.addWidget(b4,2,0)
        grid.addWidget(b5,2,1)
        grid.addWidget(b6,2,2)
        grid.addWidget(bm,2,3)

        grid.addWidget(b1,3,0)
        grid.addWidget(b2,3,1)
        grid.addWidget(b3,3,2)
        grid.addWidget(bd,3,3)

        grid.addWidget(b0,4,0)
        grid.addWidget(bc,4,1)
        grid.addWidget(bbs,4,2)
        grid.addWidget(bM,4,3)

        grid.addWidget(bsqrt,5,0,1,2)
        grid.addWidget(be,5,2,1,2)
        grid.addWidget(QPushButton('hello'),6,0,1,3)

        #vbox.addLayout(l)
        vbox.setSpacing(2)
        vbox.addLayout(grid)
        vbox.setAlignment(Qt.AlignVCenter)
        self.setMinimumSize(QSize(350,300))

        self.setLayout(vbox)
    def add_to(self,text):
        self.txt+=str(text)
        self.output.setText(self.txt)
    def clr_entry(self):
        self.output.setText('')
        self.txt=""
    def bck_entry(self):
        try:
            self.txt = self.txt[:-1]
            self.output.setText(self.txt)
        except Exception as e:
            self.output.setText("")
    def calculate(self):
        try:
            out = self.output.text()

            print(out, self.txt)
            cal = str(eval(out))
            self.output.setText(cal)
            self.txt = cal
        except:
            QMessageBox.warning(self,"Warning","Error Can't Perform this Calculation : {}".format(self.output.text()))

if __name__ =="__main__":
    app=QApplication([])
    win=Window()
    win.show()
    app.exec_()
