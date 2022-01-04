import os
from dotenv import load_dotenv

load_dotenv()

open_weather_token = os.getenv("OPEN_WEATHER_TOKEN")
tg_bot_token = os.getenv("BOT_TOKEN")
