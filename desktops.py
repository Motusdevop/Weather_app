from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap

from mind import db_logic, news, weather


class Start(QWidget):

    def __init__(self):
        super().__init__()
        with open("style/Start.stylesheet") as f:
            self.setStyleSheet(f.read())
        self.Setting()
        self.initUi()
        self.show()
    
    def Setting(self):
        self.resize(500,300)
        self.setWindowTitle("Sing up or Sing in")
    
    def initUi(self):
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
        self.Guide = QLabel('<a href="guide.html" style="color: #C8C8C8"> Guide</a>')
        self.Guide.setOpenExternalLinks(True)
        
        lay = QVBoxLayout(self)
        lay.addWidget(self.label, alignment=Qt.AlignCenter)
        lay.addWidget(self.user_line, alignment=Qt.AlignCenter)
        lay.addWidget(self.password_line, alignment=Qt.AlignCenter)
        lay.addWidget(self.register_radio)
        lay.addWidget(self.login_radio)
        lay.addWidget(self.button, alignment=Qt.AlignCenter)
        lay.addWidget(self.Guide)

    def check(self):
        db_logic.create()
        self.correct = Correct()
        user = self.user_line.text()
        password = self.password_line.text()

        if user == "" or len(user) <= 3:
            self.user_line.setStyleSheet("QLineEdit {background-color: #F08080}")
            self.correct.label.setText("Your nickname must not be empty and be longer than 3 characters")
            return
        
        if password == "" or len(password) < 4:
            self.password_line.setStyleSheet("QLineEdit {background-color: #F08080}")
            self.correct.label.setText("Your password must not be empty and must be at least 4 characters long")
            return


        if self.button_group.checkedId() == 1:
            answer_list = db_logic.register(user, password)
            self.correct.label.setText(answer_list[0])
        elif self.button_group.checkedId() == 2:
            answer_list = db_logic.login(user, password)
            self.correct.label.setText(answer_list[0])
        
        if answer_list[1]:
            self.user_line.setStyleSheet("QLineEdit {background-color: #66CDAA}")
        else:
            self.user_line.setStyleSheet("QLineEdit {background-color: #F08080}")
        if answer_list[2]:
            self.password_line.setStyleSheet("QLineEdit {background-color: #66CDAA}")
        else:
            self.password_line.setStyleSheet("QLineEdit {background-color: #F08080}")
        
        if answer_list[1] and answer_list[2]:
            self.main_win = MainWin(user)
            self.hide()


class Correct(QWidget):

    def __init__(self):
        super().__init__()
        with open("style/Correct.stylesheet") as f:
            self.setStyleSheet(f.read())
        self.Setting()
        self.InitUi()
        self.show()
    
    def Setting(self):
        self.resize(300,200)
        self.move(500, 200)
        self.setWindowTitle("Correct")

    def InitUi(self):
        self.label = QLabel("...")
        self.button = QPushButton("OK")
        self.button.clicked.connect(self.hide)

        lay = QVBoxLayout(self)
        lay.addWidget(self.label, alignment=Qt.AlignCenter)
        lay.addWidget(self.button, alignment=Qt.AlignCenter)

class MainWin(QWidget):

    def __init__(self, login: str):
        super().__init__()
        MainWin.win = self
        with open("style/Main.stylesheet") as f:
            MainWin.win.setStyleSheet(f.read())
        self.login = login
        self.city = db_logic.EnterCity(self.login)
        self.Setting()
        self.InitUi()
        self.show()

    def Setting(self):
        self.resize(800,500)
        self.move(900, 200)
        self.setWindowTitle("Light Tool")
    
    def InitUi(self):
        self.result = weather.get_weather(self.city)
        self.icon = QPixmap(self.result[6])

        self.WeatherTitle = QLabel("Погода")
        self.WeatherTitle.setFont(QFont('Geneva', 24))
        self.WeatherTitle.setStyleSheet("QLabel {color: #6495ed}")
        self.name = QLabel("В населённом пункте: " + self.result[0])
        self.temp = QLabel("температура: " + self.result[1])
        self.temp_max = QLabel("максимальная температура: " + self.result[2])
        self.temp_min = QLabel("минимальная температура: " + self.result[3])
        self.humidity = QLabel("влажность воздуха: " + self.result[4])
        self.description = QLabel("Сейчас: " + self.result[5])

        self.news = news.get()
        self.world_title = QLabel("Последняя новость в разделе [В мире]:")
        self.world_title.setFont(QFont('Geneva', 24))
        self.world_title.setStyleSheet("QLabel {color: #24a319}")
        self.news_title = QLabel(self.news["title"])
        self.news_title.setFont(QFont('', 18))
        self.news_time = QLabel("Время публикации: " + self.news["time"])
        self.news_link = QLabel(f'<a href="{self.news["link"]}"> Подробнее</a>' + " Источник 'РИА Новости'")
        self.news_link.setOpenExternalLinks(True)

        
        self.label_img = QLabel(self)
        self.label_img.setPixmap(self.icon)
        self.label_img.resize(100, 100)
        

        self.btm_change = QPushButton("Изменить населённый пункт")
        self.btm_change.clicked.connect(self.setWeather)
        self.btm_update = QPushButton("Обновить данные")
        self.btm_update.clicked.connect(self.update_weather)

        lay = QVBoxLayout(self)
        hlay = QHBoxLayout(self)

        hlay.addWidget(self.btm_change)
        hlay.addWidget(self.btm_update)
        hlay.addStretch(7)

        
        lay.addWidget(self.WeatherTitle, alignment=Qt.AlignCenter)
        lay.addWidget(self.label_img)
        lay.addWidget(self.name)
        lay.addWidget(self.temp)
        lay.addWidget(self.temp_max)
        lay.addWidget(self.temp_min)
        lay.addWidget(self.humidity)
        lay.addWidget(self.description)
        lay.addLayout(hlay)
        lay.addWidget(self.world_title, alignment=Qt.AlignCenter)
        lay.addWidget(self.news_title)
        lay.addWidget(self.news_time)
        lay.addWidget(self.news_link)
    
    def setWeather(self):
        self.update_win = Upd(login=self.login)
    
    def update_weather(self):
        self.city = db_logic.EnterCity(self.login)
        self.result = weather.get_weather(self.city)
        
        self.WeatherTitle.setText("Погода")
        self.name.setText("В населённом пункте: " + self.result[0])
        self.temp.setText("температура: " + self.result[1])
        self.temp_max.setText("максимальная температура:" + self.result[2])
        self.temp_min.setText("минимальная температура:" + self.result[3])
        self.humidity.setText("влажность воздуха: " + self.result[4])
        self.description.setText("Сейчас: " + self.result[5])
        
        self.icon = QPixmap(self.result[6])
        self.label_img.setPixmap(self.icon)

        self.news = news.get()
        self.news_title.setText(self.news["title"])
        self.news_time.setText("Время публикации: " + self.news["time"])
        self.news_link.setText(f'<a href="{self.news["link"]}"> Подробнее</a>' + " Источник 'РИА Новости'")
        

class Upd(QWidget):
    def __init__(self, login: str):
        super().__init__()
        with open("style/Upd.stylesheet") as f:
            self.setStyleSheet(f.read())
        self.login = login
        self.Setting()
        self.initUi()
        self.show()
    
    def Setting(self):
        self.setWindowTitle("Update city")
        self.resize(300, 120)
    
    def initUi(self):
        self.title = QLabel("Введи город или оставь старый")
        self.line = QLineEdit(placeholderText="Лондон...")
        self.btm_cancel = QPushButton("Оставить старый")
        self.btm_change = QPushButton("Потвердить")

        self.btm_cancel.clicked.connect(self.hide)
        self.btm_change.clicked.connect(self.update)

        lay = QVBoxLayout(self)
        hlay = QHBoxLayout(self)
        
        hlay.addWidget(self.btm_cancel, alignment= Qt.AlignLeft)
        hlay.addWidget(self.btm_change, alignment= Qt.AlignRight)

        lay.addWidget(self.title, alignment= Qt.AlignCenter)
        lay.addWidget(self.line, alignment= Qt.AlignCenter)
        lay.addLayout(hlay)
    
    def update(self):
        db_logic.SetCity(city=self.line.text(), login=self.login)
        MainWin.win.update_weather()
        self.hide()