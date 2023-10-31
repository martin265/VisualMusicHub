from connection.db_connection import my_connection
from datetime import datetime


class Sample:
    def __init__(self, sample_name, sample_description, sample_uploaded_date):
        self.sample_name = sample_name
        self.sample_description = sample_description
        self.sample_uploaded_date = sample_uploaded_date
        self.database_cursor = my_connection.cursor()

    #  ----------------the function will insert new note into the database----------------//
    def upload_new_samples(self):
        """the function will be used to upload new notes"""
        try:
            sql = "INSERT INTO Samples(sample_name, sample_description, sample_uploaded_date) VALUES (%s, %s, %s)"
            val = (self.sample_name, self.sample_description, self.sample_uploaded_date)
            self.database_cursor.execute(sql, val)
            my_connection.commit()
        except Exception as ex:
            print(ex)
