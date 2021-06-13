import joblib
import pandas as pd
import os
import sys
import numpy as np

try:
    __file__
except NameError:
    __file__ = None

if __file__ is not None:
    dir = os.path.dirname(__file__)
else:
    dir = ""
sys.path.append(os.path.join(dir, "../"))
print(os.path.join(dir, "../"))

from config import *
from model.Opt import Opt


class Model:
    def __init__(self):
        self.model = self.read_model(MODEL_PATH)
        self.data = None
        self.processed_data = None
        self.best_parameters = None

    def read_model(self, path):
        return joblib.load(path)

    def feed_storage(self, data: pd.DataFrame):
        self.data = data
        return self.data

    def process_data(self):
        df = self.data

        df[TIME_VARIABLE] = pd.to_datetime(df[TIME_VARIABLE])
        df = df.set_index(TIME_VARIABLE)
        df = df.resample(f'{RESAMPLE_TIME}S').mean()
        df = df.dropna().reset_index()
        df[f'{RESPONSE_VARIABLE}_train'] = df[RESPONSE_VARIABLE]
        df = df.set_index([TIME_VARIABLE, RESPONSE_VARIABLE])
        for col in df.columns:
            df[f'{col}_diff'] = df[col].diff()
            df[f'{col}_diff_2'] = df[col] - 2 * df[col].shift(1) + df[col].shift(2)
        self.processed_data = df[-1:].reset_index().set_index(TIME_VARIABLE).drop(labels=RESPONSE_VARIABLE, axis=1)
        return self.processed_data

    def optimize_parameters(self):
        # przepływ powietrza dystrybucyjnego '001FCx00285_SPPV.PV'
        PPD_SV_currenct = data.iloc[MODEL_REQ_ROWS - 1, 1]
        PPD_SV_space = [PPD_SV_currenct - PPD_SV_MaxStepPerSec, PPD_SV_currenct + PPD_SV_MaxStepPerSec]
        PPD_SV_space[0] = max([PPD_SV_space[0], PPD_SV_range[0]])
        PPD_SV_space[1] = max([PPD_SV_space[1], PPD_SV_range[1]])

        PPD_SV_possible_parameters = np.linspace(PPD_SV_space[0], PPD_SV_space[1], 50)

        # tlen w dmuchu procesowym (%) '001XXXCALC01.NUM.PV[3]'
        TwDP_SV_currenct = data.iloc[MODEL_REQ_ROWS - 1, 2]
        TwDP_SV_space = [TwDP_SV_currenct - TwDP_SV_MaxStepPerSec, TwDP_SV_currenct + TwDP_SV_MaxStepPerSec]
        TwDP_SV_space[0] = max([TwDP_SV_space[0], TwDP_SV_range[0]])
        TwDP_SV_space[1] = max([TwDP_SV_space[1], TwDP_SV_range[1]])

        TwDP_SV_possible_parameters = np.linspace(TwDP_SV_space[0], TwDP_SV_space[1], 50)

        # prędkość dmuchu [m/s] '001SCx00274_SPPV.PV'
        PD_SV_currenct = data.iloc[MODEL_REQ_ROWS - 1, 3]
        PD_SV_space = [PD_SV_currenct - PD_SV_MaxStepPerSec, PD_SV_currenct + PD_SV_MaxStepPerSec]
        PD_SV_space[0] = max([PD_SV_space[0], PD_SV_range[0]])
        PD_SV_space[1] = max([PD_SV_space[1], PD_SV_range[1]])

        PD_SV_possible_parameters = np.linspace(PD_SV_space[0], PD_SV_space[1], 50)

        return {"001FCx00285_SPPV.PV": PPD_SV_possible_parameters, "001FCx00241_sppv.pv":  TwDP_SV_possible_parameters,"001SCx00274_SPPV.PV": PD_SV_possible_parameters,}


if __name__ == '__main__':
    model = Model()
    data = pd.read_pickle("test_data_model.pkl")
    print(data)
    model.feed_storage(data)
    model.process_data()
    print(model.processed_data)
    output = model.optimize_parameters()
    print(output)