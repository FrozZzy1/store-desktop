from typing import Optional

from PyQt6.QtWidgets import QMainWindow, QPushButton

from windows.authorization import AuthorizationWindow
from windows.registration import RegistrationWindow
from windows.template import TemplateWindow


class MainWindow(QMainWindow, TemplateWindow):

    def __init__(self):
        super().__init__()

        self.authorization_window: AuthorizationWindow | None = None
        self.registration_window: RegistrationWindow | None = None

        self.setWindowTitle('Store')
        self.setStyleSheet("""
        QMainWindow {
        background-image: url(images/mainwindow__background.png);
        }
        """)

        self.authorization_button = QPushButton('Авторизация', self)
        self.authorization_button.move(1000, 100)
        self.authorization_button.resize(150, 45)
        self.authorization_button.clicked.connect(self.to_authorization)

        self.registration_button = QPushButton('Регистрация', self)
        self.registration_button.move(1000, 160)
        self.registration_button.resize(150, 45)
        self.registration_button.clicked.connect(self.to_registration)

        self.show()

    def to_authorization(self):
        self.authorization_window = AuthorizationWindow()
        self.authorization_window.show()
        self.close()

    def to_registration(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()
        self.close()
