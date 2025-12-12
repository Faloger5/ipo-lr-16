import pandas as pd  # библиотека для работы с таблицами

class DeliveryCalculator:  # класс для расчёта стоимости доставки
    def __init__(self, cost_per_km: float):  # конструктор принимает стоимость за километр
        self.cost_per_km = cost_per_km  # сохраняем параметр

    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:  # метод для расчёта
        df = df.rename(columns=lambda x: str(x).strip())  # убираем пробелы в названиях колонок

        if "Расстояние" in df.columns:  # если колонка называется "Расстояние"
            df = df.rename(columns={"Расстояние": "Расстояние (км)"})  # переименовываем
        if "Вес" in df.columns:  # если колонка называется "Вес"
            df = df.rename(columns={"Вес": "Вес груза (кг)"})  # переименовываем

        df["Базовая стоимость"] = df["Расстояние (км)"] * self.cost_per_km  # считаем базовую стоимость
        df["Наценка за вес"] = df["Вес груза (кг)"].apply(lambda w: 500 if w > 50 else 0)  # наценка
        df["Итого к оплате"] = df["Базовая стоимость"] + df["Наценка за вес"]  # итог
        return df  # возвращаем результат
