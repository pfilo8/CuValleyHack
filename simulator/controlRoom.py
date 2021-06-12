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

        PARAMS = {"zmienna1":1, "zmienna2":22}
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
