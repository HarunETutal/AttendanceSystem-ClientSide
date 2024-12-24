# -*- author: Harun Emre Tutal -*-

from kivy.graphics import Color, RoundedRectangle
from kivy.properties import ListProperty, ColorProperty
from kivy.uix.button import Button

class CButton(Button):
    bg_color = ColorProperty((.7, .7, .7, 1))
    radius = ListProperty((7, 7, 7, 7))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_color = 0, 0, 0, 0
        self.background_down = ""
        self.background_normal = ""
        self.background_disabled_down = ""
        self.background_disabled_normal = ""

        self.color = (.3, .3, .3, 1)

        with self.canvas.before:
            self._color = Color(rgba=self.bg_color)
            self._background = RoundedRectangle(radius=self.radius)
    
    def on_pos(self, instance, new_pos):
        self._background.pos = new_pos
    
    def on_size(self, instance, new_size):
        self._background.size = self.size
    
    def on_radius(self, instance, new_radius):
        self._background.radius = new_radius
    
    def on_bg_color(self, instance, new_color):
        self._color.rgba = new_color
