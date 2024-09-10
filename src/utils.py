import os
from dotenv import load_dotenv
import logging

def setup_environment():
    """Carrega as variáveis de ambiente do arquivo .env"""
    load_dotenv()

def setup_logging():
    """Configura o logging do aplicativo"""
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
