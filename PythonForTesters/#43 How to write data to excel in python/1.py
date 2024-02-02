from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws['A1'] = "Data, written from python"
# Остановился на 8:02, пошел отдыхать