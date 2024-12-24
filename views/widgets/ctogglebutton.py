# -*- author: Harun Emre Tutal -*-

from kivy.graphics import Color, RoundedRectangle, Canvas
from kivy.properties import ListProperty, ColorProperty
from kivy.uix.togglebutton import ToggleButton


class CToggleButton(ToggleButton):
    down_color = ColorProperty((.7, .7, .7, 1))
    normal_color = ColorProperty((.85, .85, .85, 1))
    radius = ListProperty((7, 7, 7, 7))

    def __init__(self, **kwargs):
        self.canvas = Canvas()

        with self.canvas.before:
            self._color = Color(rgba=self.normal_color)
            self._background = RoundedRectangle(radius=self.radius)
        
        super().__init__(**kwargs)

        self.background_color = 0, 0, 0, 0
        self.background_down = ""
        self.background_normal = ""
        self.background_disabled_down = ""
        self.background_disabled_normal = ""

        self.color = (.3, .3, .3, 1)
        
    def on_pos(self, instance, pos):
        self._background.pos = pos
    
    def on_size(self, instance, size):
        self._background.size = size
    
    def on_state(self, instance, state):
        if state == "down":
            self._color.rgba = self.down_color
        else:
            self._color.rgba = self.normal_color
        
    def on_color(self, instance, new_color):
        self.on_state(self, self.state)
    
    def on_radius(self, instance, radius):
        self._background.radius = radius
