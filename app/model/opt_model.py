from ..config import *

class model:
    def __init__(self):
        self.model = self.read_model(MODEL_PATH)

    def read_model(self, path):
        pass

    def feed_storage(self, data):
        self.data = data

    def process_data(self):
        self.data_processed = None

    def optimize_parameters(self):
        PPD_SV_range # = [1900, 3500]  # przepływ powietrza dystrybucyjnego (Nm3/h)
        PPD_SV_MaxStepPerSec #= 80.0
        TwDP_SV_range #= [65, 81]  # tlen w dmuchu procesowym (%)
        TwDP_SV_MaxStepPerSec #= 0.013
        PD_SV_range #= [40, 70]  # prędkość dmuchu [m/s]
        PD_SV_MaxStepPerSec #= 2.0


