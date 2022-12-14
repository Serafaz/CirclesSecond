import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
from design import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def run(self, qp):
        self.do_paint = True
        self.repaint()

    def drawCircle(self, qp):
        rcolor, gcolor, bcolor = randint(0, 255), randint(0, 255), randint(0, 255)
        qp.setBrush(QColor(rcolor, gcolor, bcolor))
        r, r1 = randint(50, 150), randint(50, 250)
        qp.drawEllipse(QPoint(600, 400), r, r)
        qp.drawEllipse(QPoint(300, 400), r1, r1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
