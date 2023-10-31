import flet as ft
import os
from pathlib import Path
from connection.db_connection import my_connection
from classes.students import Student
import time
import pyautogui


class Dashboard(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.item_count = ft.Text()
        self.database_cursor = my_connection.cursor()
        # -----------------the student table will be here---------------------//
        self.student_table = ft.DataTable(
            bgcolor="white",
            border_radius=ft.border_radius.all(10),
            width=1200,
            horizontal_margin=10,
            sort_column_index=0,
            height=700,
            sort_ascending=True,
            column_spacing=5,
            heading_text_style=ft.TextStyle(
                size=15,
                weight=ft.FontWeight.BOLD,
                color="#007BDD",
            ),
            border=ft.border.all(1, "#f5f5f5"),
            columns=[
                ft.DataColumn(ft.Text("first name".title())),
                ft.DataColumn(ft.Text("last name".title())),
                ft.DataColumn(ft.Text("age".title())),
                ft.DataColumn(ft.Text("phone number".title())),
                ft.DataColumn(ft.Text("email".title())),
                ft.DataColumn(ft.Text("course".title())),
                ft.DataColumn(ft.Text("gender".title())),
                ft.DataColumn(ft.Text("grade".title())),
                ft.DataColumn(ft.Text("date registered".title())),
            ],
            rows=[]
        )
        self.text_to_type = "hello world"
        self.delay_between_keys = 0.2

    def recordings_counter(self):
        try:
            folder_path = 'recordings'

            # Create a Path object for the folder
            folder = Path(folder_path)

            # Check if the folder exists
            if folder.exists() and folder.is_dir():
                # List all items in the folder
                items = list(folder.iterdir())

                # Count the items (files and subfolders)
                self.item_count = len(items)

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

    def auto_text_type(self):
        try:
            time.sleep(5)

            for char in self.text_to_type:
                pyautogui.write(char)
                time.sleep(self.delay_between_keys)

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
        self.fetch_all_students()
        self.recordings_counter()

        return ft.ListView(
            #  ------------help us to understand you more and more each day Lord--------------------//
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1220,
            height=700,
            controls=[
                #  ------------------------the controls for the administrator panels will be here------//
                ft.Container(
                    bgcolor="#eceff1",
                    border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        controls=[
                            #  -----------------the container for the top most controls----------//
                            ft.Container(
                                margin=ft.margin.only(top=15, left=20),
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "main dashboard".capitalize(),
                                            style=ft.TextThemeStyle.BODY_MEDIUM,
                                            color="",
                                            weight=ft.FontWeight.BOLD,
                                            size=24
                                        )
                                    ]
                                )
                            ),
                            #  ----------------------------//------------------//--------------//
                            ft.Container(
                                margin=ft.margin.only(left=20),
                                content=ft.Row(
                                    controls=[
                                        #  ----------------the main cards will be here-----------//
                                        ft.Container(
                                            height=400,
                                            width=700,
                                            shadow=ft.BoxShadow(
                                                blur_radius=2,
                                                # spread_radius=1,
                                                blur_style=ft.ShadowBlurStyle.INNER
                                            ),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#311B92",
                                                    "#0050C1"
                                                ],
                                                begin=ft.alignment.center_left,
                                                end=ft.alignment.bottom_right
                                            ),
                                            border_radius=ft.border_radius.all(10),
                                            content=ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        controls=[
                                                            #  ------------------the top inner container here-------//
                                                            ft.Container(
                                                                margin=ft.margin.only(top=20, left=30),
                                                                content=ft.Row(
                                                                    controls=[
                                                                        ft.Icon(
                                                                            ft.icons.QUERY_STATS_ROUNDED,
                                                                            color="#E52E6A",
                                                                            size=40,
                                                                        ),

                                                                        ft.Text(
                                                                            "stats".capitalize(),
                                                                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                                                                            color="white"
                                                                        )
                                                                    ]
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                    #  ------------------------//-----------------------//
                                                    ft.Container(
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Container(
                                                                    margin=ft.margin.only(left=30, top=10),
                                                                    border=ft.border.all(1, color="white"),
                                                                    height=200,
                                                                    width=300,
                                                                    border_radius=ft.border_radius.all(10),
                                                                    content=ft.Column(
                                                                        controls=[
                                                                            #   -------------the container for the text-----//
                                                                            ft.Container(
                                                                                margin=ft.margin.only(top=20, left=30),
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.Icon(
                                                                                            ft.icons.MIC_EXTERNAL_ON_ROUNDED,
                                                                                            color="#FF7451",
                                                                                            size=40
                                                                                        ),
                                                                                        ft.Text(
                                                                                            "active recordings...".capitalize(),
                                                                                            color="white",
                                                                                            size=20,
                                                                                            weight=ft.FontWeight.BOLD
                                                                                        )
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            #  ---------------the container to display the total recordings------//
                                                                            ft.Container(
                                                                                margin=ft.margin.only(left=30),
                                                                                content=ft.Row(
                                                                                    controls=[
                                                                                        ft.Text(
                                                                                            f"{self.item_count}",
                                                                                            style=ft.TextThemeStyle.BODY_LARGE,
                                                                                            color="white",
                                                                                            weight=ft.FontWeight.W_700,
                                                                                            size=90
                                                                                        ),
                                                                                        ft.Text(
                                                                                            "recordings".capitalize(),
                                                                                            color="",
                                                                                            size=24,
                                                                                            weight=ft.FontWeight.W_500
                                                                                        )
                                                                                    ]
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                ),
                                                                #  ------------------//-----------//
                                                                ft.Container(
                                                                    margin=ft.margin.only(left=30, top=10),
                                                                    border=ft.border.all(1, color="white"),
                                                                    height=200,
                                                                    width=300,
                                                                    border_radius=ft.border_radius.all(10),
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
                                        ),
                                        #  -----------------------//---------------------//-------//
                                        ft.Container(
                                            height=400,
                                            width=455,
                                            border_radius=ft.border_radius.all(10),
                                            shadow=ft.BoxShadow(
                                                blur_radius=2,
                                                # spread_radius=1,
                                                blur_style=ft.ShadowBlurStyle.INNER
                                            ),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#311B92",
                                                    "#0050C1"
                                                ],
                                                begin=ft.alignment.bottom_right,
                                                end=ft.alignment.top_right
                                            ),
                                            #  -----------------the container for the AI caplot information-----------//
                                            content=ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        margin=ft.margin.only(top=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "program insides",
                                                                    weight=ft.FontWeight.W_700,
                                                                    color="white",
                                                                    style=ft.TextThemeStyle.HEADLINE_MEDIUM
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  -----------------------container for the list tiles here-------------//
                                                    ft.Container(
                                                        width=100,
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(ft.icons.BUILD_ROUNDED, size=30,
                                                                        color="#FFB84A"),
                                                                ft.Text(
                                                                    "the system has been integrated with "
                                                                    "machine learning and open ai"
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  --------------------//--------------------//------------//
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            #  ---------------------the container to show all the available students----//
                            ft.Container(
                                width=1220,
                                margin=ft.margin.only(left=10, top=20, right=10),
                                padding=ft.padding.only(left=10, right=30, top=30, bottom=30),
                                bgcolor="#F2ECFF",
                                border_radius=ft.border_radius.all(10),
                                content=ft.Row(
                                    controls=[
                                        ft.Tabs(
                                            selected_index=1,
                                            animation_duration=200,
                                            scrollable=True,
                                            width=1170,
                                            height=600,
                                            tabs=[
                                                ft.Tab(
                                                    text="registered students".title(),
                                                    icon=ft.icons.APP_REGISTRATION_ROUNDED,
                                                    content=ft.Container(
                                                        content=ft.Row(
                                                            controls=[
                                                                self.student_table
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ),
                ft.Container()
            ]
        )

    #  ---------------------------//function to fetch al, the available students-----------------//
    def fetch_all_students(self):
        try:
            sql = "SELECT * FROM Students"
            self.database_cursor.execute(sql)
            all_results = self.database_cursor.fetchall()
            #  ----------pushing the data to the main table here----------------//
            columns = [column[0] for column in self.database_cursor.description]
            rows = [dict(zip(columns, row)) for row in all_results]

            for single_record in rows:
                self.student_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(single_record["first_name"])),
                            ft.DataCell(ft.Text(single_record["last_name"])),
                            ft.DataCell(ft.Text(single_record["age"])),
                            ft.DataCell(ft.Text(single_record["phone_number"])),
                            ft.DataCell(ft.Text(single_record["email"][:5])),
                            ft.DataCell(ft.Text(single_record["course"])),
                            ft.DataCell(ft.Text(single_record["gender"][:10])),
                            ft.DataCell(ft.Text(single_record["grade"])),
                            ft.DataCell(ft.Text(single_record["registered_date"])),
                            #  -----------------------// the controls for the crud functions---------------//
                        ]
                    )
                )
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
