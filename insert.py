import logging
from random import randint
from psycopg2 import DatabaseError
from connect import create_connection
from functools import wraps

from FakeData import DataGeneratorFactory

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 50
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20


class DatabaseInserter:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    @staticmethod
    def insert_data_error_handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except DatabaseError as e:
                logging.error(f"Database error: {e}")
                args[0].conn.rollback()

        return wrapper

    @insert_data_error_handler
    def groups_insert(self, count):
        sql_groups_insert = "INSERT INTO groups (name) VALUES (%s);"
        group_gen = DataGeneratorFactory.create_data_generator("group")
        for _ in range(count):
            self.cursor.execute(sql_groups_insert, group_gen.generate_fake_data())
        self.conn.commit()

    @insert_data_error_handler
    def teachers_insert(self, count):
        sql_teachers_insert = (
            "INSERT INTO teachers (first_name, last_name) VALUES (%s, %s);"
        )
        teacher_gen = DataGeneratorFactory.create_data_generator("teacher")
        for _ in range(count):
            self.cursor.execute(sql_teachers_insert, teacher_gen.generate_fake_data())
        self.conn.commit()

    @insert_data_error_handler
    def students_insert(self, count, max_group_id):
        sql_students_insert = "INSERT INTO students (first_name, last_name, date_of_birth, group_id) VALUES (%s, %s, %s, %s);"
        student_gen = DataGeneratorFactory.create_data_generator("student")
        for _ in range(count):
            self.cursor.execute(
                sql_students_insert,
                student_gen.generate_fake_data() + [randint(1, max_group_id)],
            )
        self.conn.commit()

    @insert_data_error_handler
    def subjects_insert(self, count, max_teacher_id):
        sql_subjects_insert = "INSERT INTO subjects (name, teacher_id) VALUES (%s, %s);"
        subject_gen = DataGeneratorFactory.create_data_generator("subject")
        for _ in range(count):
            self.cursor.execute(
                sql_subjects_insert,
                subject_gen.generate_fake_data() + [randint(1, max_teacher_id)],
            )
        self.conn.commit()

    @insert_data_error_handler
    def grades_insert(self, count, max_student_id, max_subjucts_id):
        sql_grades_insert = "INSERT INTO grades (date_of_grade, mark, student_id, subject_id) VALUES (%s, %s, %s, %s);"
        grade_gen = DataGeneratorFactory.create_data_generator("grade")
        count = count * max_student_id * max_subjucts_id
        for _ in range(count):
            self.cursor.execute(
                sql_grades_insert,
                grade_gen.generate_fake_data()
                + [
                    randint(1, 12),
                    randint(1, max_student_id),
                    randint(1, max_subjucts_id),
                ],
            )
        self.conn.commit()


def run_insertions(inserter: DatabaseInserter):
    inserter.groups_insert(NUMBER_GROUPS)
    inserter.teachers_insert(NUMBER_TEACHERS)
    inserter.students_insert(NUMBER_STUDENTS, NUMBER_GROUPS)
    inserter.subjects_insert(NUMBER_SUBJECTS, NUMBER_TEACHERS)
    inserter.grades_insert(NUMBER_GRADES, NUMBER_STUDENTS, NUMBER_SUBJECTS)


if __name__ == "__main__":
    try:
        with create_connection() as conn:
            if conn:
                db = DatabaseInserter(conn)
                run_insertions(db)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)
