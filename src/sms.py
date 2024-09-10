import logging
import os
from twilio.rest import Client
from src.utils import setup_environment

setup_environment()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

def enviar_sms(to, from_, body):
    """Envia um SMS e salva o resultado"""
    try:
        message = client.messages.create(
            to=to,
            from_=from_,
            body=body
        )
        logging.info(f'SMS enviado para {to}. SID: {message.sid}')
        return message.sid
    except Exception as e:
        logging.error(f'Erro ao enviar SMS: {e}')
        raise
