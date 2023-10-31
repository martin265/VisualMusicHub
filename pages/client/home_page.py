import flet as ft


class HomePage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        """the build function for all the controls here"""
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1220,
            height=700,
            controls=[
                #  ----------the top container for the system----------//
                ft.Container(
                    bgcolor="#eceff1",
                    width=1320,
                    expand=True,
                    height=1200,
                    border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        controls=[
                            #  ----------------the other container----------------//
                            ft.Container(
                                margin=ft.margin.only(left=10, top=20),
                                content=ft.Column(
                                    controls=[
                                        #  ---------------//container for the text----------//
                                        ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.Text(
                                                        "welcome...".capitalize(),
                                                        style=ft.TextThemeStyle.DISPLAY_SMALL,
                                                    )
                                                ]
                                            )
                                        ),
                                        #  -----------------the container for the cards here----------//
                                        ft.Container(
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    ft.Container(
                                                        height=500,
                                                        width=500,
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Image(
                                                                    border_radius=ft.border_radius.all(10),
                                                                    src=f"assets/backgrounds/pexels-pixabay-270288.jpg",
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  -----------------// container for the card-------//
                                                    ft.Container(
                                                        height=500,
                                                        margin=ft.margin.only(right=10),
                                                        width=430,
                                                        border_radius=ft.border_radius.all(10),
                                                        gradient=ft.LinearGradient(
                                                            colors=[
                                                                "#523F4F",
                                                                "#009CDC"
                                                            ],
                                                            begin=ft.alignment.top_left,
                                                            end=ft.alignment.bottom_right,

                                                        ),
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Container(
                                                                    margin=ft.margin.only(top=50),
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            ft.Icon(
                                                                                ft.icons.LIGHTBULB_CIRCLE_ROUNDED,
                                                                                size=80,
                                                                                color="#FBB566"
                                                                            )
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(
                                                                    padding=ft.padding.only(left=10, right=10),
                                                                    margin=ft.margin.only(bottom=20),
                                                                    width=500,
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            ft.Row(
                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                controls=[
                                                                                    ft.Text(
                                                                                        "what you will get inside".title(),
                                                                                        weight=ft.FontWeight.W_700,
                                                                                        size=30,
                                                                                        color="#212121",

                                                                                    ),
                                                                                ]
                                                                            ),
                                                                            ft.Text(
                                                                                "provide a topic and the system will "
                                                                                "automatically create notes basing on the"
                                                                                "topic that you have provide using, machine"
                                                                                "learning and natural language"
                                                                                "processing. the content generated is "
                                                                                "proven to be of higher accuracy".capitalize(),
                                                                                weight=ft.FontWeight.W_500,
                                                                                size=20,
                                                                                color="white",
                                                                                text_align=ft.alignment.center
                                                                            ),

                                                                            #  ---------------------the text boxes for creating the notes---//
                                                                            ft.Container(
                                                                                margin=ft.margin.only(top=20),
                                                                                content=ft.Row(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    controls=[
                                                                                        ft.IconButton(
                                                                                            icon=ft.icons.FACEBOOK_ROUNDED,
                                                                                            icon_color="#f5f5f5",
                                                                                            icon_size=50,
                                                                                            on_click={},
                                                                                            tooltip="facebook".capitalize()
                                                                                        ),
                                                                                        #  ----------//-----------//
                                                                                        ft.IconButton(
                                                                                            icon=ft.icons.DISCORD_ROUNDED,
                                                                                            icon_color="#f5f5f5",
                                                                                            icon_size=50,
                                                                                            on_click={},
                                                                                            tooltip="discord".capitalize()
                                                                                        ),
                                                                                        #  ------------//---------//
                                                                                        ft.IconButton(
                                                                                            icon=ft.icons.REDDIT_ROUNDED,
                                                                                            icon_color="#ffab00",
                                                                                            icon_size=50,
                                                                                            on_click={},
                                                                                            tooltip="reddit".capitalize()
                                                                                        ),
                                                                                        # ----------------//--------
                                                                                    ]
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        #  ------------------// the other container for the other gallery components---//
                                        ft.Container(
                                            content=ft.Column(
                                                scroll=ft.ScrollMode.HIDDEN,
                                                controls=[
                                                    # ---------------// container for the center text here--------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "inside components".capitalize(),
                                                                    style=ft.TextThemeStyle.DISPLAY_SMALL,
                                                                    weight=ft.FontWeight.W_700,
                                                                    color="#212121"
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  -------------------the icon----------------//
                                                    ft.Container(
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.SETTINGS_INPUT_COMPONENT_ROUNDED,
                                                                    size=30
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  ------------------the components here---------------//
                                                    ft.Container(
                                                        margin=ft.margin.only(left=10),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Container(
                                                                    height=400,
                                                                    width=400,
                                                                    border_radius=ft.border_radius.all(10),
                                                                    gradient=ft.LinearGradient(
                                                                        colors=[
                                                                            "#523F4F",
                                                                            "#009CDC"
                                                                        ],
                                                                        begin=ft.alignment.top_left,
                                                                        end=ft.alignment.bottom_right
                                                                    ),
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            ft.Row(
                                                                                controls=[
                                                                                    
                                                                                ]
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ),

            ]
        )
