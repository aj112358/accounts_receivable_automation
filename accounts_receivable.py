# This program sends messages to clients.
# Created By: AJ Singh
# Date: Jan 12, 2021

import extract_client_data
import create_text_messages
from calendar import month_name

MONTHS = list(month_name)


def main():

    path = input("\nWhat is the path to the Excel file: \n")  # .encode('unicode-escape').decode()

    month = input("\nEnter full name of month: ").capitalize()
    while month not in MONTHS:
        print("Invalid month!")
        month = input("\nEnter full name of month: ").capitalize()

    extract_client_data.main(path, month)
    create_text_messages.main()


if __name__ == "__main__":
    main()
