from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, NoTransition
from screen_nav import screen_helper
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from threading import Thread
import time
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.anchorlayout import MDAnchorLayout


class Tab(MDFloatLayout, MDTabsBase):
    pass

# Screen size (for testing)
from kivy.core.window import Window

Window.size = (384, 824)

class DashboardScreen(Screen):
    def on_pre_enter(self):
        if not hasattr(self, 'root_layout'):
            self.root_layout = MDGridLayout(cols=1, rows=4, spacing=dp(8), padding=[dp(8), dp(120), dp(8), dp(8)])

            self.label = MDLabel(text='Loading Data', halign="center", theme_text_color="Primary", font_style="H5")
            self.root_layout.add_widget(self.label)

            self.add_widget(self.root_layout)

            Thread(target=self.load_data, daemon=True).start()

    def load_data(self):
        time.sleep(5)
        Clock.schedule_once(lambda dt: self.update_info())

    def update_info(self):
        self.root_layout.clear_widgets()

        for i in range(1, 5):
            tab = Tab(title=f'Tab {i}')
            self.ids.dashboard_collection_tabs.add_widget(tab)

        for i in range(1, 5):
            card = MDCard(size_hint=(1, 1), elevation=4, padding=dp(8))

            labels_layout = MDBoxLayout(orientation='vertical', spacing=dp(0), padding=0, size_hint_y=None)

            label = MDLabel(text=f"Card {i}", halign="center", valign="middle", theme_text_color="Primary", font_style="H5", size_hint_y=None, height=dp(28))
            label_1 = MDLabel(text=f"Card {i}", halign="center", valign="middle", theme_text_color="Primary", font_style="Caption", size_hint_y=None, height=dp(18))

            labels_layout.add_widget(label)
            labels_layout.add_widget(label_1)

            labels_layout.height = label.height + label_1.height

            anchor = MDAnchorLayout(anchor_x='center', anchor_y='center')
            anchor.add_widget(labels_layout)

            card.add_widget(anchor)
            self.root_layout.add_widget(card)

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