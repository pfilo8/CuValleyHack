import sqlite3
from sqlite3 import Error

class db_conn:
    def __init__(self):
        self.conn = None

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        try:
            self.conn = sqlite3.connect(db_file)
            self.create_table()
            print(sqlite3.version)
        except Error as e:
            print(e)

    def create_table(self):
        """ create a table from the create_history_table statement """
        create_history_table = """ CREATE TABLE IF NOT EXISTS history (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                zmienna1 real NOT NULL,
                                                zmienna2 real NOT NULL
                                            ); """

        try:
            c = self.conn.cursor()
            c.execute(create_history_table)
        except Error as e:
            print(e)

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def get_n_rows(self):
        n_rows_query = """ SELECT COUNT(zmienna1) FROM history; """
        n_rows = False
        try:
            c = self.conn.cursor()
            c.execute(n_rows_query)
            n_rows = c.fetchall()
        except Error as e:
            print(e)
        return n_rows[0][0]

    def insert(self, var_dict):
        zmienna1 = var_dict["zmienna1"]
        zmienna2 = var_dict["zmienna2"]
        insert_query = """ INSERT INTO history (zmienna1, zmienna2) VALUES (""" + \
                    str(zmienna1) + ',' + str(zmienna2)+ """); """
        try:
            c = self.conn.cursor()
            c.execute(insert_query)
            self.conn.commit()
        except Error as e:
            print(e)

    def read_rows(self, n):
        select_query = """ SELECT * FROM history LIMIT """ + str(n) + """; """
        selected_rows = False
        try:
            c = self.conn.cursor()
            c.execute(select_query)
            selected_rows = c.fetchall()
        except Error as e:
            print(e)

        return selected_rows