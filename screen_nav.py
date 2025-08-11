screen_helper = """
<OneLineIconListItem>:
    ripple_scale: 0
    ripple_alpha: 0

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
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Dashboard'
                        anchor_title: 'left'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 2
                    MDTabs:
                        id: dashboard_collection_tabs
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            MDBoxLayout:
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
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'view-dashboard'

                        OneLineIconListItem:
                            text: 'Sets'
                            on_release:
                                root.manager.current = 'sets'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'card-multiple'

                        OneLineIconListItem:
                            text: 'Cards'
                            on_release:
                                root.manager.current = 'cards'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'cards'

                        OneLineIconListItem:
                            text: 'Products'
                            on_release:
                                root.manager.current = 'products'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'package-variant'

                        OneLineIconListItem:
                            text: 'Collection(s)'
                            on_release:
                                root.manager.current = 'collection'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'card-plus'

<SetsScreen>:
    name: 'sets'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Sets'
                        anchor_title: 'left'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 2
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
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
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'view-dashboard'

                        OneLineIconListItem:
                            text: 'Sets'
                            on_release:
                                root.manager.current = 'sets'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'card-multiple'

                        OneLineIconListItem:
                            text: 'Cards'
                            on_release:
                                root.manager.current = 'cards'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'cards'

                        OneLineIconListItem:
                            text: 'Products'
                            on_release:
                                root.manager.current = 'products'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'package-variant'

                        OneLineIconListItem:
                            text: 'Collection(s)'
                            on_release:
                                root.manager.current = 'collection'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'card-plus'

<CardsScreen>:
    name: 'cards'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Cards'
                        anchor_title: 'left'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 2
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
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
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'view-dashboard'

                        OneLineIconListItem:
                            text: 'Sets'
                            on_release:
                                root.manager.current = 'sets'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'card-multiple'

                        OneLineIconListItem:
                            text: 'Cards'
                            on_release:
                                root.manager.current = 'cards'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'cards'

                        OneLineIconListItem:
                            text: 'Products'
                            on_release:
                                root.manager.current = 'products'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'package-variant'

                        OneLineIconListItem:
                            text: 'Collection(s)'
                            on_release:
                                root.manager.current = 'collection'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'card-plus'

<ProductsScreen>:
    name: 'products'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Products'
                        anchor_title: 'left'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 2
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
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
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'view-dashboard'

                        OneLineIconListItem:
                            text: 'Sets'
                            on_release:
                                root.manager.current = 'sets'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'card-multiple'

                        OneLineIconListItem:
                            text: 'Cards'
                            on_release:
                                root.manager.current = 'cards'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'cards'

                        OneLineIconListItem:
                            text: 'Products'
                            on_release:
                                root.manager.current = 'products'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'package-variant'

                        OneLineIconListItem:
                            text: 'Collection(s)'
                            on_release:
                                root.manager.current = 'collection'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'card-plus'

<CollectionScreen>:
    name: 'collection'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Collection(s)'
                        anchor_title: 'left'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        elevation: 2
                    MDTabs:
                        Tab:
                            title: "Home"
                            MDLabel:
                                text: "Welcome to the Home Tab"
                                halign: "center"
                        Tab:
                            title: "Profile"
                            MDLabel:
                                text: "Your Profile Info Here"
                                halign: "center"
                        Tab:
                            title: "Settings"
                            MDLabel:
                                text: "Adjust settings here"
                                halign: "center"
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            MDBoxLayout:
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
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'view-dashboard'

                        OneLineIconListItem:
                            text: 'Sets'
                            on_release:
                                root.manager.current = 'sets'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'card-multiple'

                        OneLineIconListItem:
                            text: 'Cards'
                            on_release:
                                root.manager.current = 'cards'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'cards'

                        OneLineIconListItem:
                            text: 'Products'
                            on_release:
                                root.manager.current = 'products'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'package-variant'

                        OneLineIconListItem:
                            text: 'Collection(s)'
                            on_release:
                                root.manager.current = 'collection'
                                nav_drawer.set_state("close", animation=False)
                            IconLeftWidget:
                                icon: 'card-plus'
"""