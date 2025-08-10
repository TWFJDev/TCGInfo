screen_helper = """
ScreenManager:
    MenuScreen:
    DashboardScreen:
    SetsScreen:
    
<MenuScreen>:
    name: 'menu'

    MDRectangleFlatButton:
        text: 'Dashboard'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        on_press: root.manager.current = 'dashboard'

    MDRectangleFlatButton:
        text: 'Sets'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'sets'

<DashboardScreen>:
    name: 'dashboard'

    MDLabel:
        text: 'Dashboard'
        halign: 'center'

    MDRectangleFlatButton:
        text: 'Menu'
        pos_hint: {'center_x': 0.5, 'center_y': 0.42}
        on_press: root.manager.current = 'menu'

<SetsScreen>:
    name: 'sets'

    MDLabel:
        text: 'Sets'
        halign: 'center'

    MDRectangleFlatButton:
        text: 'Menu'
        pos_hint: {'center_x': 0.5, 'center_y': 0.42}
        on_press: root.manager.current = 'menu'
"""