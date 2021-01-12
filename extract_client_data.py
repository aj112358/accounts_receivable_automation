# This program extracts data from the client data.
# Created By: AJ Singh
# Date: Jan 10, 2021

from openpyxl import load_workbook
from calendar import month_name

MONTHS = list(month_name)


# Opens Excel file containing client data.
# @params: None
# @return: Excel worksheet.
def open_file():
    """Open Excel worksheet containing client data."""

    PATH = r"C:\Users\AJ\Desktop\accounts_receivable_automation\client_data_sample.xlsx"
    file = load_workbook(PATH, data_only=True)
    ws = file.active

    return ws


# Extract columns headers from Excel sheet.
# @param worksheet: Excel worksheet.
# @return: List of active column headers.
def get_column_headers(worksheet) -> list:

    num_columns = worksheet.max_column
    headers = []
    for i in range(1, num_columns+1):
        cell_obj = worksheet.cell(row=1, column=i)
        headers.append(cell_obj.value)

    return headers


# Extract client names from Excel sheet.
# @param worksheet: Excel worksheet.
# @return: List of client names.
def get_client_names(worksheet) -> list:

    num_rows = worksheet.max_row
    names = []
    for j in range(2, num_rows+1):
        cell_obj = worksheet.cell(row=j, column=1)
        if cell_obj.value not in names:
            names.append(cell_obj.value)

    return names


def get_amounts_owing(month, names, ws) -> dict:

    # Values will have structure: [ (date, amount) ]
    my_dict = {name: [] for name in names}
    num_rows = ws.max_row

    i = 2
    while i <= num_rows:

        paid = ws.cell(row=i, column=10).value
        y = ws.cell(row=i, column=4).value.month

        if not paid and y == MONTHS.index(month):
            date = ws.cell(row=i, column=4).value
            owing = ws.cell(row=i, column=9).value
            name = ws.cell(row=i, column=1).value

            my_dict[name].append((date, owing))
        i += 1

    return my_dict


def get_phone_nums(ws, names) -> dict:
    num_rows = ws.max_row
    my_dict = {name: "" for name in names}

    for i in range(2, num_rows+1):
        name = ws.cell(row=i, column=1).value
        phone = ws.cell(row=i, column=12).value

        my_dict[name] = phone

    return my_dict


def print_results(results: dict, month: str):

    for name in results:

        if results[name]:  # There is an amount owing.

            totals = list(zip(*results[name]))[1]
            total = sum(totals)
            print("{0}: ${1:.2f}".format(name, total))

        else:
            print(f"{name}: All good!")


# Creates text file containing name/amount owing/phone number of client.
# @param results:
def save_results(results: dict, month: str, phone_nums: dict) -> None:

    with open(f"{month}.txt", mode='w') as file:
        for name in results:
            if results[name]:
                totals = list(zip(*results[name]))[1]
                total = sum(totals)
                phone = phone_nums[name]
                file.write("{0},${1:.2f},{2}\n".format(name, total, phone))


def main():
    ws = open_file()
    month = input("What month (full name)? ").capitalize()
    COLUMNS = get_column_headers(ws)
    names = get_client_names(ws)

    NUM_COLUMNS = ws.max_column
    NUM_ROWS = ws.max_row

    results = get_amounts_owing(month, names, ws)
    phone_nums = get_phone_nums(ws, names)
    print_results(results, month)

    save_results(results, month, phone_nums)


if __name__ == "__main__":
    main()



##### OLD CODES #####


# print("Your total amount owing for the month of {0} is: ${1:.2f}".format(month.capitalize(), total_amount))

