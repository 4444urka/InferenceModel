import numpy as np

class CustomLinearRegression:
    def __init__(self):
        self.coefficients = None
        self.intercept = None

    def fit(self, x, y):
        x = np.array(x)
        y = np.array(y)
        x_b = np.c_[np.ones((x.shape[0], 1)), x]
        theta_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)
        self.intercept = theta_best[0]
        self.coefficients = theta_best[1:]

    def predict(self, x):
        x = np.array(x)
        return x.dot(self.coefficients) + self.intercept