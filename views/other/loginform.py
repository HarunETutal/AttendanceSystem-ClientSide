# -*- author: Harun Emre Tutal -*-

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from views.widgets import CTextInput


SUCCESS_MESSAGE_COLOR = (0, .6, 0, 1)
INFO_MESSAGE_COLOR = (.1, .1, .1, 1)
WARNING_MESSAGE_COLOR = (.7, .7, 0, 1)
DANGER_MESSAGE_COLOR = (.6, 0, 0, 1)

LOGINFORM_KV = """
<FormInput@CTextInput>:
    size_hint_y: None
    height: "55dp"
    padding: [15, (self.height - self.line_height) / 2]
    radius: dp(15), dp(15), dp(15), dp(15)
    multiline: False
    halign: "center"
    write_tab: False
    font_size: "17sp"

<FormLabel@Label>:
    size_hint_y: None
    color: (.3, .3, .3, 1)

<LogInForm>:
    orientation: "vertical"
    size_hint_y: None
    height: self.minimum_height
    spacing: "15dp"
    padding: "10dp"
    pos_hint: {"center_y":.5}

    FormLabel:
        id: title_label
        text: root.title
        height: self.texture_size[1] + kivy.metrics.dp(60)
        font_size: "20sp"

    FormInput:
        id: username_input
        hint_text: root.username_hint_text
        input_filter: "int"

    FormInput:
        id: password_input
        hint_text: root.password_hint_text
        password: True
        password_mask: "•"

    CButton:
        id: submit_button
        text:
        markup: True
        pos_hint: {"center_x": .5}
        size_hint: None, None
        size: "300dp", "55dp"
        radius: dp(15), dp(15), dp(15), dp(15)
        font_size: "17sp"
        on_release: root.dispatch("on_submit")
    
    FormLabel:
        id: message_label
        height: self.texture_size[1] + kivy.metrics.dp(10)
        font_size: "17sp"
"""


class LogInForm(BoxLayout):
    Builder.load_string(LOGINFORM_KV)

    ## Form Properties
    # Form
    title = StringProperty("Form Title", allownone=False)

    # Username Input
    username_input_filter = StringProperty("str", allownone=False)
    username_hint_text = StringProperty("Username", allownone=False)

    # Password Input
    password_hint_text = StringProperty("Password", allownone=False)

    # Submit Button
    submit_button_text = StringProperty("Log In", allownone=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Define form submit event
        self.register_event_type("on_submit")
        
    def on_submit(self, *args, **kwargs):
        """ This event will be trigged when the form is submitted """
    
    def _set_message_color(self, status):
        _statuses = ("success", "info", "warning", "danger")
        assert status in _statuses, f"status must be one of them: {_statuses}"

        if status == "success":
            self.message_label.color = SUCCESS_MESSAGE_COLOR
        elif status == "info":
            self.message_label.color = INFO_MESSAGE_COLOR
        elif status == "warning":
            self.message_label.color = WARNING_MESSAGE_COLOR
        else:
            self.message_label.color = DANGER_MESSAGE_COLOR
    
    def set_form_message(self, message, status):
        self.message_label.text = message
        self._set_message_color(status)
    

    # Form Items
    @property
    def title_label(self):
        return self.ids.title_label

    @property
    def username_input(self):
        return self.ids.username_input

    @property
    def password_input(self):
        return self.ids.password_input

    @property
    def submit_button(self):
        return self.ids.submit_button
    
    @property
    def message_label(self):
        return self.ids.message_label
    

    # Events
    def on_title(self, instance, new_title):
        self.title_label.text = new_title
    
    def on_username_input_filter(self, instance, filter_key):
        self.username_input.input_filter = filter_key
    
    def on_username_hint_text(self, instance, hint_text):
        self.username_input.hint_text = hint_text
    
    def on_password_hint_text(self, instance, hint_text):
        self.password_input.hint_text = hint_text
    
    def on_submit_button_text(self, instance, new_text):
        self.submit_button.text = new_text
