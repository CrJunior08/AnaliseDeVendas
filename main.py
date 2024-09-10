import logging
import os
from src.utils import setup_environment, setup_logging
from src.vendas import processar_vendas

setup_environment()
setup_logging()

def main():
    lista_meses = ['data/janeiro.xlsx', 'data/fevereiro.xlsx', 'data/março.xlsx', 'data/abril.xlsx', 'data/maio.xlsx', 'data/junho.xlsx']
    
    for mes in lista_meses:
        try:
            processar_vendas(mes)
        except Exception as e:
            logging.error(f'Erro ao processar vendas do mes {mes}: {e}')

if __name__ == "__main__":
    main()
