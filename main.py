# -*- title: Attendance System Mobile App -*-
# -*- version: v0.0.1 -*-
# -*- author: Harun Emre -*-

from kivy.core.window import Window

from kivy.app import App
from views.mainsm import MainScreenManager


class ASMobileApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)

        self.main_screen_manager = MainScreenManager()
        return self.main_screen_manager


if __name__ == "__main__":
    ASMobileApp().run()
