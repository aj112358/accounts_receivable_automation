# This program extracts data from the client data.
# Created By: AJ Singh
# Date: Jan 10, 2021

from openpyxl import load_workbook
from calendar import month_name

MONTHS = [month_name[i] for i in range(len(month_name))]


def open_file():

    PATH = r"C:\Users\AJ\Desktop\accounts_receivable_automation\client_data_sample.xlsx"
    file = load_workbook(PATH, data_only=True)
    ws = file.active

    return ws


def get_basic_data(worksheet):

    NUM_COLUMNS = worksheet.max_column
    NUM_ROWS = worksheet.max_row

    COLUMNS = []
    for i in range(1, NUM_COLUMNS+1):
        cell_obj = worksheet.cell(row=1, column=i)
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
        cell_obj = worksheet.cell(row=j, column=1)
        if cell_obj.value not in NAMES:
            NAMES.append(cell_obj.value)
    # print(NAMES)

    return COLUMNS, NAMES, NUM_COLUMNS, NUM_ROWS


def get_amounts_owing(month, NAMES, ws, NUM_ROWS) -> dict:

    # Will contain name: [ (date, amount) ]
    my_dict = {name: [] for name in NAMES}

    i = 2
    while i <= NUM_ROWS:

        paid = ws.cell(row=i, column=10).value
        y = ws.cell(row=i, column=4).value.month

        if not paid and y == MONTHS.index(month):
            date = ws.cell(row=i, column=4).value
            owing = ws.cell(row=i, column=9).value
            name = ws.cell(row=i, column=1).value

            my_dict[name].append((date, owing))
        i += 1

    return my_dict


# print("Your total amount owing for the month of {0} is: ${1:.2f}".format(month.capitalize(), total_amount))


def print_results(results: dict):

    for name in results:

        if results[name]:

            totals = list(zip(*results[name]))[1]
            total = sum(totals)
            print("{0}: ${1:.2f}".format(name, total))

        else:
            print(f"{name}: All good!")


def main():
    ws = open_file()
    month = input("What month (full name)? ").capitalize()
    COLUMNS, NAMES, NUM_COLUMNS, NUM_ROWS = get_basic_data(ws)
    results = get_amounts_owing(month, NAMES, ws, NUM_ROWS)
    print_results(results)


if __name__ == "__main__":
    main()
