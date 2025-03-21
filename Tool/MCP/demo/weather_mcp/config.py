class Config:
    # API配置
    WEATHER_API_KEY = "your_api_key_here"
    WEATHER_API_URL = "https://api.weatherapi.com/v1"
    
    # MCP配置
    MODEL_NAME = "claude-3"
    MAX_RETRIES = 3
    TIMEOUT = 10
    
    # 提示词模板
    PROMPT_TEMPLATE = """
    You are a helpful weather assistant. Please provide weather information for {location}.
    Current weather data: {weather_data}
    Please format your response in a clear and concise way.
    """ 