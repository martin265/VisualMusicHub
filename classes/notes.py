from connection.db_connection import my_connection
from datetime import datetime


class Note:
    def __init__(self, note_name, note_description, note_uploaded_date):
        self.note_name = note_name
        self.note_description = note_description
        self.note_uploaded_date = note_uploaded_date
        self.database_cursor = my_connection.cursor()

    #  ----------------the function will insert new note into the database----------------//
    def upload_new_notes(self):
        """the function will be used to upload new notes"""
        try:
            sql = "INSERT INTO Notes(note_name, note_description, note_uploaded_date) VALUES (%s, %s, %s)"
            val = (self.note_name, self.note_description, self.note_uploaded_date)
            self.database_cursor.execute(sql, val)
            my_connection.commit()
        except Exception as ex:
            print(ex)
