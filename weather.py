def get_weather(city) -> tuple:
    from config import TOKEN
    import requests
    #from pprint import pprint
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN}&units=metric&lang=ru"
        )
        data = req.json()

        if data['cod'] == '404':
            return ('Город не найден', 'None', 'None', 'None', 'None', 'None', "source/01d.png")

        city = data["name"]
        temp = data["main"]["temp"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        humidity = str(data["main"]["humidity"]) + "%"
        description = data["weather"][0]["description"]
        icon = "source/" + data['weather'][0]['icon'] + ".png"

        result = (
            city,
            temp,
            temp_max,
            temp_min,
            humidity,
            description,
            icon
        )
        result = tuple(map(str, result))

        return result
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(get_weather("Лондон"))