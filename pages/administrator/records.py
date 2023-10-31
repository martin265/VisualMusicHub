import flet as ft
from connection.db_connection import my_connection
from classes.students import Student
from datetime import datetime


class Records(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.editDelete_id = ft.Text()
        self.database_cursor = my_connection.cursor()
        #  ---------------------the student details----------------------//
        self.first_name = ft.TextField(
            width=300,
            height=100,
            border_color="#0050C1",
            keyboard_type=ft.KeyboardType.NAME,
            autocorrect=True,
            autofocus=True,
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            helper_text="characters only",
            hint_text="first name".capitalize(),
            label="first name".title(),
            focused_border_color="#1565c0",
        )
        # -------------------------//-------------------------------//----------------//
        self.last_name = ft.TextField(
            width=300,
            height=100,
            border_color="#0050C1",
            keyboard_type=ft.KeyboardType.NAME,
            autocorrect=True,
            autofocus=True,
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            helper_text="characters only",
            hint_text="first name".capitalize(),
            label="last name".title(),
            focused_border_color="#1565c0",
        )
        #  -------------------------//----------------------------//---------------------//
        self.age = ft.TextField(
            width=300,
            height=100,
            border_color="#0050C1",
            keyboard_type=ft.KeyboardType.NUMBER,
            autocorrect=True,
            autofocus=True,
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            helper_text="numbers only",
            hint_text="age".capitalize(),
            label="age".title(),
            focused_border_color="#1565c0",
        )
        #  -----------------------//------------------------//---------------------//
        self.phone_number = ft.TextField(
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            width=300,
            height=100,
            prefix_icon=ft.icons.PHONE_ANDROID_ROUNDED,
            helper_text="numbers only",
            border_color="#0050C1",
            label="phone number".capitalize(),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#1565c0",
            keyboard_type=ft.KeyboardType.NAME,
            border_width=2
        )
        #  ------------------------//---------------------------//-------------------//
        self.email = ft.TextField(
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            width=300,
            height=100,
            prefix_icon=ft.icons.EMAIL_ROUNDED,
            helper_text="characters only",
            border_color="#0050C1",
            label="email".capitalize(),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#1565c0",
            keyboard_type=ft.KeyboardType.EMAIL,
            border_width=2
        )
        #  ------------------------//---------------------------//-------------------//
        self.course = ft.Dropdown(
            label="select course....",
            hint_text="required field",
            helper_text="only characters",
            width=300,
            height=100,
            border_color="#0050C1",
            prefix_icon=ft.icons.LIBRARY_BOOKS_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            options=[
                ft.dropdown.Option("Mathematics"),
                ft.dropdown.Option("Social Studies"),
                ft.dropdown.Option("Biology"),
                ft.dropdown.Option("Physical science"),
                ft.dropdown.Option("Geography"),
            ]
        )
        #  ------------------------//------------------------//
        self.gender = ft.RadioGroup(
            content=ft.Row(
                controls=[
                    ft.Text(
                        "gender".capitalize(),
                        size=18,
                        weight=ft.FontWeight.W_700
                    ),
                    ft.Radio(value="male", label="male".capitalize()),
                    ft.Radio(value="female", label="female".capitalize())
                ]
            )
        )
        #  ---------------------//grade--------------------------------------//
        self.grade = ft.Dropdown(
            label="select grade....",
            width=300,
            height=100,
            hint_text="required field",
            helper_text="only characters",
            border_color="#0050C1",
            prefix_icon=ft.icons.GRADE_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            options=[
                ft.dropdown.Option("Level 4"),
                ft.dropdown.Option("Level 5"),
                ft.dropdown.Option("Level 6")
            ]
        )
        #  ------------------getting the table for the students here----------------//
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
                ft.DataColumn(ft.Text("controls".capitalize()))
            ],
            rows=[]
        )
        #  ------------------------the delete modal will be here----------------------//
        self.delete_modal = ft.AlertDialog(
            modal=False,
            content=ft.Container(
                height=100,
                width=300,
                margin=ft.margin.only(left=20, right=20),
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "are you sure you want to delete the record".capitalize(),
                            weight=ft.FontWeight.W_700
                        )
                    ]
                )
            ),
            actions=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                icon=ft.icons.CONFIRMATION_NUM_ROUNDED,
                                text="yes".capitalize(),
                                on_click=self.delete_student_record,
                                width=100,
                                height=50,
                                icon_color="#311b92"
                            ),
                            # ----------------------------the controls for the delete and update------------//
                            ft.ElevatedButton(
                                icon=ft.icons.CANCEL_ROUNDED,
                                text="NO".capitalize(),
                                on_click=self.close_delete_modal,
                                width=100,
                                height=50,
                                icon_color="#b71c1c"
                            )
                        ]
                    )
                )
            ]
        )
        #  --------------------update modal will be here for the system---------------------//
        self.update_dlg_modal = ft.AlertDialog(
            title=ft.Container(
                content=ft.Text(
                    "update student records".capitalize()
                )
            ),
            title_padding=ft.padding.only(left=20, top=20),
            content=ft.Container(
                width=600,
                height=500,
                margin=ft.margin.only(top=40),
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                self.first_name,
                                self.last_name,
                            ]
                        ),
                        ft.Row(
                            controls=[
                                self.age,
                                self.phone_number,
                            ]
                        ),
                        ft.Row(
                            controls=[
                                self.email,
                                self.course,
                            ]
                        ),
                        ft.Row(
                            controls=[
                                self.grade,
                                self.gender,
                            ]
                        ),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.ElevatedButton(
                                        text="update",
                                        icon=ft.icons.UPDATE_ROUNDED,
                                        icon_color="blue",
                                        bgcolor="#311b92",
                                        on_click=self.update_student_records,
                                        height=80,
                                        width=200,
                                        color="white"
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )
        )

    #  ------------------------the function to trigger the modal here-----------------------//
    def trigger_delete_modal(self, e):
        """the function used to open up the delete modal"""
        try:
            self.page.dialog = self.delete_modal
            self.delete_modal.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "something went wrong at {}".capitalize().format(ex),
                                size=24
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  ------------------------function to close the modal-------------------------//
    def close_delete_modal(self, e):
        try:
            self.page.dialog = self.delete_modal
            self.delete_modal.open = False
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

    def delete_student_record(self, e):
        try:
            current_date = datetime.now().strftime("%d, %A, %B")
            current_id = self.editDelete_id
            student = Student(
                first_name=self.first_name,
                last_name=self.last_name,
                age=self.age,
                gender=self.gender,
                grade=self.grade,
                phone_number=self.phone_number,
                email=self.phone_number,
                course=self.course,
                current_date=current_date
            )
            #  -------------------calling the delete function here-----------------//
            student.delete_student_record(current_id)
            print(current_id)
            self.page.snack_bar = ft.SnackBar(
                bgcolor=ft.colors.RED_700,
                content=ft.Text("record deleted successfully".title()),
                action="OK"
            )
            self.page.snack_bar.open = True
            self.page.update()
            self.delete_modal.open = False
            self.page.update()
            self.show_student_data()

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

    # ---------------------------// function to fill the id-----------------------------//
    def fill_delete_id(self, e):
        try:
            self.editDelete_id = e.control.data["id"]
            self.page.dialog = self.delete_modal
            self.delete_modal.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "something went wrong with {}".format(ex)
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  ---------------------------function to update the student records here-------------//
    def trigger_update_modal(self, e):
        try:
            self.page.dialog = self.update_dlg_modal
            self.update_dlg_modal.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "something went wrong with {}".format(ex)
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    def build(self):
        self.show_student_data()
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1220,
            height=700,
            controls=[
                #  ------------------the main container wrapper here-----------//
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "all available records".capitalize()
                                        )
                                    ]
                                )
                            ),
                            #  --------------------the container for the tabs-----------//
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
                )
            ]
        )

    def show_student_data(self):
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
                        ft.DataCell(
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        data=single_record,
                                        icon=ft.icons.UPDATE_ROUNDED,
                                        on_click=self.fill_update_records,
                                        tooltip="update",
                                        icon_color="#311b92",
                                    ),
                                    ft.IconButton(
                                        data=single_record,
                                        icon=ft.icons.DELETE_ROUNDED,
                                        on_click=self.fill_delete_id,
                                        tooltip="delete",
                                        icon_color="#f44336"
                                    ),
                                    #  ------------------deleting and updating the records-------//
                                ]
                            )
                        ),
                    ]
                )
            )

    #  -------------------//the functions for deleting and updating--------------------------//
    def fill_update_records(self, e):
        try:
            self.editDelete_id = e.control.data["id"]
            self.first_name.value = e.control.data["first_name"]
            self.last_name.value = e.control.data["last_name"]
            self.age.value = e.control.data["age"]
            self.phone_number.value = e.control.data["phone_number"]
            self.email.value = e.control.data["email"]
            self.course.value = e.control.data["course"]
            self.gender.value = e.control.data["gender"]
            self.grade.value = e.control.data["grade"]
            #  ------------------opening the update modal here-----------------//
            self.page.dialog = self.update_dlg_modal
            self.update_dlg_modal.open = True
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

    #  ----------------------// function to update the records in the database----------------//
    def update_student_records(self, e):
        try:
            current_date = datetime.now().strftime("%d, %A, %B")
            student = Student(
                self.first_name.value,
                self.last_name.value,
                self.age.value,
                self.phone_number.value,
                self.email.value,
                self.course.value,
                self.gender.value,
                self.grade.value,
                current_date
            )
            # #  ------------------// calling the update function from the class here----------//
            student.update_student_record(self.editDelete_id)
            self.update_dlg_modal.open = False
            #  -----------------// the success message here---------------------//
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0078D9",
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "student record updated successfully".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
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
