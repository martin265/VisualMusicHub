import flet as ft
import pyaudio
import os
import wave


# ------------------this page will be a great success by the help of our Lord Jesus Christ----//
class Studios(ft.UserControl):
    """the class that will house all the controls"""

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.duration = float(30)
        self.recordings_path = "recordings"
        self.output_folder = "recordings"  # Change this to the folder where you want to save the recordings
        self.filename = "recordings"  # Change this to the desired filename
        self.record_duration = 10  # Change this to adjust the recording duration (in seconds)
        self.single_recording = ft.Text()
        #  --------------------the input controls here for the recording---------//
        self.microphone = ft.Dropdown(
            width=300,
            height=100,
            autofocus=True,
            prefix_icon=ft.icons.MIC_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",

            ),
            helper_text="select your active microphone",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="active mic".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="white",

        )
        #  ---------------------// getting the recording channel here-----------------//
        self.recording_channel = ft.Dropdown(
            width=300,
            height=100,
            autofocus=True,
            prefix_icon=ft.icons.WIFI_CHANNEL_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",

            ),
            helper_text="select your active channel",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="active channel".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="white",
        )
        #  ------------------------------//getting the recording duration here----------//
        self.recording_duration = ft.TextField(
            width=300,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.TIMELAPSE_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",

            ),
            helper_text="numbers only",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="recording duration".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="white",
            keyboard_type=ft.KeyboardType.NAME,
            color="white",
        )
        #  ---------------------//getting the file name here for the recording--------------//
        self.recording_filename = ft.TextField(
            width=300,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.FILE_OPEN_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",

            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="recording filename".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="white",
            color="white",
            keyboard_type=ft.KeyboardType.NAME
        )

        #  ---------------------the grid view for the audio files here-----------------//
        self.audio_gallery = ft.GridView(
            runs_count=4,
            expand=True,
            max_extent=300,
            spacing=10
        )

        #  -------------------------the drop down for the audio file--------------//
        self.recorded_files = ft.Dropdown(
            width=400,
            height=100,
            autofocus=True,
            prefix_icon=ft.icons.MUSIC_NOTE_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",
            ),
            helper_text="select your recordings",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="recordings".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="white",
        )
        #  --------------------------the audio control----------------------//

        self.audio1 = ft.Audio(
            src=f"{self.filename} {self.single_recording}",
            autoplay=False,
            volume=1,
            balance=0,
        )
        self.page.overlay.append(self.audio1)

    #   -------------------------//------------------------------//
    def get_current_audio_file(self):
        try:
            print(self.single_recording)
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

    def fetch_all_recorded_files(self):
        try:
            for self.single_recording in os.listdir(self.recordings_path):
                self.recorded_files.options.append(
                    ft.dropdown.Option(
                        self.single_recording
                    )
                )

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

    #  ----------------//validating the input fields-------------------------//
    def validate_input_fields(self, e):
        """the function to validate the input fields here--------"""
        try:
            if not self.microphone.value:
                self.microphone.error_text = "select active mic first".capitalize()
                self.update()
            #  ----------------------------//-------------------------------------//
            elif not self.recording_channel.value:
                self.recording_channel.error_text = "select active channel".capitalize()
                self.update()
            #  --------------------------------//---------------------------------//
            elif not self.recording_duration.value:
                self.recording_duration.error_text = "enter the time to record".capitalize()
                self.update()
            #  -------------------------------------//-------------------------------//
            elif not self.recording_filename.value:
                self.recording_filename.error_text = "enter the filename for saving".capitalize()
                self.update()
            #  -------------------------------------//-----------------------------------//
            else:
                self.record_audio(self.output_folder, self.recording_filename.value + ".wav",
                                  duration=int(self.recording_duration.value))

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

    #  -----------------------getting all the available microphones------------------//
    def list_microphones(self):
        p = pyaudio.PyAudio()

        device_count = p.get_device_count()

        for i in range(device_count):
            device_info = p.get_device_info_by_index(i)
            device_name = device_info["name"]
            device_is_input = device_info["maxInputChannels"] > 0

            if device_is_input:
                self.microphone.options.append(
                    ft.dropdown.Option(
                        device_name
                    )
                )

        p.terminate()

    #  -----------------------//--------------------------//
    def volume_down(self, _):
        self.audio1.volume -= 0.1
        self.audio1.update()

    #  -------------------------the volume up control-------------//
    def volume_up(self, _):
        self.audio1.volume += 0.1
        self.audio1.update()

    def build(self):
        self.list_microphones()
        self.show_active_channels()
        self.fetch_all_recordings()
        self.fetch_all_recorded_files()
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            width=1220,
            height=700,
            controls=[
                #  ------------------------the main container for the system here---------//
                ft.Container(
                    bgcolor="#eceff1",
                    width=1320,
                    height=700,
                    border_radius=ft.border_radius.all(10),
                    content=ft.Column(
                        controls=[
                            #  ---------------the container for the top most test
                            ft.Container(
                                margin=ft.margin.only(left=20),
                                content=ft.Row(
                                    controls=[
                                        ft.Text(
                                            "studio time".capitalize(),
                                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                                            color="#0078D9"
                                        )
                                    ]
                                )
                            ),
                            #  -------------------the container for the main recording panel-----//

                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            height=550,
                                            width=700,
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
                                                                    height=200,
                                                                    width=200
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  -------------------the container for the input fields---------//
                                                    ft.Container(
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        self.microphone,
                                                                        self.recording_channel
                                                                    ]
                                                                ),
                                                                #  ---------------//thank you Jesus Christ-------//
                                                                ft.Row(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    controls=[
                                                                        self.recording_duration,
                                                                        self.recording_filename
                                                                    ]
                                                                ),
                                                                #  ------------------------/help me please/-----------------//
                                                                ft.Container(
                                                                    margin=ft.margin.only(top=30, left=40, right=40),
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                        controls=[
                                                                            ft.ElevatedButton(
                                                                                icon=ft.icons.RECORD_VOICE_OVER_ROUNDED,
                                                                                icon_color="",
                                                                                height=60, width=300,
                                                                                text="start recording session".title(),
                                                                                elevation=None,
                                                                                style=ft.ButtonStyle(
                                                                                    bgcolor="#4A4453",
                                                                                    color="white",

                                                                                ),
                                                                                #  ------------the click function-------//
                                                                                on_click=self.validate_input_fields,
                                                                            ),
                                                                            #  ----------------------//--------------------------//
                                                                            ft.ElevatedButton(
                                                                                icon=ft.icons.CLOSE_ROUNDED,
                                                                                icon_color="red",
                                                                                height=60, width=200,
                                                                                text="clear fields".title(),
                                                                                elevation=None,
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
                                                    )
                                                ]
                                            )
                                        ),
                                        #  -----------------------the container for the previews here---------//
                                        ft.Container(
                                            height=550,
                                            width=480,
                                            #  ------------setting up the colors here----------//
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#0050C1",
                                                    "#FF7451"
                                                ],
                                                begin=ft.alignment.bottom_left,
                                                end=ft.alignment.top_right
                                            ),
                                            margin=ft.margin.only(top=10),
                                            border_radius=ft.border_radius.all(10),
                                            content=ft.Column(
                                                controls=[
                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, top=10),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "preview your recordings".capitalize(),
                                                                    style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                                                    weight=ft.FontWeight.W_700,
                                                                    color="white"
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    #  -----------------the container for the audio files-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=20),
                                                        content=ft.Column(
                                                            controls=[

                                                                ft.Container(
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            ft.Image(
                                                                                height=220,
                                                                                width=200,
                                                                                src="assets/stickers/people.png"
                                                                            )
                                                                        ]
                                                                    )
                                                                ),
                                                                #  -------------------------//------------------//
                                                                ft.Container(
                                                                    margin=ft.margin.only(top=20),
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            self.recorded_files
                                                                        ]
                                                                    )
                                                                ),
                                                                #  -----------------the rows for the media player
                                                                ft.Container(
                                                                    margin=ft.margin.only(left=20, top=10),
                                                                    content=ft.Row(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        controls=[
                                                                            ft.IconButton(
                                                                                icon=ft.icons.PLAY_ARROW_ROUNDED,
                                                                                icon_size=40,
                                                                                icon_color="black",
                                                                                tooltip="play",
                                                                                bgcolor="#f5f5f5",
                                                                                on_click=lambda
                                                                                    _: self.audio1.play()
                                                                            ),
                                                                            ft.IconButton(
                                                                                icon=ft.icons.PAUSE_ROUNDED,
                                                                                icon_size=40,
                                                                                icon_color="black",
                                                                                bgcolor="#f5f5f5",
                                                                                tooltip="pause".title(),
                                                                                on_click=lambda
                                                                                    _: self.audio1.pause()
                                                                            ),
                                                                            ft.IconButton(
                                                                                icon=ft.icons.VOLUME_DOWN_ROUNDED,
                                                                                icon_size=40,
                                                                                icon_color="black",
                                                                                bgcolor="#f5f5f5",
                                                                                tooltip="volume down".title(),
                                                                                on_click=self.volume_down
                                                                            ),
                                                                            ft.IconButton(
                                                                                icon=ft.icons.VOLUME_UP_ROUNDED,
                                                                                icon_size=40,
                                                                                icon_color="black",
                                                                                bgcolor="#f5f5f5",
                                                                                tooltip="volume up".title(),
                                                                                on_click=self.volume_up
                                                                            ),
                                                                            #  -----------------the seek and resume----//
                                                                            ft.IconButton(
                                                                                icon=ft.icons.ROTATE_90_DEGREES_CW_ROUNDED,
                                                                                icon_size=40,
                                                                                icon_color="black",
                                                                                bgcolor="#f5f5f5",
                                                                                tooltip="release".title(),
                                                                                on_click=self.audio1.release()
                                                                            ),
                                                                            #  ----------------------//---------------//
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

                            #  -------------------for the love of God we have faith and hope----------//
                        ]
                    )
                )
            ]
        )

    #  ------------------function to clear the text fields-----------------------------------//
    def clear_text_fields(self, e):
        try:
            self.recording_channel.value = ""
            self.recording_duration.value = ""
            self.recording_filename.value = ""
            self.microphone.value = ""
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

    #  --------------------------//the function to list all the available channels here-------------------//
    def show_active_channels(self):
        try:
            py_audios = pyaudio.PyAudio()
            for channel in py_audios.get_default_input_device_info():
                self.recording_channel.options.append(
                    ft.dropdown.Option(
                        channel
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

    #  ----------------------------function to start the recorder here------------------------//
    def record_audio(self, output_folder, filename, duration=5, channels=1, sample_rate=44100):
        # Initialize PyAudio
        audio = pyaudio.PyAudio()

        # Configure the audio stream
        stream = audio.open(format=pyaudio.paInt16,
                            channels=channels,
                            rate=sample_rate,
                            input=True,
                            frames_per_buffer=1024)

        # Start recording
        self.page.snack_bar = ft.SnackBar(
            bgcolor="#0050C1",
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "your recording has started".capitalize(),
                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                            weight=ft.FontWeight.W_700,
                            color="white"
                        )
                    ]
                )
            )
        )
        self.page.snack_bar.open = True
        self.page.update()

        frames = []
        for _ in range(0, int(sample_rate / 1024 * duration)):
            data = stream.read(1024)
            frames.append(data)

        # finished recording
        self.page.snack_bar = ft.SnackBar(
            bgcolor="#0050C1",
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "finished recording".capitalize(),
                            style=ft.TextThemeStyle.DISPLAY_SMALL,
                            weight=ft.FontWeight.W_700,
                            color="white"
                        )
                    ]
                )
            )
        )
        self.page.snack_bar.open = True
        self.page.update()

        # Stop and close the audio stream
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save the recorded audio to a WAV file
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        file_path = os.path.join(output_folder, filename)
        with wave.open(file_path, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))

        print(f"Audio saved to {file_path}")

    #  -------------------------the function will be used to fetch all the recordings in the folder---------//
    def fetch_all_recordings(self):
        try:
            for single_recording in os.listdir(self.recordings_path):
                self.audio_gallery.controls.append(
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Row(
                                                controls=[
                                                    ft.Image(
                                                        width=100,
                                                        src=f"https://cdn-icons-gif.flaticon.com/9538/9538503.gif"
                                                    )
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            ft.Text("some text here")
                                        ),
                                    ]
                                )
                            ]
                        )
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
