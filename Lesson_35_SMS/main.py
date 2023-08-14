import requests
import os
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
API = "caee46e9e99be2fda623af3e12889f8d"
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

account_sid = 'ACf12f62297cfd7d52a6f185c4cf5ce2bf'
auth_token = '773a0eb97a3cbd89e8957f5e98c5a975'
if rain:

    client = Client(account_sid, auth_token)
    message = client.messages.create(
      from_='+447862137479',
      body='Get an umbrella',
      to='+447739104731'
    )


