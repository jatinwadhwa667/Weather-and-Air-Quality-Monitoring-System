import os
import logging
import requests
from dotenv import load_dotenv


# Load variables from .env file
load_dotenv()

# Get API key
API_KEY = os.getenv("API_KEY")


# Configure logger
logging.basicConfig(
    filename="weather.log",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# Check API key
if not API_KEY:
    logger.error("API key not found in .env file")
    exit()


# Ask user for city
city = input("Enter city name: ").strip()

if not city:
    logger.error("City name cannot be empty")
    exit()


# API URLs
weather_url = "https://api.openweathermap.org/data/2.5/weather"
air_quality_url = "https://api.openweathermap.org/data/2.5/air_pollution"


try:
    # Call 1: Current Weather API

    logger.info("Getting weather data for %s", city)

    weather_params = {
        "q": city,
        "appid": API_KEY
    }

    response = requests.get(
        weather_url,
        params=weather_params,
        timeout=10
    )

    response.raise_for_status()

    weather_data = response.json()

    # Extract weather description
    description = weather_data["weather"][0]["description"]

    # Extract temperature
    temperature_kelvin = weather_data["main"]["temp"]

    # Kelvin to Celsius
    temperature_celsius = temperature_kelvin - 273.15

    # Extract latitude and longitude
    latitude = weather_data["coord"]["lat"]
    longitude = weather_data["coord"]["lon"]

    logger.info("Weather data received successfully")
    logger.info("Latitude: %s, Longitude: %s", latitude, longitude)


    # Call 2: Air Quality API

    logger.info("Getting air quality data")

    air_quality_params = {
        "lat": latitude,
        "lon": longitude,
        "appid": API_KEY
    }

    response = requests.get(
        air_quality_url,
        params=air_quality_params,
        timeout=10
    )

 
    response.raise_for_status()

    air_quality_data = response.json()

    print(air_quality_data)
    

    # Extract AQI
    aqi = air_quality_data["list"][0]["main"]["aqi"]


    # AQI meaning
    aqi_meaning = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor"
    }

    aqi_status = aqi_meaning.get(aqi, "Unknown")


    # Display result

    print("\n" + "=" * 40)
    print(f"Weather Report for: {city}")
    print("=" * 40)

    print(f"Current Weather: {description}")
    print(f"Temperature: {temperature_celsius:.1f}°C")
    print(f"Air Quality (AQI): {aqi} ({aqi_status})")
    print(f"coordinates : Latitude: {latitude} , Longitude: {longitude}")

    print("=" * 40)

    logger.info("Weather report generated successfully")


except requests.exceptions.HTTPError as e:

    logger.error("HTTP error occurred: %s", e)

    try:
        error_message = response.json().get(
            "message",
            "Unknown API error"
        )

        print(f"\nError: {error_message}")

    except Exception:
        print("\nAn API error occurred.")


except requests.exceptions.Timeout:

    logger.error("Request timed out")
    print("\nError: Request timed out. Please try again.")


except requests.exceptions.ConnectionError:

    logger.error("Connection error")
    print("\nError: Could not connect to the API.")


except requests.exceptions.RequestException as e:

    logger.error("Request error: %s", e)
    print("\nError while calling API.")


except KeyError as e:

    logger.error("Missing key in API response: %s", e)
    print("\nError: Unexpected API response.")


except Exception as e:

    logger.exception("Unexpected error occurred")
    print("\nSomething went wrong.")
