import requests


def get_weather_data(api_key, location):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": api_key,
        "units": "metric",  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print("Error:", data.get("message", "An error occurred."))
            return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None


def display_weather(data):
    if data:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
        print(f"Wind Speed: {wind_speed} m/s")


if __name__ == "__main__":
    api_key = "ebfc69f3caff1783c8594b95d0598e92"   # Replace with your actual OpenWeatherMap API key

    location = input("Enter a city name or zip code: ")

    weather_data = get_weather_data(api_key, location)

    if weather_data:
        display_weather(weather_data)
