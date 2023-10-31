import flet as ft
from pages.client.home_page import HomePage
from pages.client.students import Students
from pages.client.lylic_generator import LyricsNotes
from pages.client.studio import Studios
from pages.client.lyrics_formatter import LyricFormatter
from pages.client.visual_instruments import VisualInstruments
from pages.client.lyric_writer import LyricWriter


def main(page: ft.Page):
    page.theme_mode = "light"
    page.window_center()
    page.update()

    page.appbar = ft.AppBar(
        bgcolor="white",
        color="black",
        elevation=10,
        toolbar_height=85,
        leading=ft.Container(
            margin=ft.margin.only(left=30),
            content=ft.Row(
                controls=[
                    ft.IconButton(ft.icons.STREAM_ROUNDED,
                                  icon_size=50,
                                  icon_color="#E52E6A"),
                    #  ---------the test for the music hub website-------------//
                    ft.Text(
                        "music hub",
                        weight=ft.FontWeight.W_700,
                        style=ft.TextThemeStyle.HEADLINE_MEDIUM
                    )
                ]
            )
        ),
        center_title=False,
        actions=[
            ft.Container(
                margin=ft.margin.only(right=30),
                content=ft.Row(
                    controls=[
                        ft.ElevatedButton(text="login", on_click={}, icon=ft.icons.LOGIN_ROUNDED)
                    ]
                )
            )
        ]
    )
    page.update()
    #  --------------------the side bar navigation for the website will be here-------------//
    all_pages = [
        HomePage(page=page),
        Students(page=page),
        LyricsNotes(page=page),
        Studios(page=page),
        LyricFormatter(page=page),
        VisualInstruments(page=page),
        LyricWriter(page=page)
    ]

    #  --------------function for transitioning the pages------------------//
    def transition_through_pages():
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

    #  ---------------------------the function to find the selected page here----------//
    def destination_page(e):
        try:
            transition_through_pages()
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

    #  -------------------------the actual navigation bar here for the website----------//
    navigation_rail = ft.NavigationRail(
        selected_index=0,
        group_alignment=-0.9,
        min_width=80,
        min_extended_width=150,
        extended=False,
        #  -----------------the destinations here for the navigation-----------//
        destinations=[
            #  ------------------------//may the good Lord Jesus Christ be with us all---------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.HOME_FILLED,
                    tooltip="dashboard".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "home".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            #  ------------------------//may the good Lord Jesus Christ be with us all---------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.APP_REGISTRATION_ROUNDED,
                    tooltip="register/enroll".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "registration".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            #  ----------------------//the destination for the lyrics-----------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.LYRICS_ROUNDED,
                    tooltip="lyric generator".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "song lyrics".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            #  -------------------------the studio destination here-----------------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.PLAY_LESSON_ROUNDED,
                    tooltip="your studio".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "studio bay".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            #  -----------------the destination for the lyric formatter--------------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.FORMAT_COLOR_FILL_ROUNDED,
                    tooltip="lyric doctor".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "lyric doctor".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            # ---------------------------the visual instruments destination here----------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.PIANO_ROUNDED,
                    tooltip="visual instruments".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "instruments".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
            #  ----------------------lyric writer here for the system---------------------//
            ft.NavigationRailDestination(
                icon_content=ft.Icon(
                    ft.icons.DESIGN_SERVICES_ROUNDED,
                    tooltip="lyric writer".capitalize(),
                    size=30,
                    color="black"
                ),
                label_content=ft.Text(
                    "writer".capitalize(),
                    style=ft.TextThemeStyle.BODY_MEDIUM,
                    weight=ft.FontWeight.W_700,
                    color="#212121"
                )
            ),
        ],
        on_change=destination_page
    )
    transition_through_pages()

    #  -----------------------adding the page controls to the main window here---------//
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
    ft.app(target=main, view=ft.WEB_BROWSER)
