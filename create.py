import logging
from psycopg2 import DatabaseError

from connect import create_connection


def create_table(conn, sql_expression: str):
    """ create a table from the create_table_sql statement
    :param sql_expression:
    :param conn: Connection object
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    # Таблиця студентів
    sql_create_students_table = """CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        date_of_birth DATE NOT NULL,
        group_id INT REFERENCES groups(id) ON DELETE SET NULL
    );"""
    
    # Таблиця груп
    sql_create_groups_table = """CREATE TABLE IF NOT EXISTS groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE
    );"""

    # Таблиця викладачів
    sql_create_teachers_table = """CREATE TABLE IF NOT EXISTS teachers (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL
    );"""

    # Таблиця предметів
    sql_create_subjects_table = """CREATE TABLE IF NOT EXISTS subjects (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL UNIQUE,
        teacher_id INT REFERENCES teachers(id) ON DELETE SET NULL
    );"""

    # Таблиця оцінок студентів
    sql_create_students_marks_table = """CREATE TABLE IF NOT EXISTS grades (
        id SERIAL PRIMARY KEY,
        mark SMALLINT NOT NULL,
        student_id INT REFERENCES students(id) ON DELETE CASCADE,
        subject_id INT REFERENCES subjects(id) ON DELETE CASCADE,
        date_of_grade DATE NOT NULL
    );"""

    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, sql_create_groups_table)
                create_table(conn, sql_create_students_table)
                create_table(conn, sql_create_teachers_table)
                create_table(conn, sql_create_subjects_table)
                create_table(conn, sql_create_students_marks_table)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
