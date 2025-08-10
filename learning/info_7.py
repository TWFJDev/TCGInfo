from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (384, 824)

nav_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: 'Test App'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 2
                    
                    Widget:
    MDNavigationDrawer:
        id: nav_drawer

        BoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8dp'

            MDLabel:
                text: 'TCG Info'
                font_style: 'Subtitle1'
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: 'All of Your Card Needs!'
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]

            MDScrollView:
                MDList:
                    OneLineIconListItem:
                        text: 'Dashboard'
                        on_release: print('Dashboard')
                        IconLeftWidget:
                            icon: 'view-dashboard'

                    OneLineIconListItem:
                        text: 'Sets'
                        IconLeftWidget:
                            icon: 'card-multiple'

                    OneLineIconListItem:
                        text: 'Cards'
                        IconLeftWidget:
                            icon: 'cards'
"""

class TestApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = 'A700'
        self.theme_cls.theme_style = 'Dark'

        screen = Builder.load_string(nav_helper)

        return screen
    
TestApp().run()