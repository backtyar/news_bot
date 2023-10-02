from decouple import config
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json


bot = telebot.TeleBot(config('TOKEN'))
text = ''


@bot.message_handler(commands=['start'])
def start_commands(message):
    global text
    text = 'добро пожаловать'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def menu_news(message):
    global text
    markup = InlineKeyboardMarkup(row_width=1)
    if message.text.lower() == 'новасти':
        with open('news_dict.json', 'r') as file:
            data = json.load(file)
            for i in data:
                button = InlineKeyboardButton(str(i), url=data[i]['Ссылки'])
                markup.add(button)
    else:
        text = 'Для получения списка  новостей напишите слова "новасти"'
    bot.reply_to(message,text=text,reply_markup=markup)

@bot.message_handler(content_types=['video','photo','sticker','voice',])
def filter_message(message):
    global text
    text = 'Бот реагирует только на текстовые сообщение'
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, text)


bot.polling()




