#import telebot
#import config
import requests
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        print(
              f"Ваш город {city}\n"
              f"температура: {cur_weather}°C\n"
              f"влажность {humidity}\n"
              f"давление {pressure}\n"
              f"скорость ветра {wind}\n"    
              )
    except Exception as ex:
        print(ex)
        print("Проверить название города")

def main():
    city = input("Введите город")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
# bot = telebot.TeleBot(config.TOKEN)
 
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id, f"Добро пожаловать, {message.from_user.first_name}!")
    

# @bot.message_handler(content_types=['text'])
# def func(message):
#     bot.send_message(message.chat.id, message.text)

# bot.polling(none_stop=True)
