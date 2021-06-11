import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QLabel
from PyQt5.QtGui import QFont, QIcon


class Test(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Verdana', 10))

        self.setToolTip("Hello World!")

        button = QPushButton("Button", self)
        button.setToolTip("Privet")
        button.resize(button.sizeHint())
        button.move(50, 50)

        label = QLabel(self)
        label.setText("Hello world!")
        label.setFont(QFont("Gili Sans", 10))
        label.move(25, 25)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Привет PyQt")
        self.setWindowIcon(QIcon("amogus.jpg"))

        self.show()

app = QApplication(sys.argv)

test = Test()

sys.exit(app.exec_())