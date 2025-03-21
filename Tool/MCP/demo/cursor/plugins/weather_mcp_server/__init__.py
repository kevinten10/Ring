from typing import Dict, Any
from cursor.plugin import Plugin, register_plugin
from .weather_mcp import WeatherMCP

@register_plugin
class WeatherMCPServer(Plugin):
    """Cursor天气查询MCP服务插件"""
    
    def __init__(self):
        super().__init__()
        self.weather_mcp = WeatherMCP()
        self.name = "weather_mcp_server"
        self.description = "Weather MCP Server for Cursor"
    
    async def activate(self):
        """插件激活时的初始化"""
        self.register_command(
            "weather.query",
            self.handle_weather_query,
            "Query weather information for a location"
        )
    
    async def deactivate(self):
        """插件停用时的清理"""
        pass
    
    async def handle_weather_query(self, location: str) -> Dict[str, Any]:
        """处理天气查询命令"""
        try:
            result = self.weather_mcp.process_query(location)
            if result["status"] == "success":
                return {
                    "type": "weather_info",
                    "data": result["data"],
                    "prompt": result["prompt"]
                }
            else:
                return {
                    "type": "error",
                    "message": result["error"]
                }
        except Exception as e:
            return {
                "type": "error",
                "message": str(e)
            } 