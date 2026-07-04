import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read API key from environment variable
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Base URL for OpenWeather current weather API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Kenya county monitoring locations
# Each county is represented by a major town / county headquarters
COUNTY_LOCATIONS = [
    {"county": "Mombasa", "location": "Mombasa"},
    {"county": "Kwale", "location": "Kwale"},
    {"county": "Kilifi", "location": "Kilifi"},
    {"county": "Tana River", "location": "Hola"},
    {"county": "Lamu", "location": "Lamu"},
    {"county": "Taita Taveta", "location": "Voi"},
    {"county": "Garissa", "location": "Garissa"},
    {"county": "Wajir", "location": "Wajir"},
    {"county": "Mandera", "location": "Mandera"},
    {"county": "Marsabit", "location": "Marsabit"},
    {"county": "Isiolo", "location": "Isiolo"},
    {"county": "Meru", "location": "Meru"},
    {"county": "Tharaka Nithi", "location": "Chuka"},
    {"county": "Embu", "location": "Embu"},
    {"county": "Kitui", "location": "Kitui"},
    {"county": "Machakos", "location": "Machakos"},
    {"county": "Makueni", "location": "Wote"},
    {"county": "Nyandarua", "location": "Ol Kalou"},
    {"county": "Nyeri", "location": "Nyeri"},
    {"county": "Kirinyaga", "location": "Kerugoya"},
    {"county": "Murang'a", "location": "Murang'a"},
    {"county": "Kiambu", "location": "Kiambu"},
    {"county": "Turkana", "location": "Lodwar"},
    {"county": "West Pokot", "location": "Kapenguria"},
    {"county": "Samburu", "location": "Maralal"},
    {"county": "Trans Nzoia", "location": "Kitale"},
    {"county": "Uasin Gishu", "location": "Eldoret"},
    {"county": "Elgeyo Marakwet", "location": "Iten"},
    {"county": "Nandi", "location": "Kapsabet"},
    {"county": "Baringo", "location": "Kabarnet"},
    {"county": "Laikipia", "location": "Nanyuki"},
    {"county": "Nakuru", "location": "Nakuru"},
    {"county": "Narok", "location": "Narok"},
    {"county": "Kajiado", "location": "Kajiado"},
    {"county": "Kericho", "location": "Kericho"},
    {"county": "Bomet", "location": "Bomet"},
    {"county": "Kakamega", "location": "Kakamega"},
    {"county": "Vihiga", "location": "Vihiga"},
    {"county": "Bungoma", "location": "Bungoma"},
    {"county": "Busia", "location": "Busia"},
    {"county": "Siaya", "location": "Siaya"},
    {"county": "Kisumu", "location": "Kisumu"},
    {"county": "Homa Bay", "location": "Homa Bay"},
    {"county": "Migori", "location": "Migori"},
    {"county": "Kisii", "location": "Kisii"},
    {"county": "Nyamira", "location": "Nyamira"},
    {"county": "Nairobi", "location": "Nairobi"},
]