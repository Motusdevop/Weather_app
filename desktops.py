from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import mind


class Start(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(500,300)
        self.setWindowTitle("Sing up or Sing in")
        self.label = QLabel("Enter login and password")
        self.user_line  = QLineEdit(placeholderText="User...")
        self.password_line = QLineEdit(placeholderText="Password...")
        self.button = QPushButton("Confirm")
        self.button.clicked.connect(self.check)

        self.register_radio = QRadioButton("Register")
        self.login_radio = QRadioButton("Login")
        self.login_radio.setChecked(True)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.register_radio, id=1)
        self.button_group.addButton(self.login_radio, id=2)
        
        lay = QVBoxLayout(self)
        lay.addWidget(self.label, alignment = Qt.AlignCenter)
        lay.addWidget(self.user_line, alignment = Qt.AlignCenter)
        lay.addWidget(self.password_line, alignment = Qt.AlignCenter)
        lay.addWidget(self.register_radio)
        lay.addWidget(self.login_radio)
        lay.addWidget(self.button, alignment = Qt.AlignCenter)

    def check(self):
        global correct
        mind.create()
        user = self.user_line.text()
        password = self.password_line.text()
        if self.button_group.checkedId() == 1:
            correct.label.setText(mind.register(user, password)[0])
        elif self.button_group.checkedId() == 2:
            correct.label.setText(mind.login(user, password)[0])
        correct.show()


class Correct(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(300,200)
        self.setWindowTitle("Correct")
        self.label = QLabel("...")
        
        lay = QVBoxLayout(self)
        lay.addWidget(self.label, alignment = Qt.AlignCenter)