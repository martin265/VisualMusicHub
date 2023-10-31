import flet as ft
from classes.notes import Note
from datetime import datetime
from classes.samples import Sample


class Notes(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ------------------//-----------------------------//--------------------//\
        self.save_file_path = ft.Text()

        #  ------------------saving files trial here--------------------//
        # self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_dialog)
        #  -----------------------the controls for the file uploads here--------------//
        self.file_name = ft.TextField(
            width=500,
            height=100,
            hint_text="file name".capitalize(),
            capitalization=ft.TextCapitalization.CHARACTERS,
            prefix_icon=ft.icons.FILE_UPLOAD,
            helper_text="make sure to provide file name".capitalize(),
            keyboard_type=ft.KeyboardType.NAME,
            border_color=ft.colors.WHITE,
            border_width=2,
            border_radius=ft.border_radius.all(5),
            helper_style=ft.TextStyle(
                color="white",
                size=15
            ),
            hint_style=ft.TextStyle(
                color="white",
                size=15
            ),
        )
        #  ------------------------//-----------------------//
        self.file_description = ft.TextField(
            width=500,
            height=100,
            hint_text="file description".capitalize(),
            capitalization=ft.TextCapitalization.CHARACTERS,
            prefix_icon=ft.icons.DESCRIPTION_ROUNDED,
            helper_text="make sure to provide some description".capitalize(),
            keyboard_type=ft.KeyboardType.NAME,
            border_color=ft.colors.WHITE,
            border_width=2,
            multiline=True,
            max_lines=20,
            border_radius=ft.border_radius.all(5),
            helper_style=ft.TextStyle(
                color="white",
                size=15
            ),
            hint_style=ft.TextStyle(
                color="white",
                size=15
            ),

        )

        #  ------------------------the upload alert dialog here for the system---------------//
        self.upload_file_dialog = ft.AlertDialog(
            title=ft.Text(
                "file upload".capitalize(),
            ),
            content=ft.Text(
                "confirm your upload"
            ),
            actions=[
                ft.TextButton("Yes", on_click=self.save_uploaded_samples),
                ft.TextButton("No", on_click=self.close_dialog)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        #  --------------------------//sample upload dialog------------------------------//
        self.upload_sample_dialog = ft.AlertDialog(
            title=ft.Text(
                "sample upload".capitalize(),
            ),
            content=ft.Text(
                "confirm your upload"
            ),
            actions=[
                ft.TextButton("Yes", on_click=self.save_samples),
                ft.TextButton("No", on_click=self.close_samples_dialog)
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        #  -------------------------/sample collection/------------------------------------------//
        self.sample_name = ft.TextField(
            width=500,
            height=100,
            hint_text="sample name".capitalize(),
            capitalization=ft.TextCapitalization.CHARACTERS,
            prefix_icon=ft.icons.SPEAKER_NOTES_ROUNDED,
            helper_text="make sure to provide sample name".capitalize(),
            keyboard_type=ft.KeyboardType.NAME,
            border_color=ft.colors.WHITE,
            border_width=2,
            multiline=True,
            max_lines=20,
            border_radius=ft.border_radius.all(5),
            helper_style=ft.TextStyle(
                color="white",
                size=15
            ),
            hint_style=ft.TextStyle(
                color="white",
                size=15
            ),

        )
        #  ------------------//sample description----------------------//
        self.sample_description = ft.TextField(
            width=500,
            height=100,
            hint_text="sample description".capitalize(),
            capitalization=ft.TextCapitalization.CHARACTERS,
            prefix_icon=ft.icons.DESCRIPTION_ROUNDED,
            helper_text="make sure to provide some description".capitalize(),
            keyboard_type=ft.KeyboardType.NAME,
            border_color=ft.colors.WHITE,
            border_width=2,
            multiline=True,
            max_lines=20,
            border_radius=ft.border_radius.all(5),
            helper_style=ft.TextStyle(
                color="white",
                size=15
            ),
            hint_style=ft.TextStyle(
                color="white",
                size=15
            ),

        )

    #  --------------------------/function to validate the uploaded samples/-----------------------------------------//
    def validate_samples(self, e):
        """the function will be used to validate the sample inputs"""
        try:
            if not self.sample_name.value:
                self.sample_name.error_text = "enter sample name".capitalize()
                self.update()
            elif not self.sample_description.value:
                self.sample_description.error_text = "fill in the sample description".capitalize()
                self.update()
            else:
                self.open_samples_modal()
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

    #  ----------------------//function to validate the field inputs here---------------//
    def validate_inputs(self, e):
        try:
            if not self.file_name.value:
                self.file_name.error_text = "provide the file name first name".capitalize()
                self.update()
            #  ----------------------------//------------------------------------//
            elif not self.file_description.value:
                self.file_description.error_text = "provide the description".capitalize()
                self.update()
            else:
                self.open_dialog_modal()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text("something went wrong at {}".format(ex))
                        ]
                    )
                )
            )
            self.page.update()

    #  ----------------------function to trigger the modal---------------//
    def open_dialog_modal(self):
        try:
            self.page.dialog = self.upload_file_dialog
            self.upload_file_dialog.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  --------------------function to open the dialog modal here---------------//
    def save_uploaded_files(self, e):
        try:
            self.save_notes()
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "lyrics files uploaded successfully"
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.upload_file_dialog.open = False
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  ---------------------function to close the dialog modal-----------------//
    def close_dialog(self, e):
        try:
            self.upload_file_dialog.open = False
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  --------------------closing the samples modal here--------------------//
    def close_samples_dialog(self, e):
        try:
            self.upload_sample_dialog.open = False
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  -------------------------//opening the samples modal here----------------------//
    def open_samples_modal(self):
        try:
            self.page.dialog = self.upload_sample_dialog
            self.upload_sample_dialog.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    #  ----------------------the function to save the voice samples----------------//
    def save_uploaded_samples(self):
        try:
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0050C1",
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "sample files uploaded successfully"
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.upload_file_dialog.open = False
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
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
            controls=[
                #  -----------------the main container----------------------//
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(left=10),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Text(
                                            "notes".capitalize(),
                                            style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                                            color="#311B92"
                                        ),
                                    ]
                                )
                            ),
                            ft.Container(
                                width=1220,
                                margin=ft.margin.only(left=10, top=20, right=10),
                                padding=ft.padding.only(left=10, right=30, top=30, bottom=30),
                                bgcolor="#F2ECFF",
                                border_radius=ft.border_radius.all(10),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[

                                        #  -------------------//----------------------//
                                        ft.Container(
                                            width=550,
                                            height=600,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#0050C1",
                                                    "#A50084"
                                                ],
                                                begin=ft.alignment.bottom_left,
                                                end=ft.alignment.bottom_right
                                            ),
                                            content=ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        margin=ft.margin.only(top=40),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.MIC_ROUNDED,
                                                                    size=100,
                                                                    color="white",
                                                                )
                                                            ]
                                                        ),
                                                    ),
                                                    #  -------------the container for the text--------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "upload some lyrics".capitalize(),
                                                                    size=30,
                                                                    color="white",
                                                                    weight=ft.FontWeight.W_700
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  ------------------the container for the text boxes---------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        self.file_name
                                                                    ]
                                                                ),
                                                                #  -----------------// file description--------//
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        self.file_description
                                                                    ]
                                                                ),
                                                                ft.Container(
                                                                    margin=ft.margin.only(left=20, top=30),
                                                                    content=ft.Row(
                                                                        controls=[
                                                                            ft.ElevatedButton(
                                                                                on_click=self.validate_inputs,
                                                                                text="upload file".capitalize(),
                                                                                elevation=True,
                                                                                width=200,
                                                                                height=50,
                                                                                icon=ft.icons.UPLOAD_FILE_ROUNDED,
                                                                                icon_color="#0050C1",
                                                                            ),
                                                                            #  --------------button to pick the files--
                                                                            ft.ElevatedButton(
                                                                                "Save file",
                                                                                icon=ft.icons.SAVE,
                                                                                on_click=lambda
                                                                                    _: self.save_file_dialog.save_file(),
                                                                                disabled=self.page.web,
                                                                            ),
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        #  ---------------------//-------------------//
                                        ft.Container(
                                            width=550,
                                            height=600,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#0050C1",
                                                    "#A50084"
                                                ],
                                                begin=ft.alignment.bottom_left,
                                                end=ft.alignment.bottom_right
                                            ),
                                            content=ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        margin=ft.margin.only(top=40),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Icon(
                                                                    ft.icons.LIBRARY_MUSIC_ROUNDED,
                                                                    size=100,
                                                                    color="white",
                                                                )
                                                            ]
                                                        ),
                                                    ),
                                                    #  -------------the container for the text--------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "upload some voice samples".capitalize(),
                                                                    size=30,
                                                                    color="white",
                                                                    weight=ft.FontWeight.W_700
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  ------------------the container for the text boxes---------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=30),
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        self.sample_name
                                                                    ]
                                                                ),
                                                                #  -----------------// file description--------//
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        self.sample_description
                                                                    ]
                                                                ),
                                                                ft.Container(
                                                                    margin=ft.margin.only(left=20, top=30),
                                                                    content=ft.Row(
                                                                        controls=[
                                                                            ft.ElevatedButton(
                                                                                on_click=self.validate_samples,
                                                                                text="upload file".capitalize(),
                                                                                elevation=True,
                                                                                width=200,
                                                                                height=50,
                                                                                icon=ft.icons.DRIVE_FOLDER_UPLOAD_ROUNDED,
                                                                                icon_color="#0050C1",
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
                            #  ------------------------------//---------------------------//

                        ]
                    )
                )
            ]
        )

    #  -------------------------functions to insert the new notes into the database-------------//
    def save_notes(self):
        try:
            current_date = datetime.now().strftime("%d, %A, %B")
            notes = Note(
                self.file_name.value,
                self.file_description.value,
                current_date
            )
            notes.upload_new_notes()
            self.clear_text_fields()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Column(
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

    #  ---------------------function to clear the text boxes after successfully uploading files
    def clear_text_fields(self):
        try:
            self.file_name.value = ""
            self.file_description.value = ""
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Column(
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

    #  ------------------------------//closing the save process for the notes--------------------//
    def save_recorded_samples(self):
        try:
            current_date = datetime.now().strftime("%d, %A, %B")
            sample = Sample(
                self.sample_name.value,
                self.sample_description.value,
                current_date
            )
            sample.upload_new_samples()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Column(
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

    #  ---------------------saving the samples here-------------------------//
    def save_samples(self, e):
        try:
            current_date = datetime.now().strftime("%d, %A, %B")
            samples = Sample(
                self.sample_name.value,
                self.sample_description.value,
                current_date
            )
            samples.upload_new_samples()
            self.clear_text_fields()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Column(
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

    #  ----------------------the function will be used to pick the files and upload them here--------//
    # Pick files dialog
    # Save file dialog
    def save_file_result(self, e: ft.FilePickerResultEvent):
        self.save_file_path.value = e.path if e.path else "Cancelled!"
        self.save_file_path.update()

    save_file_dialog = ft.FilePicker(on_result=save_file_result)
