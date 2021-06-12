import sqlite3
from sqlite3 import Error
import sys
import pandas as pd
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
                                                zmienna0 text NOT NULL,
                                                zmienna1 real NOT NULL,
                                                zmienna2 real NOT NULL,
                                                zmienna3 real NOT NULL,
                                                zmienna4 real NOT NULL,
                                                zmienna5 real NOT NULL,
                                                zmienna6 real NOT NULL,
                                                zmienna7 real NOT NULL,
                                                zmienna8 real NOT NULL,
                                                zmienna9 real NOT NULL,
                                                zmienna10 real NOT NULL,
                                                zmienna11 real NOT NULL,
                                                zmienna12 real NOT NULL,
                                                zmienna13 real NOT NULL,
                                                zmienna14 real NOT NULL,
                                                zmienna15 real NOT NULL,
                                                zmienna16 real NOT NULL,
                                                zmienna17 real NOT NULL,
                                                zmienna18 real NOT NULL,
                                                zmienna19 real NOT NULL,
                                                zmienna20 real NOT NULL,
                                                zmienna21 real NOT NULL,
                                                zmienna22 real NOT NULL,
                                                zmienna23 real NOT NULL,
                                                zmienna24 real NOT NULL,
                                                zmienna25 real NOT NULL,
                                                zmienna26 real NOT NULL
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
        zmienna0 = var_dict["zmienna0"]
        zmienna1 = var_dict["zmienna1"]
        zmienna2 = var_dict["zmienna2"]
        zmienna3 = var_dict["zmienna3"]
        zmienna4 = var_dict["zmienna4"]
        zmienna5 = var_dict["zmienna5"]
        zmienna6 = var_dict["zmienna6"]
        zmienna7 = var_dict["zmienna7"]
        zmienna8 = var_dict["zmienna8"]
        zmienna9 = var_dict["zmienna9"]
        zmienna10 = var_dict["zmienna10"]
        zmienna11 = var_dict["zmienna11"]
        zmienna12 = var_dict["zmienna12"]
        zmienna13 = var_dict["zmienna13"]
        zmienna14 = var_dict["zmienna14"]
        zmienna15 = var_dict["zmienna15"]
        zmienna16 = var_dict["zmienna16"]
        zmienna17 = var_dict["zmienna17"]
        zmienna18 = var_dict["zmienna18"]
        zmienna19 = var_dict["zmienna19"]
        zmienna20 = var_dict["zmienna20"]
        zmienna21 = var_dict["zmienna21"]
        zmienna22 = var_dict["zmienna22"]
        zmienna23 = var_dict["zmienna23"]
        zmienna24 = var_dict["zmienna24"]
        zmienna25 = var_dict["zmienna25"]
        zmienna26 = var_dict["zmienna26"]

        insert_query = """ INSERT INTO history ("zmienna0", "zmienna1", "zmienna2",
        "zmienna3", "zmienna4", "zmienna5",
        "zmienna6", "zmienna7", "zmienna8",
        "zmienna9","zmienna10", "zmienna11",
        "zmienna12", "zmienna13", "zmienna14",
        "zmienna15", "zmienna16", "zmienna17",
        "zmienna18", "zmienna19", "zmienna20",
        "zmienna21", "zmienna22", "zmienna23",
        "zmienna24", "zmienna25", "zmienna26") VALUES (" """ + \
                    str(zmienna0) + '",' + str(zmienna1) + ',' + str(zmienna2)+','+\
                       str(zmienna3) + ',' + str(zmienna4)+','+\
                       str(zmienna5) + ',' + str(zmienna6)+','+\
                       str(zmienna7) + ',' + str(zmienna8)+','+\
                       str(zmienna9) + ',' + str(zmienna10)+','+\
                       str(zmienna11) + ',' + str(zmienna12)+','+\
                       str(zmienna13) + ',' + str(zmienna14)+','+\
                       str(zmienna15) + ',' + str(zmienna16)+','+\
                       str(zmienna17) + ',' + str(zmienna18)+','+\
                       str(zmienna19) + ',' + str(zmienna20)+','+\
                       str(zmienna21) + ',' + str(zmienna22)+','+\
                       str(zmienna23) + ',' + str(zmienna24)+','+\
                       str(zmienna25) + ',' + str(zmienna26) + """); """
        print(insert_query, file=sys.stderr)
        try:
            c = self.conn.cursor()
            c.execute(insert_query)
            self.conn.commit()
        except Error as e:
            print(e)

    def read_rows(self, n):
        select_query = """ SELECT * FROM history ORDER BY zmienna0 DESC LIMIT """ + str(n) + """; """
        selected_rows = False
        try:
            # c = self.conn.cursor()
            # c.execute(select_query)
            selected_rows = pd.read_sql_query(select_query, self.conn)
            # selected_rows = c.fetchall()
        except Error as e:
            print(e)

        return selected_rows