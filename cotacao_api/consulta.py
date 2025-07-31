import os
import requests
from dotenv import load_dotenv

load_dotenv()

moedas = ['BRL', 'EUR', 'GBP', 'JPY', 'ARS']

KEY_API = os.getenv("API_KEY")

res = requests.get(f"https://v6.exchangerate-api.com/v6/{KEY_API}/latest/USD")
cotacao = res.json()

cotacoes = cotacao['conversion_rates']

for moeda, valor in cotacoes.items():
    if moeda in moedas:
        print(f"{moeda}: {valor}")
    
