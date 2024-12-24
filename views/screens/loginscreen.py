# -*- title: Login Screen -*-

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from views.other import LogInForm  
from views.widgets import CToggleButton
from controls.users import user_login


STUDENT_FORM_SCREEN = "student_form_screen"
LECTURER_FORM_SCREEN = "lecturer_form_screen"

LOGIN_KV = f"""
#: import NoTransition kivy.uix.screenmanager.NoTransition

<LogInToggleButton@CToggleButton>:
    group: "user_type"
    radius: dp(10), dp(10), dp(10), dp(10)
    allow_no_selection: False
    text_size: self.size
    halign: "center"
    valign: "middle"
    font_size: "17sp"
    markup: True

<LogInScreen>:
    BoxLayout:
        orientation: "vertical"

        BoxLayout:
            spacing: "5dp"
            padding: "5dp"
            size_hint_y: None
            height: "60dp"

            LogInToggleButton:
                text: "[b]Öğrenci[/b]"
                state: "down"
                on_state: root.on_change_form(self.state)
            LogInToggleButton:
                text: "[b]Öğretim Görevlisi[/b]"

        ScreenManager:
            id: login_forms
            transition: NoTransition()

            Screen:
                name: "{STUDENT_FORM_SCREEN}"

                LogInForm:
                    id: student_form
                    title: "Öğrenci Giriş Formu"
                    username_hint_text: "Öğrenci Numarası"
                    username_input_filter: "int"
                    password_hint_text: "Parola"
                    submit_button_text: "[b]Giriş Yap[/b]"
                    on_submit: root.form_submit(self, "student")
            Screen:
                name: "{LECTURER_FORM_SCREEN}"

                LogInForm:
                    id: lecturer_form
                    title: "Öğretim Görevlisi Giriş Formu"
                    username_hint_text: "Kullanıcı Adı"
                    password_hint_text: "Parola"
                    submit_button_text: "[b]Giriş Yap[/b]"
                    on_submit: root.form_submit(self, "lecturer")
"""

class LogInScreen(Screen):
    Builder.load_string(LOGIN_KV)

    @property
    def current_form(self):
        return self.forms_sm.current

    @current_form.setter
    def current_form(self, value):
        if value == "student_form":
            self.forms_sm.current = STUDENT_FORM_SCREEN
        elif value == "lecturer_form":
            self.forms_sm.current = LECTURER_FORM_SCREEN

    def on_change_form(self, state):
        if state == "down":
            self.current_form = "student_form"
        else:
            self.current_form = "lecturer_form"
    

    ## Form Items 

    @property
    def forms_sm(self):
        return self.ids.login_forms
    
    @property
    def student_form(self):
        return self.ids.student_form
    
    @property
    def lecturer_form(self):
        return self.ids.lecturer_form
    

    ## Events
    def form_submit(self, instance, usertype):
        if usertype == "student":
            form = self.student_form
        elif usertype == "lecturer":
            form = self.lecturer_form

        username = form.username_input.text
        password = form.password_input.text

        user_login(username, password, usertype)
