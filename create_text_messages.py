# This program sends personalized messages to all your clients about their amount owing.
# Created By: AJ Singh
# Date: Jan 11, 2021

import os
from twilio.rest import Client

# Twilio Information
# ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
# AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
# TWILIO_NUM = os.environ['TWILIO_NUM']
# client = Client(ACCOUNT_SID, AUTH_TOKEN)


# PATH = r"C:\Users\AJ\Desktop\accounts_receivable_automation\March.txt"
PATH = r"C:\Users\AJ\Desktop\test.txt"


def get_data() -> list:

    file = open(PATH)
    # print(file.read())
    data = []
    while True:
        line = file.readline().strip("\n")
        # print(line.split(","))
        if line:
            data.append(line.split(","))
        else:
            break

    return data


def create_messages(data: list):

    messages = {}
    for person in data:
        name, amount = person[0], person[1]
        phone = person[2]

        body = f"Hey {name}, your amount owing for the month of (MARCH) is {amount}."
        # print(body)
        messages[phone] = body

    print(messages)
    return messages


def send_messages(messages):

    for number in messages:
        body = messages[number]
        from_number = TWILIO_NUM  # Already has +1 on it.
        to_number = "+1" + number

        # Make API calls here...
        message = client.messages.create(
                             body=body,
                             from_=from_number,
                             to=to_number
                            )

        print(message.sid)


def main():
    data = get_data()
    messages = create_messages(data)
    # send_messages(messages)


if __name__ == '__main__':
    main()
