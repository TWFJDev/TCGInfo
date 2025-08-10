from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import username_helper

class TestApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'

        screen = Screen()

        btn = MDRectangleFlatButton(text='Show', pos_hint={'center_x': 0.5, 'center_y': 0.4}, on_release=self.show_data)

        self.username = Builder.load_string(username_helper)

        screen.add_widget(self.username)
        screen.add_widget(btn)

        return screen
    
    def show_data(self, obj):
        if self.username.text == '':
            check_string = 'Please enter a username!'
        else:
            check_string = self.username.text

        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')

        self.dialog = MDDialog(title='Username Check', text=check_string, buttons=[more_button, close_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
    
TestApp().run()