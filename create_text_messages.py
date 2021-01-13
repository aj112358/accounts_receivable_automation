# This program creates personalized messages to all your clients about their amount owing.
# Created By: AJ Singh
# Date: Jan 11, 2021

from os import environ
from twilio.rest import Client

# Twilio Information
ACCOUNT_SID = environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = environ['TWILIO_AUTH_TOKEN']
TWILIO_NUM = environ['TWILIO_NUM']

# Instantiate client object.
client = Client(ACCOUNT_SID, AUTH_TOKEN)


# Get amount owing data from text file created by 'extract_client_data.py'
# @params text_file: Path for text file containing summary of amounts owing.
# @return: List of lines in text file.
def load_data(text_file) -> list:
    """Extract each line of data from text file."""

    file = open(text_file)
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
def create_messages(data: list, month_name: str) -> dict:
    """Create messages for each client including their amount owing."""

    messages = {}
    for person in data:
        name, amount, phone = person[0], person[1], person[2]
        body = f"Hey {name}, your amount owing for the month of {month_name} is {amount}."

        messages[phone] = body

    print("\nHere are the messages to be sent:\n")
    for key in messages:
        print(messages[key])

    return messages


# Connect to Twilio account to send text messages to clients.
# @param messages: Dictionary of phone:message key-value pairs.
# @return: String output for (un)successful delivery of messages
def send_messages(messages: dict) -> str:
    """Connect to Twilio and send text messages."""

    approval = input("\nDo you wish to send these messages? Type 'yes' or 'no': ")
    if approval.lower() != 'yes':
        return "Messages not approved. Please run the program again."

    for number in messages:
        body = messages[number]
        from_number = TWILIO_NUM  # Already has +1 on it.
        to_number = "+1" + number

        message = client.messages.create(body=body, from_=from_number, to=to_number)
        print(message.sid)

    return "All messages sent!"


# Main function to create text messages to send to clients.
# @param file_path: Path to text file containing summary of amount owing data.
# @return: None.
def create_text_messages(file_path: str) -> None:
    """Loads file, creates text messages, and sends them upon approval."""

    data = load_data(file_path)
    month_name = file_path[file_path.rindex("\\", -14) + 1:-4]

    messages = create_messages(data, month_name)
    success = send_messages(messages)
    print(success)


if __name__ == '__main__':
    path = r"C:\Users\AJ\Desktop\test.txt"
    create_text_messages(path)
