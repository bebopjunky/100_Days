import requests
from datetime import datetime

MY_LAT = 50.822529
MY_LONG = -0.137163
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="Http://api-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_lon = float(data["iss_position"]["longitude"])

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":"))
sunset = int(data["results"]["sunset"].split("T")[1].split(":"))
time_now = datetime.now()



