import flet as ft
import flet.canvas as cv


#  -------------------the code for the canvas here for the writing pad--------------------//
class State:
    x: float
    y: float


state = State()


class LyricWriter(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.cp = cv.Canvas(
            [
                cv.Fill(
                    ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            (0, 0), (600, 600), colors=[ft.colors.CYAN_50, ft.colors.GREY]
                        )
                    )
                ),
            ],
            content=ft.GestureDetector(
                on_pan_start=self.pan_start,
                on_pan_update=self.pan_update,
                drag_interval=10,
            ),
            expand=False,
        )

    #  -------------------------the functions for the brushes here-------------//
    def pan_start(self, e: ft.DragStartEvent):
        try:
            state.x = e.local_x
            state.y = e.local_y

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

    #  --------------------function to update the pen upon drawing--------------------//
    def pan_update(self, e: ft.DragStartEvent):
        """the function that will trigger the paint brushes here"""
        try:
            self.cp.shapes.append(
                cv.Line(
                    state.x, state.y, e.local_x, e.local_y, paint=ft.Paint(stroke_width=3)
                )
            )
            self.cp.update()
            state.x = e.local_x
            state.y = e.local_y

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

    #  ---------------------function to change the background paint-----------//
    def change_blend_mode(self, e):
        try:
            self.cp = cv.Canvas(
                [
                    cv.Fill(
                        ft.Paint(
                            color="yellow"
                        )
                    )
                ]
            )
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

    #  ----------------------the controls will be here--------------------//
    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1220,
            height=700,
            controls=[
                #  ---------------------the main container wrapper for the system---------//
                ft.Container(
                    bgcolor="#eceff1",
                    width=1320,
                    height=700,
                    border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        controls=[
                            #  ------------//the top container for the text will be here------//
                            ft.Container(
                                margin=ft.margin.only(left=30, top=10),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Text(
                                            "lyric writing pad".capitalize(),
                                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                                            color="#0050C1",
                                            weight=ft.FontWeight.W_700
                                        ),
                                        #  ---------------the colors to fill the canvas will be here-------//
                                        ft.Container(
                                            margin=ft.margin.only(top=10, right=30),
                                            content=ft.Row(
                                                controls=[
                                                    ft.IconButton(
                                                        icon=ft.icons.COLOR_LENS_ROUNDED,
                                                        icon_size=30,
                                                        icon_color="#FF7451",
                                                        tooltip="choose color blend",
                                                        bgcolor="white",
                                                        on_click={}
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            #  -------------------the container for the canvas will be here---------//
                            ft.Container(
                                #  --------------forgive me Lord if i have hurt anyone in my ways of taking--------//
                                height=500,
                                width=1200,
                                margin=ft.margin.only(left=20, right=20),
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            self.cp,
                                            border_radius=5,
                                            width=float("inf"),
                                            expand=True
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
