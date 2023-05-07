import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import open_weather_token

token = '6078326309:AAHyWOrGSr4h6I4FLcQ5Goi1KmaaEwLAx8I'
bot = Bot(token=token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
   await message.reply("Введите название города и я пришлю информацию о текущей погоде!")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        await message.reply(
              f"Ваш город {city}\n"
              f"температура: {cur_weather}°C\n"
              f"влажность {humidity}\n"
              f"давление {pressure}\n"
              f"скорость ветра {wind} км/ч\n"    
              )
    except:
        await message.reply("Проверить название города")


if __name__=='__main__':
    executor.start_polling(dp)
