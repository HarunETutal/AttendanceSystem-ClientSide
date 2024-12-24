# -*- title: Custom Text Input -*-

from kivy.graphics import Color, RoundedRectangle
from kivy.properties import ListProperty, ColorProperty
from kivy.uix.textinput import TextInput

class CTextInput(TextInput):
    radius = ListProperty((7, 7, 7, 7))
    bg_color = ColorProperty((.875, .875, .875, 1))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_color = (0, 0, 0, 0)
        self.background_active = ""
        self.background_normal = ""
        self.background_disabled_normal = ""

        self.hint_text_color = (.65, .65, .65, 1)
        self.foreground_color = (.3, .3, .3, 1)

        self.cursor_width = 3
        self.cursor_color = (.3, .3, .3, 1)

        self.selection_color = (.6, 0, 0, .4)

        with self.canvas.before:
            self._color = Color(rgba=self.bg_color)
            self._background = RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)
    
    def on_pos(self, instance, new_pos):
        self._background.pos = new_pos
    
    def on_size(self, instance, new_size):
        self._background.size = new_size
    
    def on_radius(self, instance, value):
        self._background.radius = value
    
    def on_bg_color(self, instance, value):
        self._color.rgba = self.bg_color
