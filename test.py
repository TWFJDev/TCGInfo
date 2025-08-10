from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, NoTransition
from screen_nav import screen_helper
from kivy.core.window import Window

Window.size = (384, 824)

class DashboardScreen(Screen):
    pass

class SetsScreen(Screen):
    pass

class CardsScreen(Screen):
    pass

class ProductsScreen(Screen):
    pass

class CollectionScreen(Screen):
    pass

class TCGInfoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'

        root = Builder.load_string(screen_helper)
        root.transition = NoTransition()
        return root

if __name__ == '__main__':
    TCGInfoApp().run()