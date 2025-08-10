from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_nav import screen_helper

class MenuScreen(Screen):
    pass

class DashboardScreen(Screen):
    pass

class SetsScreen(Screen):
    pass

sm = ScreenManager()

sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(DashboardScreen(name='dashboard'))
sm.add_widget(SetsScreen(name='sets'))

class TestApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    
TestApp().run()