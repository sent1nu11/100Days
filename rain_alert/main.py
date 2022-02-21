import requests
from twilio.rest import Client
import config


account_sid = config.TWILIO_ACCOUNT_SID
auth_token = config.TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="From Twilio.  It's a beautiful SMS Message.",
                     from_=config.TWILIO_PHONE_NUMBER,
                     to=config.SENT_TO_PHONE_NUMBER
                 )

print(message.sid)