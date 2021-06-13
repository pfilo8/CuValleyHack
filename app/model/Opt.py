from ..config import *


class Opt:
    def __init__(self, model, processing, X):
        self.X = X
        self.model = model
        self.processing = processing
        self.manipulacyjne_zmienne = ZMIENNE_MANIPULACYJNE
        self.deviations = DOPUSZCZALNE_ZMIANY
        self.maxminranges = ZAKRESY_ZMIENNYCH
        self.expected_value_of_loss = SCNS_OPTIMAL

    def get_ranges_tuple(self, values):
        ranges = []
        for i in range(len(values)):
            min_val, max_val = values[i] - self.deviations[i], values[i] + self.deviations[i]
            if min_val < self.maxminranges[i][0]:
                min_val = self.maxminranges[i][0]
                # Security, when max value is lower than min range
                if max_val < min_val:
                    max_val = min_val

            if max_val > self.maxminranges[i][1]:
                max_val = self.maxminranges[i][1]
                # Security, when min value is higher than max range
                if max_val < min_val:
                    min_val = max_val

            ranges.append((min_val, max_val))

        return ranges

    def get_ranges(self, X):
        values = []
        for variable in self.manipulacyjne_zmienne:
            values.append(X[variable].values[0])

        return self.get_ranges_tuple(values)

    def new_values_implementation(self, X, ranges, trial):
        for i, variable in enumerate(self.manipulacyjne_zmienne):
            X.loc[X.index[-1], variable] = trial.suggest_float(variable, ranges[i][0], ranges[i][1])

        return X

    def objective(self, trial):
        X = self.processing(self.X, 0, 30, RESAMPLE_TIME)
        ranges = self.get_ranges(X)
        X = self.new_values_implementation(X, ranges, trial)
        result = self.model.predict(X)

        return abs(self.expected_value_of_loss - result[0])
