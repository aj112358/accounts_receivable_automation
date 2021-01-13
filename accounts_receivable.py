# The main program to create and send text messages to clients.
# Created By: AJ Singh
# Date: Jan 12, 2021

from extract_client_data import extract_client_data
from create_text_messages import create_text_messages
from calendar import month_name
from os.path import dirname


def main():

    excel_path = input("\nWhat is the path to the Excel file: \n")
    month = input("\nEnter full name of month: ").capitalize()
    while month not in list(month_name):
        month = input("\nInvalid input. Enter full name of month: ").capitalize()

    directory = dirname(excel_path)
    month_file = directory + f"\\{month}.txt"

    extract_client_data(excel_path, month)
    create_text_messages(month_file)


if __name__ == "__main__":
    main()
