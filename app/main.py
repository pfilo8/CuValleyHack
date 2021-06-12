from fastapi import FastAPI
from database.db import db_conn
from config import DB_PATH
app = FastAPI()

model = {"req_rows": 2}

@app.get("/getNewParams/")
def read_item(zmienna1: float, zmienna2: float):
    local_database = db_conn()
    local_database.create_connection(DB_PATH)
    n_rows_db = local_database.get_n_rows()
    print(n_rows_db)

    if  n_rows_db > model["req_rows"]:

        local_database.close_connection()
        return "Model output " + str([zmienna1, zmienna2])
    else:
        local_database.insert({"zmienna1": zmienna1, "zmienna2": zmienna2})
        print(local_database.get_n_rows())
        print(local_database.read_rows(5))
        local_database.close_connection()
        return "Collecting data" + str([zmienna1, zmienna2])



