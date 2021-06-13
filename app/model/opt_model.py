import optuna
import joblib
import pandas as pd

from ..config import *
from Opt import Opt


class model:
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
        df[ZMIENNA_CZASU] = pd.to_datetime(df[ZMIENNA_CZASU])
        df = df.set_index(ZMIENNA_CZASU)
        df = df.resample(f'{RESAMPLE_TIME}S').mean()
        df = df.dropna().reset_index()
        df[f'{ZMIENNA_CELU}_train'] = df[ZMIENNA_CELU]
        df = df.set_index([ZMIENNA_CZASU, ZMIENNA_CELU])
        for col in df.columns:
            df[f'{col}_diff'] = df[col].diff()
            df[f'{col}_diff_2'] = df[col] - 2 * df[col].shift(1) + df[col].shift(2)
        self.processed_data = df[-1:].reset_index().set_index(ZMIENNA_CZASU).drop(labels=ZMIENNA_CELU, axis=1)
        return self.processed_data

    def optimize_parameters(self):
        study = optuna.create_study()
        study.optimize(Opt(model=self.model, processing=self.processed_data, X=self.data).objective, timeout=1)
        self.best_parameters = study.best_params
        return self.best_parameters
