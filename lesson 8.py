import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Test(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Привет PyQt")
        self.setWindowIcon(QIcon("amogus.jpg"))

        self.show()

app = QApplication(sys.argv)

test = Test()

sys.exit(app.exec_())