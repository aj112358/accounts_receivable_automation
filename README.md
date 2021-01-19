# Accounts Receivable Automation

This project automates the process of sending your small business clients their current amount owing for your services provided during a particular month.

## Problem Description

In my private small business, clients make their payments with varying frequency. Some pay after each session, others pay bi-weekly or monthly. For the latter, I have to manually compute the amount owing from each client and send my clients text messages to let them know. This takes up a considerable amount of time, and as such I wished to automate this process.

## Project Goals

There is one main goal for this project:
1. Create and send personalized text messages to all my clients that have a non-zero amount owing.

## Hardware and Software Used Used

* Python Version: 3.8
* Python Libraries: openpyxl, calendar, tabulate, os, twilio.rest, 

* Microsoft Excel
* Twilio API

## Overview of Twilio

Twilio (https://www.twilio.com) is an online cloud communications platform that offers various services including sending text messages, sending emails, and making/receiving phone calls. All of the services can be handled programmatically using the Twilio API (https://pypi.org/project/twilio/).

Signing up for a Twilio account is free, and your initial free-tier account comes with $15.50 for your use. You must then obtain a registered Twilio phone number - you can either use the one Twilio generates randomly, or you can search/specify the details of the phone number you want. 

In order to be able to send text messages, the receiving cell number must be verified with your Twilio account. This is easily done by adding the new number to your "Verified Caller ID's" list, where you will be asked to send the new number either a call or text with a verification code. Enter that verification code into Twilio and the new number is now registered.

Regarding the costs, holding a phone number costs $1.00 per month. In this project, we are only sending text messages. Each text message costs $0.0075 to send (thats 0.75 cents).

**NOTE: Twilio may reset your authentication token if you have not logged on to their website in a long time.**

## Explanation of Python Files

Here is a list of the Python modules:
* [extract_client_data](/extract_client_data.py)
* [create_text_messages](/create_text_messages.py)
* [accounts_receivable (MAIN)](/accounts_receivable.py)

### extract_client_data.py

This script takes the client data from an Excel worksheet and analyzes it to determine which clients have amounts owing. It extracts the following information and saves it into a text file:
* Name of client
* Amounts owing, along with the date
* Client phone number

**NOTE: The Excel file must have the exact structure (i.e. columns) as shown in the sample .xlsx file.**

### create_text_messages.py

This script takes the output text file from the previous script and aggregates the amounts owing for each client. It then creates custom text messages for each client, shows these to the user for last minute checks, and sends these using the Twilio API, upon approval from the user.

### accounts_receivable.py (MAIN)

This script is the main script and is a culmination of the prevoius two. It asks the user for the path to the Excel file and the month to compute the amounts owing within. It then uses the previous two scripts to extract data, and create and send the text messages to all clients.

## Conclusion

This project can be used by anyone to send their clients text messages regarding their amounts owing. It works successfully using the cloud communications service, Twilio.

## Future Steps

Here are some ideas that can be implemented in the future to improve this project:
* Ask user input for generic structure of the text messages (instead of using built-in message structure)
* Improve to work with Excel sheets with any column headers
* Create implementation of extracting data from other source

## Author

* **AJ Singh** (https://github.com/aj112358)

## License

This project is licensed under the MIT License - see the [LICENSE](/accounts_receivable_automation/blob/main/LICENSE) file for details.

## Acknowledgements

* Creators of the cloud communications platform service, Twilio
* Viewers of my GitHub page. Thanks for visiting!
