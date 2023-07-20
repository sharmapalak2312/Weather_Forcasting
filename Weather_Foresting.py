import requests

def get_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": location, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(data):
    if data["cod"] == "404":
        print("Error: City not found. Please check the spelling or try a different location.")
    elif data["cod"] == 200:
        weather_desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        print(f"Weather: {weather_desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Error: Unable to fetch weather data for the given location. Please try again later.")

def main():
    api_key = "7f5c50f5d98068f2bd2f0727db99ab7a"

    while True:
        print("\n-- Weather Forecast Application --")
        location = input("Enter the city or zip code (or 'exit' to quit): ")

        if location.lower() == "exit":
            print("Exiting the application.")
            break

        weather_data = get_weather_data(api_key, location)
        print(weather_data)
        display_weather(weather_data)

if __name__ == "__main__":
    main()
