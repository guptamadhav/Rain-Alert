import requests
import os
from twilio.rest import Client
api_key = " "
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
parameters = {
    "lat": latitude,
    "lon": longitude,
    "exclude": "current,minutely,daily,alerts",
    "appid": os.environ.get("APP_ID")
}
data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data.raise_for_status()
id = []
weather_report = data.json()["hourly"]
for i in weather_report[:12]:
    for j in range(len(i["weather"])):
        hourly_id = i["weather"][j]["id"]
        id.append(hourly_id)

will_rain = False
for i in id:
    if i <700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
         .create(
         body="Its going to rain today. Carry an umbrella☂️",
         from_='+17692274846',
         to=os.environ.get("PHONE_NUMBER")
    )
     print(message.status)
