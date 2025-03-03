import requests
from .config import Config

class WeatherAPI:
    def __init__(self):
        self.api_key = Config.WEATHER_API_KEY
        self.base_url = Config.WEATHER_API_URL
    
    def get_weather(self, location):
        """获取指定位置的天气信息"""
        try:
            url = f"{self.base_url}/current.json"
            params = {
                "key": self.api_key,
                "q": location
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Weather API error: {str(e)}")
    
    def parse_weather_data(self, data):
        """解析天气数据为结构化格式"""
        try:
            return {
                "location": data["location"]["name"],
                "country": data["location"]["country"],
                "temperature": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"],
                "humidity": data["current"]["humidity"],
                "wind_speed": data["current"]["wind_kph"]
            }
        except KeyError as e:
            raise Exception(f"Invalid weather data format: {str(e)}") 