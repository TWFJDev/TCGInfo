from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (384, 824)

screen_helper = """
Screen:
    FloatLayout:

        BoxLayout:
            orientation: 'vertical'

            MDTopAppBar:
                title: 'Test App'
                left_action_items: [['menu', lambda x: app.button_test('menu')]]
                right_action_items: [['clock', lambda x: app.button_test('clock')]]
                elevation: 2

            MDLabel:
                text: 'Hello World'
                halign: 'center'
"""

class TestApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'
        screen = Builder.load_string(screen_helper)
        return screen
    
    def button_test(self, text):
        print(text)
    
TestApp().run()