package com.example.weathermcp.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

@Data
@Configuration
@ConfigurationProperties(prefix = "weather")
public class WeatherConfig {
    private String apiKey;
    private String apiUrl;
    private int maxRetries;
    private int timeout;
} 