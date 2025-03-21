import asyncio
from typing import Dict, Any
from aiohttp import web
from .weather_mcp import WeatherMCP

class MCPServer:
    def __init__(self):
        self.app = web.Application()
        self.weather_mcp = WeatherMCP()
        self.setup_routes()
    
    def setup_routes(self):
        """设置路由"""
        self.app.router.add_post("/api/weather", self.handle_weather_query)
        self.app.router.add_get("/health", self.health_check)
    
    async def handle_weather_query(self, request: web.Request) -> web.Response:
        """处理天气查询API请求"""
        try:
            data = await request.json()
            location = data.get("location")
            if not location:
                return web.json_response(
                    {"error": "Location is required"},
                    status=400
                )
            
            result = self.weather_mcp.process_query(location)
            return web.json_response(result)
            
        except Exception as e:
            return web.json_response(
                {"error": str(e)},
                status=500
            )
    
    async def health_check(self, request: web.Request) -> web.Response:
        """健康检查端点"""
        return web.json_response({"status": "healthy"})
    
    async def start(self, host: str = "localhost", port: int = 8080):
        """启动服务器"""
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, host, port)
        await site.start()
        print(f"MCP Server running on http://{host}:{port}") 