import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin

class ExactMatchModel(BaseEstimator, ClassifierMixin):
    def __init__(self, name_1, name_2):
        self.name_1 = name_1
        self.name_2 = name_2
    
    def fit(self, X, y=None):
        return self
    
    def predict(self, X):
        return (X[self.name_1] == X[self.name_2]).astype(int)
    
    def score(self, X, y):
        return np.mean(self.predict(X) == y)