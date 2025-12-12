import pandas as pd

class DeliveryCalculator:
    def __init__(self, cost_per_km: float):
        self.cost_per_km = cost_per_km

    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        df["Базовая стоимость"] = df["Расстояние (км)"] * self.cost_per_km
        df["Наценка за вес"] = df["Вес груза (кг)"].apply(lambda w: 500 if w > 50 else 0)
        df["Итого к оплате"] = df["Базовая стоимость"] + df["Наценка за вес"]
        return df

