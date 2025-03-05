import os
import telebot
from dotenv import load_dotenv
from testWeather import get_weather

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    text = "Hello! I am a CLOUDFATHER\n\nEnter the CITY you want weather information for"
    bot.reply_to(message, text)


@bot.message_handler(func=lambda message: True)
def city_handler(message):
    city = message.text
    weather_info = get_weather(city)
    text = f'🔍 Getting weather information for {city}'
    bot.reply_to(message.chat.id, text, parse_mode='Markdown')
    
    if weather_info:
        response = f"🌍 *City*: {weather_info['city']}\n\n" \
                   f"🌡 *Temperature*: {weather_info['temperature']}K\n\n" \
                   f"💧 *Humidity*: {weather_info['humidity']}%\n\n" \
                   f"🌀 *Wind Speed*: {weather_info['wind_speed']}m/s\n\n" \
                   f"🌬 *Pressure*: {weather_info['pressure']}hPa\n\n" \
                   f"📝 *Description*: {weather_info['description']}"
        
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Sorry, couldn't find weather information for that city.", parse_mode='Markdown')


bot.infinity_polling()