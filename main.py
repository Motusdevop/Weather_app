import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,300)
        self.label = QLabel("Enter login and password")
        self.login_line  = QLineEdit()
        self.password_line = QLineEdit()
        self.button = QPushButton("Confirm")
        self.button.clicked.connect(self.check)
        
        lay = QVBoxLayout(self)
        lay.addWidget(self.label, alignment = Qt.AlignCenter)
        lay.addWidget(self.login_line, alignment = Qt.AlignCenter)
        lay.addWidget(self.password_line, alignment = Qt.AlignCenter)
        lay.addWidget(self.button, alignment = Qt.AlignCenter)

    def check(self):
        login = self.login_line.text()
        password = self.password_line.text()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_win = Start()
    start_win.show()
    sys.exit(app.exec_())