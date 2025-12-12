from flask import Flask, render_template, request, send_file  # импортируем Flask и нужные функции
import pandas as pd  # импортируем pandas для работы с Excel

app = Flask(__name__)  # создаём Flask-приложение

class DeliveryCalculator:  # класс для расчёта стоимости доставки
    def __init__(self, cost_per_km: float):  # конструктор принимает стоимость за километр
        self.cost_per_km = cost_per_km  # сохраняем параметр в объекте

    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:  # метод для расчёта по DataFrame
        df = df.rename(columns=lambda x: str(x).strip())  # убираем лишние пробелы в названиях колонок

        if "Расстояние" in df.columns:  # если колонка называется просто "Расстояние"
            df = df.rename(columns={"Расстояние": "Расстояние (км)"})  # переименовываем её в "Расстояние (км)"
        if "Вес" in df.columns:  # если колонка называется просто "Вес"
            df = df.rename(columns={"Вес": "Вес груза (кг)"})  # переименовываем её в "Вес груза (кг)"

        df["Базовая стоимость"] = df["Расстояние (км)"] * self.cost_per_km  # считаем базовую стоимость
        df["Наценка за вес"] = df["Вес груза (кг)"].apply(lambda w: 500 if w > 50 else 0)  # добавляем наценку за вес
        df["Итого к оплате"] = df["Базовая стоимость"] + df["Наценка за вес"]  # итоговая сумма
        return df  # возвращаем обновлённый DataFrame

@app.route("/", methods=["GET"])  # маршрут для главной страницы (форма)
def index():  # функция для отображения формы
    return render_template("index.html")  # рендерим HTML-шаблон index.html

@app.route("/process", methods=["POST"])  # маршрут для обработки формы
def process():  # функция для обработки загруженного файла
    file = request.files["file"]  # получаем загруженный файл
    cost_per_km = float(request.form["cost_per_km"])  # получаем введённую стоимость за км

    df = pd.read_excel(file)  # читаем Excel-файл в DataFrame

    calculator = DeliveryCalculator(cost_per_km)  # создаём объект калькулятора
    df = calculator.calculate(df)  # выполняем расчёт

    output_path = "report.xlsx"  # имя выходного файла
    df.to_excel(output_path, index=False)  # сохраняем результат в Excel

    return send_file(output_path, as_attachment=True)  # отправляем файл пользователю

if __name__ == "__main__":  # точка входа
    app.run(debug=True)  # запускаем Flask-приложение в режиме отладки
