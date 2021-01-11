# This program extracts data from the client data.
# Created By: AJ Singh
# Date: Jan 10, 2021

import openpyxl
# from datetime import date
from calendar import month_name


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

# # Just a test!!
# COLUMNS2 = []
# for row in ws.values:
#     for value in row:
#         # cell_obj = ws.cell(row=1, column=col)
#         # COLUMNS2.append(cell_obj.value)
#         print(value)
# # print(COLUMNS2)


NAMES = []
for j in range(2, NUM_ROWS+1):
    cell_obj = ws.cell(row=j, column=1)
    if cell_obj.value not in NAMES:
        NAMES.append(cell_obj.value)
# print(NAMES)

# Will contain name: [ (date, amount) ]
my_dict = {name:[] for name in NAMES}


month = input("What month (full name)? ").capitalize()
MONTHS = [month_name[i] for i in range(len(month_name))]
dates, amounts = [], []
dates_and_amounts = zip(dates, amounts)
i = 2
while i <= NUM_ROWS:

    paid = ws.cell(row=i, column=10).value
    y = ws.cell(row=i, column=4).value.month

    if not paid and y == MONTHS.index(month):
        date = ws.cell(row=i, column=4).value
        owing = ws.cell(row=i, column=9).value
        name = ws.cell(row=i, column=1).value

        dates.append(date)
        amounts.append(owing)
        my_dict[name].append((date, owing))
    i += 1

# print(my_dict)


# print(dates)
# print(amounts)

# total_amount = sum(amounts)

# print("Your total amount owing for the month of {0} is: ${1:.2f}".format(month.capitalize(), total_amount))

for name in my_dict:

    if my_dict[name]:


        totals = list(zip(*my_dict[name]))[1]

        total = sum(totals)
        print(f"{name}: {total}")

    # total = list(map(lambda x: sum(x[1]), zip(*my_dict["Barret"])))
    # map(lambda x: total + x[1], my_dict[name])
