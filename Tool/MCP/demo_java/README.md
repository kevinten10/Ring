# Weather MCP Demo (Java)

基于MCP Java SDK实现的天气查询示例，展示了如何使用Java构建MCP应用。

## 目录结构
```
demo_java/
├── src/
│   └── main/
│       ├── java/
│       │   └── com/
│       │       └── example/
│       │           └── weathermcp/
│       │               ├── WeatherMCPApplication.java
│       │               ├── config/
│       │               │   └── WeatherConfig.java
│       │               ├── service/
│       │               │   ├── WeatherService.java
│       │               │   └── WeatherAPIService.java
│       │               └── model/
│       │                   └── WeatherData.java
│       └── resources/
│           ├── application.yml
│           └── mcp/
│               └── weather-rules.yml
├── pom.xml
└── README.md
``` 