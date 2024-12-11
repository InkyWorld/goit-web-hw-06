import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    try:
        """ create a database connection to database """
        conn = psycopg2.connect(host="localhost", database="school", user="postgres", password="1234", options="-c client_encoding=utf8")
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")
