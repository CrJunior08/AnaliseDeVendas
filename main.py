import pandas as pd
from src.sms import enviar_sms
from src.vendas import processar_vendas

def main():
    lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
    
    for mes in lista_meses:
        tabela_vendas = pd.read_excel(f'data/{mes}.xlsx')
        vendedor, vendas = processar_vendas(tabela_vendas)
        
        if vendedor and vendas:
            mensagem = f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'
            enviar_sms(mensagem)

if __name__ == "__main__":
    main()
