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

### Internal config
DB_PATH = "database/lite_db.db"
app_port = 1234
