import flet as ft


class Controller(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.ListView(
            controls=[

            ]
        )
