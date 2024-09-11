# Projeto de Análise de Vendas e Envio de SMS

Este projeto analisa dados de vendas de arquivos Excel e envia SMS via Twilio quando a meta de vendas é atingida. Ele utiliza Python e bibliotecas para o processamento de dados e comunicação via SMS.

## Tecnologias Utilizadas

- **[Python](https://www.python.org/)**: Linguagem de programação principal
- **[Pandas](https://pandas.pydata.org/)**: Biblioteca para processamento de dados
- **[Twilio](https://www.twilio.com/pt-br)**: Serviço para envio de notificações/SMS
- **[Logs](https://docs.python.org/pt-br/3/howto/logging.html)**: Rastreabilidade e manutenção do sistema
- **Código Limpo**: Boas práticas de programação e documentação clara

## Índice
1. Pré-requisitos
2. Instalação
3. Configuração do Twilio
4. Modificando Variáveis e Números de Telefone
5. Rodando o Projeto
6. Estrutura do Projeto

---

## Pré-requisitos

### 1. Instale o **[Python](https://www.python.org/)** na sua máquina.

### 2. Crie uma conta no **[Twilio](https://www.twilio.com/)**, se ainda não tiver.

---

## Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/CrJunior08/AnaliseDeVendas.git
cd AnaliseDeVendas
```

### 2. Crie e ative um ambiente virtual:

No Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
```

No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

## Configuração do Twilio

1. Crie uma conta no [Twilio](https://www.twilio.com/).
2. No console do Twilio, obtenha o **Account SID** e o **Auth Token**.
3. Voce tera um número de telefone no Twilio:
   - Acesse informações da conta "Meu numero de telefone Twilio".

---

## Modificando Variáveis e Números de Telefone

### 1. Crie um arquivo `.env` na raiz do projeto e adicione as variáveis de ambiente:

```bash
TWILIO_ACCOUNT_SID=SeuAccountSID
TWILIO_AUTH_TOKEN=SeuAuthToken
```

Substitua `SeuAccountSID` e `SeuAuthToken` pelos valores obtidos no painel do Twilio.

### 2. Atualize o número de telefone no código:

No arquivo `src/sms.py`, modifique os parâmetros `to` e `from_` no método `send_sms` para os seus números:

```python
def send_sms(to, from_, body):
    """Envia um SMS e registra o resultado"""
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
```

Certifique-se de que o número `from_` é o número de telefone adquirido no Twilio, e `to` é o número de telefone para onde o SMS será enviado.

---

## Rodando o Projeto

### Execute o script principal para processar os dados e enviar os SMS:

```bash
python main.py
```

Este comando processará os arquivos Excel na pasta `data/` e enviará SMS quando a meta de vendas for atingida.

---

## Logs
Quando você executar o projeto pela primeira vez, uma pasta chamada logs/ será criada automaticamente na raiz do projeto. Todos os logs de execução, incluindo sucessos e erros, serão registrados no arquivo app.log dentro dessa pasta.

Você poderá consultar os logs acessando o arquivo logs/app.log, que conterá informações detalhadas sobre o processamento dos dados e o envio dos SMS.
