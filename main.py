import telebot
import json
from flask import Flask, request
import os
import  requests
import logging
logging.basicConfig(level=logging.INFO)

api = '7824625079:AAHA4CJaM9lCEJDblzMecLWZ0q2wUMxyQHA'

bot = telebot.TeleBot(api)

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





