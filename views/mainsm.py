# -*- title: Main Screen Manager -*-

from kivy.uix.screenmanager import ScreenManager
from views.screens.loginscreen import LogInScreen

class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(LogInScreen(name="login-screen"))
