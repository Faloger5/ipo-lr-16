#Доброва Анна
from flask import Flask, render_template, request, send_file  # Flask и функции
import pandas as pd  # pandas для чтения Excel
import os  # os для работы с путями
from delivery import DeliveryCalculator  # импортируем класс из delivery.py
from utils import style_excel  # импортируем функцию из utils.py

app = Flask(__name__)  # создаём Flask-приложение

@app.route("/", methods=["GET"])  # маршрут для главной страницы
def index():
    return render_template("index.html")  # рендерим HTML-форму

@app.route("/process", methods=["POST"])  # маршрут для обработки формы
def process():
    file = request.files["file"]  # получаем загруженный файл
    cost_per_km = float(request.form["cost_per_km"])  # получаем стоимость за км

    df = pd.read_excel(file)  # читаем Excel в DataFrame
    calculator = DeliveryCalculator(cost_per_km)  # создаём калькулятор
    df = calculator.calculate(df)  # выполняем расчёт

    output_path = os.path.join(os.path.dirname(__file__), "report.xlsx")  # путь для сохранения
    style_excel(df, output_path)  # сохраняем отчёт через функцию

    return send_file(output_path, as_attachment=True)  # отправляем файл пользователю

if __name__ == "__main__":  # точка входа
    app.run(debug=True)  # запускаем Flask

