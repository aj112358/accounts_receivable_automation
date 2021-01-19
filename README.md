# Accounts Receivable Automation
This project automates the process of sending your small business clients their current amount owing for your services provided.

## Problem Description
In my private small business, clients make their payments with varying frequency. Some pay after each session, others pay bi-weekly or monthly. For the latter, I have to manually compute the amount owing from each client and send my clients text messages to let them know. This takes up a considerable amount of time, and as such I wished to automate this process.


## Project Goals
There is one main goal for this project:
1. Create and send personalized text messages to all my clients that have a non-zero amount owing.


## Python Libraries Used
* Python Version: 3.8
* Python Libraries: openpyxl, calendar, tabulate, os, twilio.rest, 


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


### create_text_messages.py
This script takes the output text file from the previous script and aggregates the amounts owing for each client. It then creates custom text messages for each client, shows these to the user for last minute checks, and sends these using the Twilio API, upon approval from the user.


### accounts_receivable.py (MAIN)
This script is the main script and is a culmination of the prevoius two. It asks the user for the path to the Excel file and the month to compute the amounts owing within. It then uses the previous two scripts to extract data, and create and send the text messages to all clients.


## Conclusion
This project can be used by anyone to send their clients messages regarding their amounts owing.


## Future Steps
Here are some ideas that can be implemented in the future to improve this project:
* Ask user input for generic structure of the text messages (instead of using built-in message structure)
* Improve to work with Excel sheets with any column headers


## Author
* **AJ Singh** (https://github.com/aj112358)


## License


## Acknowledgements
* Creators of the cloud communications platform service, Twilio
* Viewers of my GitHub page. Thanks for visiting!



