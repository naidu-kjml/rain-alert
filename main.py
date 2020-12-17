import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "8e41d0067ebf2047856f1346b0557899"

weather_params = {
    "lat": 53.419790,
    "lon": -6.395090,
    "appid": API_KEY,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()
print(data)
