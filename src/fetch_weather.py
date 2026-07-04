import requests
from datetime import datetime
from config import OPENWEATHER_API_KEY, BASE_URL


def fetch_location_weather(county, location):
    """
    Fetch current weather data for a county using a representative location.
    """

    if not OPENWEATHER_API_KEY:
        raise ValueError("OPENWEATHER_API_KEY is missing. Please check your .env file.")

    params = {
        "q": f"{location},KE",
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params, timeout=30)

    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch data for {county} using location {location}: {response.text}"
        )

    data = response.json()

    weather_record = {
        "county": county,
        "location_used": location,
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "weather_main": data["weather"][0]["main"],
        "weather_description": data["weather"][0]["description"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return weather_record