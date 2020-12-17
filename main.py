import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


weather_params = {
    "lat": 53.419790,
    "lon": -6.395090,
    "appid": os.getenv("API_KEY"),
    "exclude": "current,minutely,daily",
}
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
data = response.json()
half_day_data = data["hourly"][:12]

will_rain = False

for hour_data in half_day_data:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella",
            from_=os.environ['FROM_NUMBER'],
            to=os.environ['NUMBER'],
    )
    print(message.status)
