import pandas as pd
import requests
from time import sleep
# from app.config import SCnS_optimal
import pandas as pd

SCnS_optimal = 25

if __name__ == '__main__':
    data_sensors = pd.read_pickle("data_sensors.pkl")
    URL = "http://172.26.0.2:8000/getNewParams/"
    for index, sensors_output in data_sensors.iterrows():

        PARAMS = {"zmienna0": sensors_output[0], "zmienna1": sensors_output[1], "zmienna2": sensors_output[2],
        "zmienna3": sensors_output[3], "zmienna4" : sensors_output[4], "zmienna5": sensors_output[5],
        "zmienna6": sensors_output[6], "zmienna7" : sensors_output[7], "zmienna8" : sensors_output[8],
        "zmienna9": sensors_output[9],"zmienna10": sensors_output[10], "zmienna11" : sensors_output[11],
        "zmienna12": sensors_output[12], "zmienna13": sensors_output[13], "zmienna14": sensors_output[14],
        "zmienna15": sensors_output[15], "zmienna16": sensors_output[16], "zmienna17": sensors_output[17],
        "zmienna18": sensors_output[18], "zmienna19": sensors_output[19], "zmienna20": sensors_output[20],
        "zmienna21": sensors_output[21], "zmienna22": sensors_output[22], "zmienna23" : sensors_output[22],
        "zmienna24": sensors_output[24], "zmienna25" : sensors_output[25],"zmienna26" : sensors_output[26]}
        r = requests.get(url=URL, params=PARAMS)

        # extracting data in json format and printing results
        data = r.json()
        print("Strata ciepłna w szybkie: " + str(sensors_output["001NIR0SZR0.daca.pv"])+ ", docelowa: " + str(SCnS_optimal) + "; Potrzebna zmiana: " + str(SCnS_optimal - sensors_output["001NIR0SZR0.daca.pv"]))
        print("Zmiana parametrów: ")
        print("001FCx00285_SPPV.PV - przep. pow. dys.: " + str(data))
        print("001XXXCALC01.NUM.PV[3] - stęż. O2 w wdmuchu: " + str(data))
        print("001SCx00274_SPPV.PV - prędk. dmuchu: " + str(data))
        print("001FCx00241_sppv.pv - nadawa pyłów proc.: " + str(data) + "\n")
        sleep(1)
