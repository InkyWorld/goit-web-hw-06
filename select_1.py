import logging
from typing import List, Tuple, Any

from tabulate import tabulate
from psycopg2 import DatabaseError

from connect import create_connection

def query_reader(filename):
    with open(filename, 'r') as f:
        return f.read()

def execute_query(filename, params=None):
    try:
        sql = query_reader(filename)
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    if params:
                        c.execute(sql, params)
                    else:
                        c.execute(sql)
                    return c.fetchall()
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)

def print_table(data: List[Tuple[Any]]) -> None:
    print(tabulate(data, tablefmt="grid"))


if __name__ == '__main__':

    # result = execute_query("query_1.sql")
    # result = execute_query("query_2.sql", ("Що",))
    # result = execute_query("query_3.sql", ("Що",))
    # result = execute_query("query_4.sql")
    # result = execute_query("query_5.sql", ("Тетяна", "Бараник"))
    # result = execute_query("query_6.sql", ("Group-02-А",))
    # result = execute_query("query_7.sql", ("Group-01-Г", "Що"))
    # result = execute_query("query_8.sql", ("Тетяна", "Бараник"))
    # result = execute_query("query_9.sql", ("Ігор", "Удовиченко"))
    # result = execute_query("query_10.sql", ("Ігор", "Удовиченко", "Тетяна", "Бараник"))
    # result = execute_query("query_11.sql", ("Ігор", "Удовиченко", "Тетяна", "Бараник"))
    result = execute_query("query_4.sql", ("Group-04-Б", "Що"))
    print_table(result)