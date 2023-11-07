import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("api_key")

weather_params = {
    "lat": 40.342430,
    "lon": -74.664574,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
SID = os.environ.get("SID")
token = os.environ.get("token")

client = Client(SID, token)
for x in range(0, 12):
    if int(weather_data["hourly"][x]["weather"][0]["id"]) < 700:
        message = client.messages.create(
            from_='+18559260376',
            body='Bring an Umbrella',
            to='+13453457548'
        )
        print(message.sid)
