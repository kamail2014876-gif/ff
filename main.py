import telebot
from random import randint
from datetime import datetime
import requests
import os
import gdown
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running"


@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_update([update])
    return '', 200leBot(api)

def load_db() :
    try:
            with open("db.json", 'r', encoding='utf-8') as f:
                return json.load(f)
    except FileNotFoundError:
        return {}

def save_db(data):
    with open("db.json", 'r', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

db = load_db()


@bot.message_handler(commands=[' start'])
def start (message) :
    user_id = str(message.from_user.id)


    if user_id not in db:
        db[user_id] = {"name":None, "age":None, 'money':100000, "state"}
    keyboardReply = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    helpButton = telebot. types. KeyboardButton("Помощь")
    infoButton = telebot. types. KeyboardButton("Инфо")
    aboutButton = telebot.types. KeyboardButton("0 боте")

    keyboardReply.add(helpButton, infoButton, aboutButton)


    bot.send_message(message.chat.id, "Hello Bot-World", reply_markup = keyboardReply)

@ bot.message_handler(commands = ['help'])

def help(message):
    bot.send_message(message.chat.id, "Инструкция по пользованию ботом")

@bot.message_handler(commands=[' info' ])
def info (message):
    bot. send_message (message.chat.id, "Информация о боте")
@bot.message_handler(content_types=['text'])
def text_event (message) :
    if message.text == "Помощь":
        pass
    elif message.text == "Инфо":
        pass
    elif message.text == "0 боте":
        bot. send_message(message.chat.id, message. text)


if __name__ == "__main__":
    server_url = os.getenv("RENDER_EXTERNAL_URL")
    if server_url and TOKEN:
        webhook_url = f"{server_url}/{TOKEN}"
        set_webhook_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={webhook_url}"
        try:
            r = requests.get(set_webhook_url)
            print("Webhook установлен:", r.text)
        except Exception as e:
            print("Ошибка при установке webhook:", e)

        port = int(os.environ.get("PORT", 10000))
        print(f"Starting server on port {port}")
        app.run(host='0.0.0.0', port=port)
    else:
        print("Запуск бота в режиме pooling")
        bot.remove_webhook()
        bot.polling(none_stop=True)



