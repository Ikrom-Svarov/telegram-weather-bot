import requests
from datetime import datetime
OPENWEATHERTOKEN ='e1e7ae891d7a54ab67630d95f85cd373'
city = input('City name:')
try:
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERTOKEN}&units=metric&lang=ru')
    data = response.json()

    # with open('file.text','w') as f:
    #     f.write(str(data))

    city = data["name"]
    des = data["weather"][0]["description"]
    temp = data ["main"]["temp"]
    humidity = data ["main"]["humidity"]
    wind = data ["wind"]["speed"]
    country = data ["sys"]["country"]
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
    sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")
    print(
        f"Current temp:{temp}\n"
        f"Weather:{des}\n"
        f"Humidity:{humidity}\n"
        f"Wind speed: {wind}\n"
        f"Country code: {country}\n"
        f"Sunrise:{sunrise}\n"
        f"Sunset:{sunset}\n"
    )
except Exception as ex:
    print(ex)







