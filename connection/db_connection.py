import mysql.connector

#  ---------the function to create the new table here-------------//
try:
    my_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="MusicHub"
    )
    if my_connection:
        print("")
    else:
        print("failed to connect with the database")
except Exception as ex:
    print(ex)


# ---------------------creating the actual tables here for the system---------------//
def create_students_table():
    try:
        database_cursor = my_connection.cursor()
        sql = "CREATE TABLE Students(" \
              "id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY," \
              "first_name VARCHAR(40) NOT NULL," \
              "last_name VARCHAR(40) NOT NULL," \
              "age VARCHAR(30) NOT NULL," \
              "phone_number VARCHAR(40) NOT NULL," \
              "email VARCHAR(40) NOT NULL," \
              "course VARCHAR(40) NOT NULL," \
              "gender VARCHAR(40) NOT NULL," \
              "grade VARCHAR(40) NOT NULL," \
              "registered_date VARCHAR(40) NOT NULL)"
        database_cursor.execute(sql)
    except Exception as ex:
        print(ex)


# ----------------------//function to create the lyrics and notes table-------------------//
def create_notes_table():
    try:
        database_cursor = my_connection.cursor()
        sql = "CREATE TABLE Notes(" \
              "id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY," \
              "note_name VARCHAR(40) NOT NULL," \
              "note_description VARCHAR(50) NOT NULL," \
              "note_uploaded_date VARCHAR(40) NOT NULL)"
        database_cursor.execute(sql)
    except Exception as ex:
        print(ex)


# -----------------------------------//function to create the samples table----------------//
def create_samples_table():
    try:
        database_cursor = my_connection.cursor()
        sql = "CREATE TABLE Samples(" \
              "id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY," \
              "sample_name VARCHAR(40) NOT NULL," \
              "sample_description VARCHAR(50) NOT NULL," \
              "sample_uploaded_date VARCHAR(40) NOT NULL)"
        database_cursor.execute(sql)
    except Exception as ex:
        print(ex)
