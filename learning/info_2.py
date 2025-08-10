from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

class TestApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()

        # btn_flat = MDRectangleFlatButton(text='Hello', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # screen.add_widget(btn_flat)

        icon_button = MDFloatingActionButton(icon='language-python', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(icon_button)

        return screen
    
TestApp().run()