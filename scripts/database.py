import sqlite3
from sqlite3 import Error
import os


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None;
    try:
        conn = sqlite3.connect(os.path.join(os.curdir, 'sql.db'))
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


create_connection()