# parametry manipulacyjne
PPD_SV_range = [1900, 3500] # przepływ powietrza dystrybucyjnego (Nm3/h)
PPD_SV_MaxStepPerSec = 80.0
TwDP_SV_range = [65, 81] # tlen w dmuchu procesowym (%)
TwDP_SV_MaxStepPerSec = 0.013
PD_SV_range = [40, 70] # prędkość dmuchu [m/s]
PD_SV_MaxStepPerSec = 2.0
# parametry manipulacyjne nieuzywane
NPP_SV_range = [13,27] # nadawa pyłów procesowych
NPP_SV_MaxStepPerSec = 0

# Cele:
SCnS_optimal = 25 #strata cieplna na szybie reakcyjnym

### Internal config
DB_PATH = "database/lite_db.db"
app_port = 1234
MODEL_PATH = ""