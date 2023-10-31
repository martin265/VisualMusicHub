import flet as ft
from classes.students import Student
from datetime import datetime


class Students(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.editDelete_id = ft.Text()
        #  --------------the controls for collecting the student details--------------//
        self.first_name = ft.TextField(
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            width=580,
            height=100,
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            helper_text="characters only",
            border_color="#0d47a1",
            label="first name".capitalize(),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#1565c0",
            keyboard_type=ft.KeyboardType.NAME
        )
        #  ------------------------//---------------------------//-------------------//
        self.last_name = ft.TextField(
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            width=580,
            height=100,
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            helper_text="characters only",
            border_color="#0d47a1",
            label="last name".capitalize(),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#1565c0",
            keyboard_type=ft.KeyboardType.NAME,
            border_width=2
        )
        #  ------------------------//---------------------------//-------------------//
        self.age = ft.TextField(
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            width=580,
            height=100,
            prefix_icon=ft.icons.NUMBERS_ROUNDED,
            helper_text="numbers only",
            border_color="#0d47a1",
            label="age".capitalize(),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#1565c0",
            keyboard_type=ft.KeyboardType.NAME,
            border_width=2
        )
        #  ------------------------//---------------------------//-------------------//
        self.phone_number = ft.TextField(
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            width=580,
            height=100,
            prefix_icon=ft.icons.PHONE_ANDROID_ROUNDED,
            helper_text="numbers only",
            border_color="#0d47a1",
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
            width=580,
            height=100,
            prefix_icon=ft.icons.EMAIL_ROUNDED,
            helper_text="characters only",
            border_color="#0d47a1",
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
            width=580,
            height=100,
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
            width=580,
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
        #  ------------------------------//----------------------------//
        
    #  ---------------------------the function to make the input validations will be here--------//
    def validate_inputs(self, e):
        """the validations for the inputs will be here"""
        if not self.first_name.value:
            self.first_name.error_text = "fill in for the first name please".capitalize()
            self.update()
        #  --------------------------//------------------------------//--------//
        elif not self.last_name.value:
            self.last_name.error_text = "fill in for the last name".capitalize()
            self.update()
        #  -------------------------------//-----------------------------------//
        elif not self.age.value:
            self.age.error_text = "enter your age first".capitalize()
            self.update()
        #  ------------------------------------//-------------------------------//
        elif not self.phone_number.value:
            self.phone_number.error_text = "select your gender".capitalize()
            self.update()
        #  -------------------------------//------------------------------------//
        elif not self.email.value:
            self.email.error_text = "select current address".capitalize()
            self.update()
        #  ---------------------------------------//------------------------------//
        elif not self.course.value:
            self.course.error_text = "select your course".capitalize()
            self.update()
        #  -----------------------------------//-------------------------------------//
        elif not self.gender.value:
            self.gender.error_text = "select gender".capitalize()
            self.update()
        #  ---------------------------------//
        elif not self.grade.value:
            self.grade.error_text = "select grade".capitalize()
            self.update()
        else:
            self.save_students_record()

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1220,
            height=700,
            controls=[
                #  ------------------this container will house everything within the app-----------//
                ft.Container(
                    content=ft.Column(
                        controls=[
                            #  ------------------some of the container components that will be included-------//
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Text(
                                                    "student details".capitalize(),
                                                    style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                                    color="#0d47a1",
                                                    weight=ft.FontWeight.W_700
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ),
                            #  ---------------the container for the main controls-------------------//
                            ft.Container(
                                width=1220,
                                margin=ft.margin.only(left=10, top=20, right=10),
                                padding=ft.padding.only(left=10, right=30, top=30, bottom=30),
                                bgcolor="#F2ECFF",
                                border_radius=ft.border_radius.all(10),
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Container(
                                                    margin=ft.margin.only(bottom=30),
                                                    width=200,
                                                    height=150,
                                                    border_radius=ft.border_radius.all(10),
                                                    gradient=ft.LinearGradient(
                                                        colors=[
                                                            "#00B4C6",
                                                            "#007BDD"
                                                        ],
                                                        begin=ft.alignment.bottom_left,
                                                        end=ft.alignment.top_right,
                                                    ),
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Icon(
                                                                ft.icons.MUSIC_NOTE_ROUNDED,
                                                                size=90,
                                                                color="white"
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                self.first_name,
                                                self.last_name
                                            ]
                                        ),
                                        #  -------------------the row for the other controls-------//
                                        ft.Row(
                                            controls=[
                                                self.age,
                                                self.phone_number
                                            ]
                                        ),
                                        # ----------------------------//---------------------------//
                                        ft.Row(
                                            controls=[
                                                self.email,
                                                self.course
                                            ]
                                        ),
                                        #  --------------------------------//--------------------//
                                        ft.Row(
                                            controls=[
                                                self.grade,
                                                self.gender,
                                            ]
                                        ),
                                        #  ---------------------the buttons---------------//
                                        ft.Row(
                                            controls=[
                                                ft.ElevatedButton(
                                                    on_click=self.validate_inputs,
                                                    text="save details",
                                                    icon=ft.icons.SAVE_ROUNDED,
                                                    height=60,
                                                    width=200,
                                                    color="white",
                                                    bgcolor="#0050C1"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                            #  ------------------------//---------------------------//
                        ]
                    )
                )
            ]
        )

    # --------------------the function to add a new student into the database
    def save_students_record(self):
        """the function to add a new student to the main database"""
        try:
            current_date = datetime.now().strftime("%d, %A, %B")
            student = Student(self.first_name.value, self.last_name.value, self.age.value, self.gender.value,
                              self.grade.value, self.phone_number.value, self.email.value, self.course.value,
                              current_date)
            student.add_new_student_details()
            #  ----------------displaying the snack bar here--------------//
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "record saved successfully"
                            )
                        ]
                    )
                ),
                action="okay"
            )
            self.page.snack_bar.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Text(
                        "something went wrong check your connection {}".format(ex).title()
                    )
                ),
                action="ok".title()
            )
            self.page.snack_bar.open = True
            self.page.update()

