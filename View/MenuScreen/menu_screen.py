import os

from kivymd.uix.screen import MDScreen

from View.MenuScreen.components import MenuCard  # NOQA


class MenuScreenView(MDScreen):
    def on_enter(self, *args) -> None:
        if not self.ids.menu_list.data:
            menu_list = [
                "Field",
                "Card",
                "Button",
                "Chip",
                "List",
                "Sliver",
                "Rail",
                "Tile",
                "Hero",
            ]
            menu_list.sort()
            for name_card in menu_list:
                self.ids.menu_list.data.append(
                    {
                        "viewclass": "MenuCard",
                        "title": name_card,
                        "elevation": 0,
                        "on_release": lambda x=name_card.lower(): self.manager.switch_screen(
                            x
                        ),
                        "source": (
                            f"{os.environ['KITCHEN_SINK_ASSETS']}/"
                            f"images/menu_screen/{name_card.lower()}.png"
                        ),
                    }
                )
