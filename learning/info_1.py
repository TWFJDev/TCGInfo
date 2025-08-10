from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon

class TestApp(MDApp):
    def build(self):
        label = MDLabel(text='Hello Peeps', halign='center', theme_text_color='Custom', text_color=(236/255.0, 98/255.0, 81/255.0, 1), font_style='H1')

        icon_label = MDIcon(icon='language-python')
        
        return icon_label
    
TestApp().run()