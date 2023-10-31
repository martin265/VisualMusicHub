import flet as ft


class LyricFormatter(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  --------------------getting the lyrics from the user here--------------------//
        self.student_lyrics = ft.TextField(
            width=950,
            height=100,
            autocorrect=True,
            autofocus=True,
            multiline=True,
            max_length=900,
            color="white",
            enable_suggestions=True,
            prefix_icon=ft.icons.FORMAT_CLEAR_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white"
            ),
            helper_text="characters only, write your lyrics and the system will collect the grammar for you",
            helper_style=ft.TextStyle(
                color="white",
                size=15,
                italic=True
            ),
            border_color="white",
            label="song lyrics".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="white",
            keyboard_type=ft.KeyboardType.NAME
        )

        #  ---------------------pop up menu for the corrected grammar------------------//
        self.pop_menu_grammar = ft.AlertDialog(

        )

    #  ---------------------------the function to clear the input field here--------//
    def clear_input_field(self, e):
        try:
            self.student_lyrics.value = ""
            self.update()

        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "something went wrong at {}".format(ex)
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1220,
            height=700,
            #  --------------the main controls will be here------------------//
            controls=[
                #  ---------------the main container that will house all the controls-------//
                ft.Container(
                    bgcolor="#eceff1",
                    width=1320,
                    border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        controls=[
                            #   -------------------//container for the top title----------------//
                            ft.Container(
                                margin=ft.margin.only(left=20, bottom=10, top=20),
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "your ai lyric grammar collector".capitalize(),
                                            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                            weight=ft.FontWeight.W_500,
                                            color="#0050C1"
                                        )
                                    ]
                                )
                            ),
                            #  ------------------//the container for formatting the lyrics------//
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        #  ------------the row for the first container-----------//
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    height=550,
                                                    width=1000,
                                                    #  ------------setting up the colors here----------//
                                                    gradient=ft.LinearGradient(
                                                        colors=[
                                                            "#0050C1",
                                                            "#E52E6A"
                                                        ],
                                                        begin=ft.alignment.bottom_left,
                                                        end=ft.alignment.top_right
                                                    ),
                                                    margin=ft.margin.only(top=10, left=20),
                                                    border_radius=ft.border_radius.all(10),
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.Image(
                                                                            src="assets/stickers/singer.png",
                                                                            height=300,
                                                                            width=300
                                                                        )
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                margin=ft.margin.only(top=30),
                                                                content=ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        self.student_lyrics
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                margin=ft.margin.only(left=30),
                                                                content=ft.Row(
                                                                    controls=[
                                                                        ft.ElevatedButton(
                                                                            icon=ft.icons.SPELLCHECK_ROUNDED,
                                                                            icon_color="",
                                                                            height=60, width=250,
                                                                            text="check lyrics grammar".title(),
                                                                            elevation=None,
                                                                            style=ft.ButtonStyle(
                                                                                bgcolor="#4A4453",
                                                                                color="white",
                                                                            ),
                                                                            #  ------------the click function-------//
                                                                            on_click={},
                                                                        ),
                                                                    ]
                                                                )
                                                            )

                                                        ]
                                                    )
                                                ),

                                                #  --------------------the second container here---------//
                                                ft.Container(
                                                    margin=ft.margin.only(top=50, right=10, left=30),
                                                    height=550,
                                                    width=180,
                                                    border_radius=ft.border_radius.all(10),
                                                    content=ft.Column(
                                                        controls=[
                                                            #  -----------------the other side controls----//
                                                            ft.IconButton(
                                                                icon=ft.icons.EDIT_DOCUMENT,
                                                                icon_size=80,
                                                                tooltip="edit".capitalize(),
                                                                icon_color="black",
                                                                bgcolor="white"
                                                            ),
                                                            #  -------------------//-----------------//
                                                            ft.IconButton(
                                                                icon=ft.icons.G_TRANSLATE_ROUNDED,
                                                                icon_size=80,
                                                                tooltip="translate".capitalize(),
                                                                icon_color="black",
                                                                bgcolor="white"
                                                            ),
                                                            #  ----------------------//-------------------//
                                                            ft.IconButton(
                                                                icon=ft.icons.LAYERS_CLEAR_ROUNDED,
                                                                icon_size=80,
                                                                tooltip="clear field".capitalize(),
                                                                icon_color="black",
                                                                bgcolor="white",
                                                                on_click=self.clear_input_field
                                                            ),
                                                            #  --------------------//------------------------//
                                                        ]
                                                    )
                                                )
                                            ]
                                        ),
                                        #  --------------the row for the second container--------//

                                    ]
                                )
                            ),
                            ft.Container(
                                height=90,
                                content=ft.Column(
                                    controls=[

                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
