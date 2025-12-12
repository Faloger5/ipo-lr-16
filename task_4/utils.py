import pandas as pd

def style_excel(df: pd.DataFrame, output_path: str):
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Report")
        sheet = writer.sheets["Report"]

        # Применяем стили: выделяем строки, где сумма > 5000
        for row in range(2, len(df) + 2):  # начиная со 2-й строки (после заголовков)
            total_value = df.loc[row - 2, "Итого к оплате"]
            if total_value > 5000:
                for col in range(1, len(df.columns) + 1):
                    cell = sheet.cell(row=row, column=col)
                    cell.fill = openpyxl.styles.PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")

