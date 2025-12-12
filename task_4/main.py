from flask import Flask, render_template, request, send_file
import pandas as pd
from delivery import DeliveryCalculator
from utils import style_excel

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    file = request.files["file"]
    cost_per_km = float(request.form["cost_per_km"])

    # Чтение Excel
    df = pd.read_excel(file)

    # Расчёт
    calculator = DeliveryCalculator(cost_per_km)
    df = calculator.calculate(df)

    # Стилизация и сохранение
    output_path = "report.xlsx"
    style_excel(df, output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

