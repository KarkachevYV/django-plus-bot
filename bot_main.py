# bot_main.py
from telebot.types import Message
import os
import telebot
import requests
from dotenv import load_dotenv


# Загрузка переменных из .env файла
load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

API_URL = "http://127.0.0.1:8000/api"

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_command(message: Message):
    data = {
        "user_id": message.from_user.id, 
        "username": message.from_user.username
    }
    response = requests.post(API_URL + "/register/", json=data)
    if response.status_code == 200:
        if response.json().get('message'):
            bot.send_message(message.chat.id, "Вы уже были зарегистрированы ранее!")
        else:
            bot.send_message(message.chat.id, f"Вы успешно зарегистрированы! Ваш уникальный номер: {response.json()['id']}")
    else:
        bot.send_message(message.chat.id, "Произошла ошибка при регистрации!")
        print(response.json())
        print(response.status_code)
        print(response.text)

@bot.message_handler(commands=['myinfo'])
def user_info(message: Message):
    response = requests.get(f"{API_URL}/user/{message.from_user.id}/")
    if response.status_code == 200:
       bot.reply_to(message, f"Ваша регистрация:\n\n{response.json()}")
    elif response.status_code == 404:
      bot.send_message(message.chat.id, "Вы не зарегистрированы!")
    else:
        bot.send_message(message.chat.id, "Непредвиденная ошибка!")
        
        
if __name__ == "__main__":
    bot.polling(none_stop=True)