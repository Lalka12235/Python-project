import requests

API_KEY = '1ac22cb3c999aa6916292b67f78d5a62'

def get_weather(city):
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        if city:
            response = requests.get(URL)
            if response.status_code == 200:  # Проверка успешности запроса
                data = response.json()
                cityName = f"{data['name']} 🌆 - Город"
                temp = f"{data['main']['temp']} °C 🌡️ - Температура"
                humidity = f"{data['main']['humidity']}% 💧 - Влажность"
                weather = f"{data['weather'][0]['description']} ☁️ - Погода"
                wind = f"{data['wind']['speed']} м/с 🌬️ - Ветер"
                print(cityName)
                print(temp)
                print(humidity)
                print(weather)
                print(wind)
            else:
                print('Город не найден:', data.get('message', 'Нет дополнительной информации'))
        else:
            return None, None
    except Exception as e:
        print('Произошла ошибка:', e)
    finally:
        print('-------')

while True:
    city = input('Введите название города (или введите "выход" для завершения): ')
    if city.lower() == 'выход':
        break
    try:
        get_weather(city)
    except Exception as e:
        print('Ошибка не найдена', e)