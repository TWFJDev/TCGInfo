from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, NoTransition
from kivymd.uix.card import MDCard
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from threading import Thread
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.anchorlayout import MDAnchorLayout
from screen_nav import screen_helper
import requests
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout


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
        Clock.schedule_once(lambda dt: self.update_info())

    def update_info(self):
        self.root_layout.clear_widgets()

        for i in range(1, 5):
            tab = Tab(title=f'Collection {i}')
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
    def on_pre_enter(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.scrollview = self.ids.scroll_container
            self.root_layout = MDGridLayout(
                cols=1,
                spacing=dp(8),
                padding=[dp(8), dp(8), dp(8), dp(8)],
                size_hint_y=None,
            )
            self.root_layout.bind(minimum_height=self.root_layout.setter('height'))

            # placeholder
            self.label = MDLabel(
                text='Loading Data...',
                halign="center",
                theme_text_color="Primary",
                font_style="H5",
                size_hint_y=None,
                height=dp(40)
            )
            self.root_layout.add_widget(self.label)

            self.scrollview.clear_widgets()
            self.scrollview.add_widget(self.root_layout)

            # pagination state
            self.all_groups = []
            self.current_page = 0
            self.items_per_page = 10

            Thread(target=self.load_data, daemon=True).start()

    def load_data(self):
        try:
            r = requests.get("https://tcgcsv.com/tcgplayer/3/groups")
            self.all_groups = r.json().get('results', [])
        except Exception:
            self.all_groups = []

        Clock.schedule_once(lambda dt: self.show_page(0))

    def show_page(self, page_index):
        self.root_layout.clear_widgets()

        if not self.all_groups:
            self.root_layout.add_widget(
                MDLabel(
                    text="Failed to load data.",
                    halign="center",
                    theme_text_color="Error",
                    font_style="H6",
                    size_hint_y=None,
                    height=dp(40)
                )
            )
            self.root_layout.height = self.root_layout.minimum_height
            return

        # pagination slice
        start = page_index * self.items_per_page
        end = start + self.items_per_page
        page_items = self.all_groups[start:end]

        for group in page_items:
            card = MDCard(
                size_hint=(1, None),
                height=dp(72),
                elevation=4,
                padding=dp(8),
                radius=[dp(10)],
            )

            labels_layout = MDAnchorLayout(anchor_x='center', anchor_y='center')
            box = MDGridLayout(cols=1, spacing=dp(0), size_hint_y=None)
            box.bind(minimum_height=box.setter('height'))

            set_name = MDLabel(
                text=group.get('name', ''),
                halign="center",
                theme_text_color="Primary",
                font_style="Body1",
                size_hint_y=None,
                height=dp(28),
            )
            set_abbreviation = MDLabel(
                text=group.get('abbreviation', ''),
                halign="center",
                theme_text_color="Secondary",
                font_style="Caption",
                size_hint_y=None,
                height=dp(18),
            )

            box.add_widget(set_name)
            box.add_widget(set_abbreviation)
            labels_layout.add_widget(box)
            card.add_widget(labels_layout)
            self.root_layout.add_widget(card)

        total_pages = (len(self.all_groups) + self.items_per_page - 1) // self.items_per_page

        nav_layout = MDGridLayout(
            cols=3,
            size_hint_y=None,
            height=dp(56),
            padding=[dp(10), dp(10)],
            spacing=dp(10),
        )

        prev_btn = MDRaisedButton(
            text="Previous",
            disabled=(page_index == 0),
            on_release=lambda x: self.show_page(page_index - 1)
        )
        page_label = MDLabel(
            text=f"Page {page_index + 1} of {total_pages}",
            halign="center",
            valign="middle"
        )
        next_btn = MDRaisedButton(
            text="Next",
            disabled=(end >= len(self.all_groups)),
            on_release=lambda x: self.show_page(page_index + 1)
        )

        nav_layout.add_widget(prev_btn)
        nav_layout.add_widget(page_label)
        nav_layout.add_widget(next_btn)

        self.root_layout.add_widget(nav_layout)

        # **Fix for ScrollView: manually set height**
        total_height = sum([child.height + dp(8) for child in self.root_layout.children])
        self.root_layout.height = total_height

        # update current page
        self.current_page = page_index


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
