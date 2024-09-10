import pandas as pd
import logging
from src.sms import enviar_sms
from src.utils import setup_logging

setup_logging()

def processar_vendas(caminho_arquivo):
    """Processa os dados de vendas e envia SMS se a meta for atingida"""
    try:
        tabela_vendas = pd.read_excel(caminho_arquivo)
        if (tabela_vendas['Vendas'] > 55000).any():
            vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
            vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
            
            logging.info(f'No arquivo {caminho_arquivo}: Vendedor {vendedor} bateu a meta com {vendas} vendas.')
            
            enviar_sms(
                to="+5511989845789",
                from_="+12513136551",
                body=f'No mes {caminho_arquivo.split("/")[1].replace(".xlsx", "")} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'
            )
        else:
            logging.info(f'No arquivo {caminho_arquivo}, ninguem bateu a meta.')
    except Exception as e:
        logging.error(f'Erro ao processar o arquivo {caminho_arquivo}: {e}')
        raise
