import flet as ft
from pages.administrator.dashboard import Dashboard
from pages.administrator.students import Students
from pages.administrator.records import Records
from pages.administrator.notes import Notes


def main(page: ft.Page):
    """the main page that will house most
    of the components including the navigation rail,
    how the pages should transition and alot more
    thanks to our Lord jesus Christ this will be
    a great project success I have the faith"""
    page.theme_mode = "light"
    page.window_center()
    page.theme = ft.Theme.use_material3
    page.update()

    #  --------------------------the list for all the pages will be here--------------//
    all_pages = [
        Dashboard(page=page),
        Students(page=page),
        Notes(page=page),
        Records(page=page)
    ]

    #  -------------------------functions to control the page transitions-----------------//
    def selected_page_transitions():
        try:
            for index, single_page in enumerate(all_pages):
                single_page.visible = True if index == navigation_rail.selected_index else False
                page.update()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            page.snack_bar.open = True
            page.update()

    #   ----------------------the function that will pass the pages-------------------//
    def destination_pages(e):
        try:
            selected_page_transitions()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            page.snack_bar.open = True
            page.update()

    #  --------------------function that will trigger the pop menu here--------------//
    instructions_alert = ft.AlertDialog(
        content=ft.Container(
            width=700,
            height=400,
            border_radius=ft.border_radius.all(10),
            gradient=ft.LinearGradient(
                colors=[
                    "#212121",
                    "#424242"
                ],
                begin=ft.alignment.bottom_left,
                end=ft.alignment.bottom_right
            ),
            content=ft.Column(
                controls=[
                    ft.Text("hello")
                ]
            )
        )
    )

    #  ----------------------take us very far our Lord Jesus----------------------//
    def trigger_pop_menu(e):
        try:
            page.dialog = instructions_alert
            instructions_alert.open = True
            page.update()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            page.snack_bar.open = True
            page.update()

    #  -----------------------the main navigation for the system will be here-----------//
    navigation_rail = ft.NavigationRail(
        leading=ft.FloatingActionButton(
            bgcolor="#212121",
            on_click=trigger_pop_menu,
            content=ft.Container(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            ft.icons.MUSIC_NOTE_ROUNDED,
                            size=50,
                            color="white"
                        )
                    ]
                )
            )
        ),
        selected_index=0,
        group_alignment=-0.9,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=250,
        # extended=True,
        #  ----------------------the actual pages for the system will be here-----------//
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.SPACE_DASHBOARD_ROUNDED,
                    tooltip="dashboard".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "dashboard".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            #  -------------------------//destination//-------------------------------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.PEOPLE_ALT_ROUNDED,
                    tooltip="students".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "students".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            #  -------------------------//destination//-------------------------------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.NOTES_ROUNDED,
                    tooltip="notes".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "notes".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            #  -------------------------//destination//-------------------------------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.DATA_ARRAY_ROUNDED,
                    tooltip="records".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "records".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
        ],
        on_change=destination_pages
    )
    selected_page_transitions()

    #  ------------------------adding the controls to the page here------------//
    page.add(
        ft.Row(
            controls=[
                navigation_rail,
                ft.Column(all_pages, alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )
    page.update()


if __name__ == "__main__":
    ft.app(target=main, port=9090, view=ft.WEB_BROWSER, assets_dir="./assets/notes", upload_dir="assets")
