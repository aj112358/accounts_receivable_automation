# This program extracts data from the client data.
# Created By: AJ Singh
# Date: Jan 10, 2021

import openpyxl

PATH = r"C:\Users\AJ\Desktop\accounts_receivable_automation\client_data_sample.xlsx"
file = openpyxl.load_workbook(PATH, data_only=True)
ws = file.active

NUM_COLUMNS = ws.max_column
NUM_ROWS = ws.max_row

COLUMNS = []
for i in range(1, NUM_COLUMNS+1):
    cell_obj = ws.cell(row=1, column=i)
    COLUMNS.append(cell_obj.value)
# print(COLUMNS)

NAMES = []
for j in range(2, NUM_ROWS+1):
    cell_obj = ws.cell(row=j, column=1)
    if cell_obj.value not in NAMES:
        NAMES.append(cell_obj.value)
# print(NAMES)

dates, amounts = [], []
dates_and_amounts = zip(dates, amounts)
# Check for Aerith's amount owing
i = 2
while i <= NUM_ROWS:

    x = ws.cell(row=i, column=10).value
    if not x and ws.cell(row=i, column=1).value == "Aerith":
        date = ws.cell(row=i, column=4).value
        owing = ws.cell(row=i, column=9).value

        dates.append(date)
        amounts.append(owing)

    i += 1

print(dates)
print(amounts)
