from fastapi import FastAPI

from database.db import db_conn
from config import DB_PATH

app = FastAPI()

@app.get("/getNewParams/")
def read_item(zmienna1: float, zmienna2: float):
    model = {"req_rows": 10}

    # insert new data to database
    local_database = db_conn()
    local_database.create_connection(DB_PATH)
    local_database.insert({"zmienna1": zmienna1, "zmienna2": zmienna2})
    print("Collecting data" + str([zmienna1, zmienna2]))
    # find optimal parameters
    # if there is enough data in database
    n_rows_db = local_database.get_n_rows()
    print(n_rows_db)
    if  n_rows_db > model["req_rows"]:
        # ask model for new outcome

        local_database.close_connection()
        return "Model output " + str([zmienna1, zmienna2])
    # else: model cannot be used yet
    else:
        print(local_database.read_rows(5))
        local_database.close_connection()
        return "Waiting for more data"




