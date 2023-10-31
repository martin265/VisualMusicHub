import flet as ft


class LyricsNotes(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ---------------------------//-------------------------------//----------------//
        self.genre = ft.TextField(
            width=650,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.LYRICS_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",

            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="song genre".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="white",
            keyboard_type=ft.KeyboardType.NAME
        )
        #  ------------------------//------------------------//
        self.mood = ft.TextField(
            width=650,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.MOOD_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white"
            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="song mood".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="white",
            keyboard_type=ft.KeyboardType.NAME
        )
        #  ------------------------//the mood for the song will be here-----------------//
        self.theme = ft.TextField(
            width=650,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.CONTENT_PASTE_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white"
            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="song theme".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="white",
            keyboard_type=ft.KeyboardType.NAME
        )
        #   --------------------//song notes---------------------//
        self.song_notes = ft.TextField(
            width=380,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.NOTES_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white"
            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="song notes".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="white",
            keyboard_type=ft.KeyboardType.NAME
        )
        #  ----------------the pop alert for the songs_notes section here------------------//
        self.song_notes_pop = ft.AlertDialog(
            modal=True,
            content=ft.Container(
                width=800,
                height=500,
                bgcolor="white",
                border_radius=ft.border_radius.all(10),
                content=ft.Column(
                    controls=[

                    ]
                )
            ),
            title=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "your generated notes".title(),
                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                            color="#0050C1",
                            italic=True,
                            weight=ft.FontWeight.W_500
                        )
                    ]
                )
            ),
            actions=[
                ft.ElevatedButton(
                    icon=ft.icons.CLOSE_ROUNDED,
                    icon_color="red",
                    height=60, width=250,
                    text="close modal".title(),
                    elevation=None,
                    style=ft.ButtonStyle(
                        bgcolor="#4A4453",
                        color="white",

                    ),
                    #  ------------the click function-------//
                    on_click=self.close_song_notes_modal,
                ),
            ]

        )
        #  ----------------------the section ends here-------------------------------------//

    #  ----------------------------// function to validate the input fields here----------//
    def validate_inputs(self, e):
        try:
            if not self.genre.value:
                self.genre.error_text = "enter the song genre to be generated".capitalize()
                self.update()
            #  ------------------------//----------------------------//
            elif not self.mood.value:
                self.mood.error_text = "enter song mood".capitalize()
                self.update()
            #  -------------------------------//------------------------//
            elif not self.theme.value:
                self.theme.error_text = "song theme required".capitalize()
                self.update()
            #  -----------------------------------//-------------------------//
            else:
                print("hello world")

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

    #  ------------------------//---------------validate song notes-----------------//
    def validate_song_notes(self, e):
        try:
            if not self.song_notes.value:
                self.song_notes.error_text = "enter what notes to get generated".capitalize()
                self.update()
            else:
                self.open_songs_notes_modal()

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

    #  -----------------------the function to open up the songs notes modal------------//
    def open_songs_notes_modal(self):
        try:
            self.page.dialog = self.song_notes_pop
            self.song_notes_pop.open = True
            self.page.update()

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

    #  ---------------------// function to close the song notes modal--------------//
    def close_song_notes_modal(self, e):
        try:
            self.page.dialog = self.song_notes_pop
            self.song_notes_pop.open = False
            self.page.update()

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
            height=650,
            controls=[
                #  ---------------------//the container to wrap all the controls--------//
                ft.Container(
                    width=1220,
                    bgcolor="#F2ECFF",
                    border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        controls=[
                            # --------------------------------//----------------------//
                            ft.Container(
                                margin=ft.margin.only(top=20, left=20),
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "generate your song lyrics".capitalize(),
                                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                                            color="#0078D9"
                                        )
                                    ]
                                )
                            ),
                            #  ---------------the first row for the system------------//
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        width=700,
                                        margin=ft.margin.only(left=20, top=30, right=10, bottom=40),
                                        height=500,
                                        border_radius=ft.border_radius.all(10),
                                        gradient=ft.LinearGradient(
                                            colors=[
                                                "#0050C1",
                                                "#00BECE"
                                            ],
                                            begin=ft.alignment.bottom_left,
                                            end=ft.alignment.top_right
                                        ),
                                        content=ft.Column(
                                            controls=[
                                                #   -------------------the top text container---------//
                                                ft.Container(
                                                    margin=ft.margin.only(top=20),
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Text(
                                                                "ai lyric generator".capitalize(),
                                                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                                                color="white"
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #   -------------------------//--------------------//----//
                                                ft.Container(
                                                    margin=ft.margin.only(left=20, top=20),
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Row([self.genre]),
                                                            # ---------------//---------------//
                                                            ft.Row([self.mood]),
                                                            #  -------------------//----------//
                                                            ft.Row([self.theme])
                                                        ]
                                                    )
                                                ),
                                                #  ------------------the container for the buttons here----//
                                                ft.Container(
                                                    margin=ft.margin.only(left=20, right=30),
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                        controls=[
                                                            ft.ElevatedButton(
                                                                icon=ft.icons.GENERATING_TOKENS_ROUNDED,
                                                                icon_color="",
                                                                height=60, width=250,
                                                                text="generate music lyrics".title(),
                                                                elevation=None,
                                                                style=ft.ButtonStyle(
                                                                    bgcolor="#4A4453",
                                                                    color="white",

                                                                ),
                                                                #  ------------the click function-------//
                                                                on_click=self.validate_inputs,
                                                            ),
                                                            #  ---------------to clear the fields----------//
                                                            ft.IconButton(
                                                                icon=ft.icons.CLEAR_ROUNDED,
                                                                icon_color="red",
                                                                height=60,
                                                                icon_size=30,
                                                                width=100,
                                                                style=ft.ButtonStyle(
                                                                    bgcolor="#4A4453",
                                                                    color="white",

                                                                ),
                                                                #  ------------the click function-------//
                                                                on_click=self.clear_text_fields,
                                                            ),
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    #  -----------------the other container for the battle lyrics-------//
                                    ft.Container(
                                        width=430,
                                        margin=ft.margin.only(left=20, top=30, right=10, bottom=40),
                                        height=500,
                                        border_radius=ft.border_radius.all(10),
                                        gradient=ft.LinearGradient(
                                            colors=[
                                                "#0050C1",
                                                "#00BECE"
                                            ],
                                            begin=ft.alignment.top_left,
                                            end=ft.alignment.bottom_right
                                        ),
                                        content=ft.Column(
                                            controls=[
                                                ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Container(
                                                            margin=ft.margin.only(top=40),
                                                            content=ft.Row(
                                                                controls=[
                                                                    ft.Image(
                                                                        src="assets/stickers/music.png",
                                                                        height=150,
                                                                        width=150
                                                                    )
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                ),
                                                ft.Container(
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Text(
                                                                "generate song notes".title(),
                                                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                                                color="white"
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  -----------------for the input field----------//
                                                ft.Container(
                                                    margin=ft.margin.only(top=30),
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Row(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                controls=[
                                                                    self.song_notes
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ),
                                                #  -------------------container for the button------//
                                                ft.Container(
                                                    margin=ft.margin.only(top=30, left=20),
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.ElevatedButton(
                                                                icon=ft.icons.NOTES_ROUNDED,
                                                                icon_color="",
                                                                height=60, width=250,
                                                                text="generate music notes".title(),
                                                                elevation=None,
                                                                style=ft.ButtonStyle(
                                                                    bgcolor="#4A4453",
                                                                    color="white",
                                                                ),
                                                                #  ------------the click function-------//
                                                                on_click=self.validate_song_notes,
                                                            ),
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ]

                    )
                )
            ]
        )

    #  -----------------------function to clear the text fields----------------------//
    def clear_text_fields(self, e):
        try:
            self.genre.value = ""
            self.mood.value = ""
            self.theme.value = ""
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
