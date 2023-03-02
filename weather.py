def get_weather(city) -> tuple:
    from config import TOKEN
    import requests
    try:
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={TOKEN}&units=metric&lang=ru"
        )
        data = req.json()

        city = data["name"]
        temp = data["main"]["temp"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        result = (
            city,
            temp,
            temp_max,
            temp_min,
            humidity,
            description
        )
        result = tuple(map(str, result))

        return result
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(get_weather("London"))