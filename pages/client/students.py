import flet as ft
from classes.students import Student
from datetime import datetime


class Students(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  -------------------getting input from the student----------------------//
        self.first_name = ft.TextField(
            width=580,
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
            width=580,
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
            width=580,
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
            width=580,
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
            width=580,
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
            width=580,
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
        #   --------------------//confirmation pop message---------------//
        self.confirmation_alert = ft.AlertDialog(
            modal=True,
            actions_alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            content=ft.Container(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            src="assets/stickers/hip-hop.png",
                            height=200,
                            width=200
                        )
                    ]
                )
            ),
            title=ft.Text(
                "confirm account creation".capitalize()
            ),
            title_padding=ft.padding.only(left=30),
            actions=[
                ft.ElevatedButton(
                    text="cancel account creation".capitalize(),
                    on_click=self.close_confirmation_modal,
                    icon=ft.icons.CANCEL_ROUNDED,
                    icon_color="red",
                    height=50
                ),
                #  -------------------------//--------------------------//
                ft.ElevatedButton(
                    text="proceed creation".capitalize(),
                    on_click=self.save_student_details,
                    icon=ft.icons.CONFIRMATION_NUM_ROUNDED,
                    height=50,
                    icon_color="#00DCBB"
                ),
                #  ----//----------------//

            ]
        )

    def validate_inputs(self, e):
        """the function will validate the input before saving the actual records"""
        try:
            if not self.first_name.value:
                self.first_name.error_text = "enter your first name".capitalize()
                self.update()
            #  -------------------//-----------------------//-------------------//
            elif not self.last_name.value:
                self.last_name.error_text = "enter last name first".capitalize()
                self.update()
            # ------------------------//------------------//------------------//
            elif not self.age.value:
                self.age.error_text = "provide your age".capitalize()
                self.update()
            #  ----------------------//--------------------//-------------------//
            elif not self.gender.value:
                self.gender.error_text = "provide your gender".capitalize()
                self.update()
            #  ------------------------//-------------------//-------------------//
            elif not self.grade.value:
                self.grade.error_text = "select grade first".capitalize()
                self.update()
            #  -----------------------//---------------------//----------------//
            elif not self.phone_number.value:
                self.phone_number.error_text = "enter your phone number".capitalize()
                self.update()
            #  ---------------------//-----------------------//----------------//
            elif not self.email.value:
                self.email.error_text = "enter your email".capitalize()
                self.update()
            #  -------------------------------//----------------//-----------//
            elif not self.course.value:
                self.course.error_text = "select course".capitalize()
                self.update()
            else:
                self.trigger_confirmation_popup()

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

    #  -------------------//function for the pop up menu here-------------------//
    def trigger_confirmation_popup(self):
        try:
            self.page.dialog = self.confirmation_alert
            self.confirmation_alert.open = True
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

    #  --------------------//functions to close the confirmation modal here------------//
    def close_confirmation_modal(self, e):
        try:
            self.page.dialog = self.confirmation_alert
            self.confirmation_alert.open = False
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

    #  -----------------the interface controls for the system here-----------//
    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1220,
            height=700,
            #  -------------------the main controls will be here-----------------//
            controls=[
                #  -----------------the main container to house the systems---//
                ft.Container(
                    bgcolor="#eceff1",
                    border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        auto_scroll=True,
                        scroll=ft.ScrollMode.HIDDEN,
                        controls=[
                            #  ----------------------//---------------------------//
                            ft.Container(
                                width=1400,
                                border_radius=ft.border_radius.all(10),
                                margin=ft.margin.only(left=20, right=20, top=20),
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "register your details".capitalize(),
                                            color="#0050C1",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                                            weight=ft.FontWeight.W_700
                                        )
                                    ]
                                )
                            ),
                            #  --------------------container for the input controls----------//
                            ft.Container(
                                margin=ft.margin.only(left=20, top=40),
                                content=ft.Column(
                                    controls=[
                                        ft.Row([self.first_name, self.last_name]),
                                        ft.Row([self.age, self.gender]),
                                        ft.Row([self.grade, self.phone_number]),
                                        ft.Row([self.email, self.course]),
                                        #  -----------------------the controls for the buttons here---------//
                                        ft.Container(
                                            margin=ft.margin.only(bottom=20, right=30),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                controls=[
                                                    ft.ElevatedButton(
                                                        icon=ft.icons.SAVE_AS_ROUNDED,
                                                        icon_color="",
                                                        height=60, width=200,
                                                        text="register".title(),
                                                        elevation=None,
                                                        style=ft.ButtonStyle(
                                                            bgcolor="#0050C1",
                                                            color="white",

                                                        ),
                                                        #  ------------the click function-------//
                                                        on_click=self.validate_inputs,
                                                    ),
                                                    #  ------------------//button to clear the fields here------//
                                                    ft.ElevatedButton(
                                                        icon=ft.icons.CLEAR_ROUNDED,
                                                        icon_color="",
                                                        height=60, width=200,
                                                        text="clear fields".title(),
                                                        elevation=None,
                                                        style=ft.ButtonStyle(
                                                            bgcolor="#4A4453",
                                                            color="white",

                                                        ),
                                                        #  ------------the click function-------//
                                                        on_click=self.clear_text_fields_btn,
                                                    ),
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

    #  -----------------------------//function to save the details to the database-------------//
    def save_student_details(self, e):
        try:
            current_date = datetime.now().strftime("%d, %A, %B")
            student = Student(self.first_name.value, self.last_name.value, self.age.value, self.gender.value,
                              self.grade.value, self.phone_number.value, self.email.value, self.course.value,
                              current_date)
            student.add_new_student_details()
            #  --------------------the confirmation snack bar here---------------//
            self.page.dialog = self.confirmation_alert
            self.confirmation_alert.open = False
            #  -------------------opening the snack bar here-----------------//
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0078D9",
                content=ft.Container(
                    height=50,
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "course registered successfully".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.clear_text_fields()
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

    #  --------------------------// function to clear the text boxes here---------------//
    def clear_text_fields(self):
        try:
            self.first_name.value = ""
            self.last_name.value = ""
            self.age.value = ""
            self.grade.value = ""
            self.phone_number.value = ""
            self.email.value = ""
            self.course.value = ""
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

    #  --------------------------// function to clear the text boxes here---------------//
    def clear_text_fields_btn(self, e):
        try:
            self.first_name.value = ""
            self.last_name.value = ""
            self.age.value = ""
            self.grade.value = ""
            self.phone_number.value = ""
            self.email.value = ""
            self.course.value = ""
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
