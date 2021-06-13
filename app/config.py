# parametry manipulacyjne
ZMIENNE_MANIPULACYJNE = ['001FCx00285_SPPV.PV',
                         '001XXXCALC01.NUM.PV[3]',
                         '001SCx00274_SPPV.PV',
                         '001FCx00241_sppv.pv']
ZMIENNA_CZASU = 'Czas'
ZMIENNA_CELU = "001NIR0SZR0.daca.pv"
DOPUSZCZALNE_ZMIANY = [80,
                       0.8 / 60,
                       2,
                       1]
ZAKRESY_ZMIENNYCH = [(1900, 3500),
                     (65, 81),
                     (40, 70),
                     (13, 27)]
RESAMPLE_TIME = 10
MODEL_REQ_ROWS = 30

# Cele:
SCNS_OPTIMAL = 25  # strata cieplna na szybie reakcyjnym
MODEL_PATH = "model/model.sav"
PPD_SV_range = [1900, 3500]  # przepływ powietrza dystrybucyjnego (Nm3/h)
PPD_SV_MaxStepPerSec = 80.0
TwDP_SV_range = [65, 81]  # tlen w dmuchu procesowym (%)
TwDP_SV_MaxStepPerSec = 0.013
PD_SV_range = [40, 70]  # prędkość dmuchu [m/s]
PD_SV_MaxStepPerSec = 2.0
# parametry manipulacyjne nieuzywane
NPP_SV_range = [13, 27]  # nadawa pyłów procesowych
NPP_SV_MaxStepPerSec = 0

# Cele:
SCnS_optimal = 25  # strata cieplna na szybie reakcyjnym

### Internal config
DB_PATH = "database/lite_db.db"
app_port = 1234

MODEL_REQ_ROWS = 20
MODEL_PATH = "model/model.sav"

# parametry preprocessing
TIME_VARIABLE = "Czas"
RESPONSE_VARIABLE = '001NIR0SZR0.daca.pv'
RESAMPLE_TIME = 10
RESPONSE_TIME = 300
