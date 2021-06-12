import joblib
import pandas as pd

from ..config import *


class model:
    def __init__(self):
        self.model = self.read_model(MODEL_PATH)

    def read_model(self, path):
        return joblib.load(path)

    def feed_storage(self, data: pd.DataFrame):
        self.data = data

    def process_data(self):
        df = self.data
        df[TIME_VARIABLE] = pd.to_datetime(df[TIME_VARIABLE])
        df = df.set_index(TIME_VARIABLE)
        df = df.resample(f'{RESAMPLE_TIME}S').mean()
        df = df.set_index([TIME_VARIABLE])
        self.processed_data = df

    def optimize_parameters(self):
        PPD_SV_range  # = [1900, 3500]  # przepływ powietrza dystrybucyjnego (Nm3/h)
        PPD_SV_MaxStepPerSec  # = 80.0
        TwDP_SV_range  # = [65, 81]  # tlen w dmuchu procesowym (%)
        TwDP_SV_MaxStepPerSec  # = 0.013
        PD_SV_range  # = [40, 70]  # prędkość dmuchu [m/s]
        PD_SV_MaxStepPerSec  # = 2.0
