import pandas as pd  # импортируем библиотеку pandas для работы с таблицами и Excel

def style_excel(df: pd.DataFrame, output_path: str):  # функция принимает DataFrame и путь для сохранения
    df.to_excel(output_path, index=False)  # сохраняем DataFrame в Excel-файл без индекса
