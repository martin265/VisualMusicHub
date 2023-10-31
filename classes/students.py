import sqlite3
from connection.db_connection import my_connection


class Student:
    """the student class will house every student detail"""

    def __init__(self, first_name, last_name, age, gender, grade, phone_number, email, course, current_date):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.grade = grade
        self.phone_number = phone_number
        self.email = email
        self.course = course
        self.current_date = current_date
        self.database_cursor = my_connection.cursor()

        #  --------------method to add new student to the details-----------------//

    def add_new_student_details(self):
        """the method to add a new student to the system"""
        try:
            sql = "INSERT INTO Students(first_name, last_name, age, gender, grade, phone_number, email, course, registered_date) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (self.first_name, self.last_name, self.age, self.gender, self.grade, self.phone_number, self.email,
                   self.course, self.current_date)
            self.database_cursor.execute(sql, val)
            my_connection.commit()

        except Exception as ex:
            print(ex)

    #  ---------------method to update the student records------------------//
    def update_student_record(self, current_student_id):
        """the method to update the student records here for the system"""
        try:
            sql = "UPDATE Students SET first_name = %s, last_name = %s, age = %s, phone_number=%s, email = %s, course = %s, gender = %s, grade = %s WHERE id = %s"
            values = (
                self.first_name, self.last_name, self.age, self.phone_number, self.email, self.course, self.gender,
                self.grade, current_student_id)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)

    #  ---------------method to update the student records------------------//
    def delete_student_record(self, current_student_id):
        """the method to delete the student records here for the system"""
        try:
            sql = "DELETE FROM Students WHERE id = %s"
            values = (current_student_id,)
            self.database_cursor.execute(sql, values)
            my_connection.commit()
        except Exception as ex:
            print(ex)
