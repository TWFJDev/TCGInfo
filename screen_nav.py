screen_helper = """
ScreenManager:
    DashboardScreen:
    SetsScreen:
    CardsScreen:
    ProductsScreen:
    CollectionScreen:

<DashboardScreen>:
    name: 'dashboard'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: 'Dashboard'
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
                            on_release:
                                root.manager.current = 'dashboard'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'view-dashboard'

                        OneLineIconListItem:
                            text: 'Sets'
                            on_release:
                                root.manager.current = 'sets'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'card-multiple'

                        OneLineIconListItem:
                            text: 'Cards'
                            on_release:
                                root.manager.current = 'cards'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'cards'

                        OneLineIconListItem:
                            text: 'Products'
                            on_release:
                                root.manager.current = 'products'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'package-variant'

                        OneLineIconListItem:
                            text: 'Collection(s)'
                            on_release:
                                root.manager.current = 'collection'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'card-plus'

<SetsScreen>:
    name: 'sets'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Sets'
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
                            on_release:
                                root.manager.current = 'dashboard'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'view-dashboard'

                        OneLineIconListItem:
                            text: 'Sets'
                            on_release:
                                root.manager.current = 'sets'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'card-multiple'

                        OneLineIconListItem:
                            text: 'Cards'
                            on_release:
                                root.manager.current = 'cards'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'cards'

                        OneLineIconListItem:
                            text: 'Products'
                            on_release:
                                root.manager.current = 'products'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'package-variant'

                        OneLineIconListItem:
                            text: 'Collection(s)'
                            on_release:
                                root.manager.current = 'collection'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'card-plus'

<CardsScreen>:
    name: 'cards'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Cards'
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
                            on_release:
                                root.manager.current = 'dashboard'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'view-dashboard'

                        OneLineIconListItem:
                            text: 'Sets'
                            on_release:
                                root.manager.current = 'sets'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'card-multiple'

                        OneLineIconListItem:
                            text: 'Cards'
                            on_release:
                                root.manager.current = 'cards'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'cards'

                        OneLineIconListItem:
                            text: 'Products'
                            on_release:
                                root.manager.current = 'products'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'package-variant'

                        OneLineIconListItem:
                            text: 'Collection(s)'
                            on_release:
                                root.manager.current = 'collection'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'card-plus'

<ProductsScreen>:
    name: 'products'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Products'
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
                            on_release:
                                root.manager.current = 'dashboard'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'view-dashboard'

                        OneLineIconListItem:
                            text: 'Sets'
                            on_release:
                                root.manager.current = 'sets'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'card-multiple'

                        OneLineIconListItem:
                            text: 'Cards'
                            on_release:
                                root.manager.current = 'cards'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'cards'

                        OneLineIconListItem:
                            text: 'Products'
                            on_release:
                                root.manager.current = 'products'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'package-variant'

                        OneLineIconListItem:
                            text: 'Collection(s)'
                            on_release:
                                root.manager.current = 'collection'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'card-plus'

<CollectionScreen>:
    name: 'collection'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Collection'
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
                            on_release:
                                root.manager.current = 'dashboard'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'view-dashboard'

                        OneLineIconListItem:
                            text: 'Sets'
                            on_release:
                                root.manager.current = 'sets'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'card-multiple'

                        OneLineIconListItem:
                            text: 'Cards'
                            on_release:
                                root.manager.current = 'cards'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'cards'

                        OneLineIconListItem:
                            text: 'Products'
                            on_release:
                                root.manager.current = 'products'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'package-variant'

                        OneLineIconListItem:
                            text: 'Collection(s)'
                            on_release:
                                root.manager.current = 'collection'
                                nav_drawer.set_state('close')
                            IconLeftWidget:
                                icon: 'card-plus'
"""