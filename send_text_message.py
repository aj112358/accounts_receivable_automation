# This program sends personalized messages to all your clients about their amount owing.
# Created By: AJ Singh
# Date: Jan 11, 2021

import os
from twilio.rest import Client

# Twilio Information
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_num = os.environ['TWILIO_NUM']
# client = Client(account_sid, auth_token)

# Make API calls here...

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+',
                     to='+'
                 )

print(message.sid)



