# script_clima.py
from dotenv import load_dotenv   # importa a função para carregar .env
import os
import requests

# Carrega as variáveis do arquivo .env para as variáveis de ambiente do processo
load_dotenv()

API_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city, country_code="BR"):
    # Lê a chave da variável de ambiente que foi carregada a partir do .env
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENWEATHER_API_KEY não encontrada. Veja instruções no README.")
    params = {
        "q": f"{city},{country_code}",
        "units": "metric",
        "appid": api_key
    }
    r = requests.get(API_URL, params=params)
    r.raise_for_status()
    d = r.json()
    return {
        "city": d["name"],
        "temp_c": d["main"]["temp"],
        "wind_m_s": d["wind"]["speed"]
    }

if __name__ == "__main__":
    # teste rápido pra confirmar que a chave foi lida corretamente
    print("OPENWEATHER_API_KEY (somente 6 primeiros chars):", (os.getenv("OPENWEATHER_API_KEY") or "")[:6])
    cities = ["Curitiba", "São Paulo"]
    for c in cities:
        w = get_weather(c)
        print(f"{w['city']}: {w['temp_c']} °C, vento {w['wind_m_s']} m/s")

        #oi