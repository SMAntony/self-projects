import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         messaging_service_sid='MG33c32942091b969b1aabecb0e215597b',
         body='Yo tengo un gato',
         to='+919489165233'
     )

print(message.sid)

"""
# twilio phone-numbers:list -> To get the list of purchased phone numbers
# twilio api:messaging:v1:services:phone-numbers:create --service-sid MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX --phone-number-sid PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 -> Add phone number to the msging service
"""

