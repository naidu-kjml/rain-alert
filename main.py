import requests
import os
from dotenv import load_dotenv
load_dotenv()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"


weather_params = {
    "lat": 53.419790,
    "lon": -6.395090,
    "appid": os.getenv("API_KEY"),
    "exclude": "current,minutely,daily",
}
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()
print(data)
