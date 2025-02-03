import pandas as pd

from src.lib.CustomLinearRegression.CustomLinearRegression import CustomLinearRegression

class PredictionModel:
    def __init__(self):
        self.model = CustomLinearRegression()

    def train(self, data: pd.DataFrame):
        x = data.drop(columns=[data.columns[0], "price", "code"])
        y = data["price"]
        self.model.fit(x, y)

    def predict(self, features: list):
        return self.model.predict([features])[0]