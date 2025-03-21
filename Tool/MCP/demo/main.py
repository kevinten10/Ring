from weather_mcp import WeatherMCP

def main():
    # 初始化WeatherMCP
    weather_mcp = WeatherMCP()
    
    try:
        # 示例查询
        location = input("Enter location for weather query: ")
        result = weather_mcp.process_query(location)
        
        if result["status"] == "success":
            print("\nWeather Information:")
            print(f"Location: {result['data']['location']}, {result['data']['country']}")
            print(f"Temperature: {result['data']['temperature']}°C")
            print(f"Condition: {result['data']['condition']}")
            print(f"Humidity: {result['data']['humidity']}%")
            print(f"Wind Speed: {result['data']['wind_speed']} km/h")
        else:
            print(f"Error: {result['error']}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 