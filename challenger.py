from matplotlib import pyplot as plt
from patsy import dmatrices
import matplotlib as mpl
import numpy as np
import pandas as pd
import statsmodels.discrete.discrete_model as sm

class Challenger:
    """Loaded data from csv file"""
    data = []

    def __init__(self):
        self.data = pd.read_csv("./challenger-data.csv")

    def plot(self):
        failures = self.data.loc[(self.data.Y == 1)]
        success = self.data.loc[(self.data.Y == 0)]
        failures_freq = failures.X.value_counts()
        success_freq = success.X.value_counts()
        plt.scatter(failures_freq.index, failures_freq, c='red', s=40)
        plt.scatter(success_freq.index, np.zeros(len(success_freq)), c='blue', s=40)
        plt.xlabel('X: Temperature')
        plt.ylabel('Number of failures')
        plt.show()

    def model(self):
        y, X = dmatrices('Y~X', self.data, return_type='dataframe')
        logit = sm.Logit(y, X)
        result = logit.fit()
        print result.summary()

    def __main__(self):
        self.model();

if __name__ == '__main__':
    challenger = Challenger()
    challenger.model()
