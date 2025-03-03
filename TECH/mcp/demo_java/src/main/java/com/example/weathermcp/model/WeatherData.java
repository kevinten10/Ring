package com.example.weathermcp.model;

import lombok.Data;

@Data
public class WeatherData {
    private String location;
    private String country;
    private double temperature;
    private String condition;
    private int humidity;
    private double windSpeed;
} 