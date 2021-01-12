# This program sends personalized messages to all your clients about their amount owing.
# Created By: AJ Singh
# Date: Jan 11, 2021

from os import environ
from twilio.rest import Client

# Twilio Information
ACCOUNT_SID = environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = environ['TWILIO_AUTH_TOKEN']
TWILIO_NUM = environ['TWILIO_NUM']

# Instantiate client object.
# client = Client(ACCOUNT_SID, AUTH_TOKEN)

# PATH = r"C:\Users\AJ\Desktop\accounts_receivable_automation\March.txt"
PATH = r"C:\Users\AJ\Desktop\test.txt"


# Get amount owing data from text file created by 'extract_client_data.py'
# @params: None.
# @return: List of lines in text file.
def load_data() -> list:
    """Extract each line of data from text file."""

    file = open(PATH)
    data = []

    line = file.readline().strip("\n")
    while line:
        data.append(line.split(","))
        line = file.readline().strip("\n")

    file.close()

    return data


# Create text messages to send to clients:
# @param data: List of amount owing data for each client.
# @return: Dictionary of phone:message key-value pairs.
def create_messages(data: list) -> dict:
    """Create messages for each client including their amount owing."""

    messages = {}
    for person in data:
        name, amount, phone = person[0], person[1], person[2]
        body = f"Hey {name}, your amount owing for the month of (MARCH) is {amount}."

        messages[phone] = body

    return messages


# Connect to Twilio account to send text messages to clients.
# @param messages: Dictionary of phone:message key-value pairs.
# @return: None.
def send_messages(messages):
    """Connect to Twilio and send text messages."""

    for number in messages:
        body = messages[number]
        from_number = TWILIO_NUM  # Already has +1 on it.
        to_number = "+1" + number

        message = client.messages.create(body=body, from_=from_number, to=to_number)
        print(message.sid)


def main():
    data = load_data()
    messages = create_messages(data)
    print(messages)
    # send_messages(messages)


if __name__ == '__main__':
    main()
