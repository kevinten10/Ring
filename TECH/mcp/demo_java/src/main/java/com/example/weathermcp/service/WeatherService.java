package com.example.weathermcp.service;

import com.example.weathermcp.model.WeatherData;
import io.modelcontextprotocol.mcp.*;
import org.springframework.stereotype.Service;

@Service
public class WeatherService implements MCPHandler {
    private final WeatherAPIService weatherAPIService;
    private final MCPMessageProcessor messageProcessor;

    public WeatherService(WeatherAPIService weatherAPIService, 
                         MCPMessageProcessor messageProcessor) {
        this.weatherAPIService = weatherAPIService;
        this.messageProcessor = messageProcessor;
    }

    @Override
    public Response handle(Message message, Context context) {
        try {
            // 提取并验证location参数
            String location = messageProcessor.extractLocation(message);
            if (!messageProcessor.validateLocation(location)) {
                return Response.builder()
                        .error("Invalid location format")
                        .build();
            }

            WeatherData weatherData = weatherAPIService.getWeather(location);
            
            // 构建提示词
            String prompt = generatePrompt(weatherData);
            
            // 更新上下文
            context.add("weather_data", weatherData);
            context.add("location", location);
            
            return Response.builder()
                    .content(prompt)
                    .build();
        } catch (Exception e) {
            return Response.builder()
                    .error(e.getMessage())
                    .build();
        }
    }

    private String generatePrompt(WeatherData data) {
        return String.format("""
            You are a helpful weather assistant. Please provide weather information for %s.
            Current weather data:
            - Temperature: %.1f°C
            - Condition: %s
            - Humidity: %d%%
            - Wind Speed: %.1f km/h
            Please format your response in a clear and concise way.
            """,
            data.getLocation(),
            data.getTemperature(),
            data.getCondition(),
            data.getHumidity(),
            data.getWindSpeed()
        );
    }
} 