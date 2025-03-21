package com.example.weathermcp.service;

import com.example.weathermcp.config.WeatherConfig;
import com.example.weathermcp.model.WeatherData;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class WeatherAPIService {
    private final WeatherConfig config;
    private final RestTemplate restTemplate;

    public WeatherAPIService(WeatherConfig config) {
        this.config = config;
        this.restTemplate = new RestTemplate();
    }

    public WeatherData getWeather(String location) {
        String url = String.format("%s/current.json?key=%s&q=%s",
                config.getApiUrl(), config.getApiKey(), location);
        
        var response = restTemplate.getForObject(url, WeatherResponse.class);
        return convertToWeatherData(response);
    }

    private WeatherData convertToWeatherData(WeatherResponse response) {
        var data = new WeatherData();
        data.setLocation(response.getLocation().getName());
        data.setCountry(response.getLocation().getCountry());
        data.setTemperature(response.getCurrent().getTempC());
        data.setCondition(response.getCurrent().getCondition().getText());
        data.setHumidity(response.getCurrent().getHumidity());
        data.setWindSpeed(response.getCurrent().getWindKph());
        return data;
    }

    @Data
    private static class WeatherResponse {
        private Location location;
        private Current current;
    }

    @Data
    private static class Location {
        private String name;
        private String country;
    }

    @Data
    private static class Current {
        private double tempC;
        private Condition condition;
        private int humidity;
        private double windKph;
    }

    @Data
    private static class Condition {
        private String text;
    }
} 