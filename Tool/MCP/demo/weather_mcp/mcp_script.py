from typing import Dict, Any
from .weather_api import WeatherAPI
from .config import Config

class WeatherMCP:
    def __init__(self):
        self.weather_api = WeatherAPI()
        self.context = []
        self.rules = self._load_rules()
    
    def _load_rules(self) -> Dict[str, Any]:
        """加载MCP规则"""
        return {
            "name": "weather_mcp",
            "model": Config.MODEL_NAME,
            "rules": {
                "context": {
                    "max_length": 2000,
                    "priority_rules": [
                        {"weather_data": "high"},
                        {"user_query": "high"},
                        {"conversation": "medium"}
                    ]
                },
                "response": {
                    "format": "markdown",
                    "style": "concise"
                }
            }
        }
    
    def process_query(self, location: str) -> Dict[str, Any]:
        """处理天气查询请求"""
        try:
            # 获取天气数据
            weather_data = self.weather_api.get_weather(location)
            parsed_data = self.weather_api.parse_weather_data(weather_data)
            
            # 构建上下文
            context = {
                "type": "weather_query",
                "location": location,
                "data": parsed_data
            }
            self.context.append(context)
            
            # 生成提示词
            prompt = self._generate_prompt(parsed_data)
            
            # 返回处理结果
            return {
                "status": "success",
                "context": context,
                "prompt": prompt,
                "data": parsed_data
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _generate_prompt(self, weather_data: Dict[str, Any]) -> str:
        """生成提示词"""
        return Config.PROMPT_TEMPLATE.format(
            location=weather_data["location"],
            weather_data=str(weather_data)
        )
    
    def update_context(self, max_items: int = 5):
        """更新上下文，保持最新的N条记录"""
        if len(self.context) > max_items:
            self.context = self.context[-max_items:] 