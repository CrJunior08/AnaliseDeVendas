import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

def enviar_sms(message_body):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+5511999999499",
        from_="+12513136551",
        body=message_body
    )
    print(message.sid)
