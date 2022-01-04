import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Salom!. Shahar nomini kiriting.")


@dp.message_handler()
async def get_weather(message: types.Message):

    code_to_smile = {
        "Clear": "Yaxshi \U00002600",
        "Clouds": "Bulutli \U00002601",
        "Rain": "Yomg\'ir \U00002614",
        "Drizzle": "Yomg\'ir \U00002614",
        "Thunderstorm": "Chaqmoq \U000026A1",
        "Snow": "Qor \U0001F328",
        "Mist:": "Tuman \U0001F32B"
    }
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data['name']
        current_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_time - sunrise_time
        weather_description = data['weather'][0]['main']

        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = ""

        await message.reply(f"*** {datetime.datetime.now().strftime('%H:%M %d.%m.%Y')} ***\n"
              f"Ko\'rsatilayotgan manzil: {city}\n"
              f"Harorat: {current_weather}C° {wd}\n"
              f"Namlik: {humidity}%\n"
              f"Bosim: {pressure} Pa\n"
              f"Shamol tezligi: {wind_speed} m/s\n"
              f"Quyosh chiqish vaqti: {sunrise_time}\n"
              f"Quyosh botish vaqti: {sunset_time}\n"
              f"Kun davomiyligi: {length_of_day}\n"
              f"Kuningiz yaxshi o\'tsin!")

    except:
        await message.reply("\U00002620 Shahar nomini qayta tekshiring.")


def main():
    city = input("Shahar nomini kiriting:  ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    executor.start_polling(dp)
