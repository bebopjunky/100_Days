import requests
import os
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
API = 
LAT = 50.822529
LON = -0.137163

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

daily = data["hourly"][:12]

rain = False

for codes in daily:
    conditions = codes["weather"][0]["id"]
    if int(conditions) < 700:
        rain = True

account_sid = 
auth_token =
if rain:

    client = Client(account_sid, auth_token)
    message = client.messages.create(
      from_='
      body='Get an umbrella',
      to=
    )


