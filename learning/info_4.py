from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget

list_helper = """
Screen:
    MDScrollView:
        MDList:
            id: list_container
"""

class TestApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)
        return screen
    
    def on_start(self):
        for i in range(20):
            icon = IconLeftWidget(icon='language-python')
            items = ThreeLineIconListItem(text=f'Item {i}', secondary_text='2nd', tertiary_text='3rd')
            items.add_widget(icon)
            self.root.ids.list_container.add_widget(items)
    
TestApp().run()