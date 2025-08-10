from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (384, 824)

KV = '''
BoxLayout:
    orientation: 'vertical'
    RecycleView:
        id: rv
        viewclass: 'MDLabel'
        RecycleBoxLayout:
            default_size: None, dp(40)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'

    BoxLayout:
        size_hint_y: None
        height: dp(50)
        spacing: dp(10)
        padding: dp(10)
        MDFlatButton:
            text: 'Previous'
            on_release: app.previous_page()
        MDLabel:
            id: page_label
            text: 'Page 1'
            halign: 'center'
        MDFlatButton:
            text: 'Next'
            on_release: app.next_page()
'''

class PaginationApp(MDApp):
    def build(self):
        self.page = 0
        self.page_size = 5
        self.items = [f"Item {i}" for i in range(1, 51)]  # 50 items total
        return Builder.load_string(KV)

    def on_start(self):
        self.load_page()

    def load_page(self):
        start = self.page * self.page_size
        end = start + self.page_size
        page_items = self.items[start:end]
        self.root.ids.rv.data = [{'text': x} for x in page_items]
        self.root.ids.page_label.text = f"Page {self.page + 1}"

    def next_page(self):
        if (self.page + 1) * self.page_size < len(self.items):
            self.page += 1
            self.load_page()

    def previous_page(self):
        if self.page > 0:
            self.page -= 1
            self.load_page()

PaginationApp().run()
