import requests
from app.config import OPENWEATHER_API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    """Получает данные о текущей погоде для указанного города."""
    params = {
        'q': city,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric',  # Получаем температуру в градусах Цельсия
        'lang': 'ru'  # Язык вывода — русский
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        return None
    
    return response.json()
