import requests

def get_weather(city):

    # ---------- STEP 1 : Find Coordinates ----------

    geo_url = (
        f"https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )

    geo_data = requests.get(geo_url).json()

    if "results" not in geo_data:
        return f"Sorry Boss, I couldn't find {city}."

    location = geo_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]
    city = location["name"]
    country = location["country"]

    # ---------- STEP 2 : Get Weather ----------

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
    )

    weather_data = requests.get(weather_url).json()

    current = weather_data["current"]

    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind = current["wind_speed_10m"]
    code = current["weather_code"]

    weather_codes = {

        0:"Clear sky",
        1:"Mainly clear",
        2:"Partly cloudy",
        3:"Overcast",
        45:"Fog",
        48:"Fog",
        51:"Light drizzle",
        53:"Moderate drizzle",
        55:"Heavy drizzle",
        61:"Light rain",
        63:"Moderate rain",
        65:"Heavy rain",
        71:"Light snow",
        73:"Moderate snow",
        75:"Heavy snow",
        80:"Rain showers",
        81:"Heavy rain showers",
        82:"Violent rain showers",
        95:"Thunderstorm"

    }

    condition = weather_codes.get(code,"Unknown")

    return (
        f"The weather in {city}, {country} is {condition}. "
        f"The temperature is {temperature} degree Celsius. "
        f"Humidity is {humidity} percent. "
        f"Wind speed is {wind} kilometers per hour."
    )