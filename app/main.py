from fastapi import FastAPI

from database.db import db_conn
from config import DB_PATH, MODEL_REQ_ROWS
from model.opt_model import Model

app = FastAPI()

@app.get("/getNewParams/")
def getNewParams(zmienna0: str, zmienna1: float, zmienna2: float,
        zmienna3: float, zmienna4 : float, zmienna5: float,
        zmienna6: float, zmienna7 : float, zmienna8 : float,
        zmienna9: float,zmienna10: float, zmienna11 : float,
        zmienna12: float, zmienna13: float, zmienna14: float,
        zmienna15: float, zmienna16: float, zmienna17: float,
        zmienna18: float, zmienna19: float, zmienna20: float,
        zmienna21: float, zmienna22: float, zmienna23 : float,
        zmienna24: float, zmienna25 : float, zmienna26 : float):
    

    # insert new data to database
    local_database = db_conn()
    local_database.create_connection(DB_PATH)
    local_database.insert({"zmienna0": zmienna0, "zmienna1": zmienna1, "zmienna2": zmienna2,
        "zmienna3": zmienna3, "zmienna4" : zmienna4, "zmienna5": zmienna5,
        "zmienna6": zmienna6, "zmienna7" : zmienna7, "zmienna8" : zmienna8,
        "zmienna9": zmienna9,"zmienna10": zmienna10, "zmienna11" : zmienna11,
        "zmienna12": zmienna12, "zmienna13": zmienna13, "zmienna14": zmienna14,
        "zmienna15": zmienna15, "zmienna16": zmienna16, "zmienna17": zmienna17,
        "zmienna18": zmienna18, "zmienna19": zmienna19, "zmienna20": zmienna20,
        "zmienna21": zmienna21, "zmienna22": zmienna22, "zmienna23" : zmienna23,
        "zmienna24": zmienna24, "zmienna25" : zmienna25,"zmienna26" : zmienna26})

    print("Collecting data" + str([zmienna1, zmienna2])) 
    # find optimal parameters
    # if there is enough data in database
    n_rows_db = local_database.get_n_rows()
    print(n_rows_db)
    if  n_rows_db > MODEL_REQ_ROWS:
        # ask model for new outcome
        data = local_database.read_rows(MODEL_REQ_ROWS)
        data = data.rename({"zmienna0": "Czas", "zmienna1": "001FCx00285_SPPV.PV", "zmienna2": "001XXXCALC01.NUM.PV[3]",
        "zmienna3": "001SCx00274_SPPV.PV", "zmienna4" : "001FCx00241_sppv.pv", "zmienna5": "001NIR0SZR0.daca.pv",
        "zmienna6": "001NIR0SZRG.daca.pv", "zmienna7" : "001NIR0S600.daca.pv", "zmienna8" : "001NIR0S500.daca.pv",
        "zmienna9": "001NIR0S300.daca.pv","zmienna10": "001NIR0S100.daca.pv", "zmienna11" : "001FYx00206_SPSUM.pv",
        "zmienna12": "001FCx00231_SPPV.PV", "zmienna13": "001FCx00251_SPPV.PV", "zmienna14": "001FCx00281.PV",
        "zmienna15": "001FCx00262.PV", "zmienna16": "001FCx00261.PV", "zmienna17": "001XXXCALC01.NUM.PV[2]",
        "zmienna18": "prob_corg", "zmienna19": "prob_s", "zmienna20": "sita_nadziarno",
        "zmienna21": "sita_podziarno", "zmienna22": "poziom_zuzel", "zmienna23" : "001UCx00274.pv",
        "zmienna24": "001NIR0ODS0.daca.pv", "zmienna25" : "temp_zuz", "zmienna26" : "007SxR00555.daca1.pv"}, axis=1)
        data = data.sort_values("Czas").drop("id", axis = 1)
        print(data)
        model = Model()
        model.feed_storage(data)
        model.process_data()
        output = model.optimize_parameters()
        print(output)
        local_database.close_connection()
        return output
    # else: model cannot be used yet
    else:
        print(local_database.read_rows(5))
        local_database.close_connection()
        return "Waiting for more data"




