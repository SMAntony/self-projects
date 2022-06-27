# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
print(account_sid, auth_token)
message = client.messages \
                .create(
                     body="TwilioQuest rules",
                     from_='+18646519103',
                     to='+919489165233'
                 )

print(message.sid)
# 9489165233
# twilio api:core:messages:create --body "Join Earth's mightiest heroes. Like Kevin Bacon." --from +18646519103 --to +919489165233
