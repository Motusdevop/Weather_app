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
        mind.create()
        self.correct = Correct()
        user = self.user_line.text()
        password = self.password_line.text()

        if user == "" or len(user) <= 3:
            self.user_line.setStyleSheet("QLineEdit {background-color: #F08080}")
            self.correct.label.setText("Your nickname must not be empty and be longer than 3 characters")
            return None
        
        if password == "" or len(password) < 4:
            self.password_line.setStyleSheet("QLineEdit {background-color: #F08080}")
            self.correct.label.setText("Your password must not be empty and must be at least 4 characters long")
            return None


        if self.button_group.checkedId() == 1:
            answer_list = mind.register(user, password)
            self.correct.label.setText(answer_list[0])
        elif self.button_group.checkedId() == 2:
            answer_list = mind.login(user, password)
            self.correct.label.setText(answer_list[0])
        
        if answer_list[2]:
            self.user_line.setStyleSheet("QLineEdit {background-color: #66CDAA}")
        else:
            self.user_line.setStyleSheet("QLineEdit {background-color: #F08080}")
        if answer_list[3]:
            self.password_line.setStyleSheet("QLineEdit {background-color: #66CDAA}")
        else:
            self.password_line.setStyleSheet("QLineEdit {background-color: #F08080}")


class Correct(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(300,200)
        self.setWindowTitle("Correct")
        self.label = QLabel("...")
        
        
        lay = QVBoxLayout(self)
        lay.addWidget(self.label, alignment = Qt.AlignCenter)

        self.show()