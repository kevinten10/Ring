package com.example.weathermcp.controller;

import com.example.weathermcp.service.WeatherService;
import io.modelcontextprotocol.mcp.Context;
import io.modelcontextprotocol.mcp.Message;
import io.modelcontextprotocol.mcp.Response;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/weather")
public class WeatherController {
    
    private final WeatherService weatherService;
    
    public WeatherController(WeatherService weatherService) {
        this.weatherService = weatherService;
    }
    
    @PostMapping("/query")
    public Response queryWeather(@RequestBody WeatherRequest request) {
        // 创建MCP消息
        Message message = Message.builder()
                .content(request.getLocation())
                .build();
                
        // 创建上下文
        Context context = new Context();
        
        // 调用MCP处理器
        return weatherService.handle(message, context);
    }
    
    @Data
    public static class WeatherRequest {
        private String location;
    }
} 