import telebot

from config import TOKEN
bot = telebot.TeleBot(TOKEN)
gmail = "kubzero.1.0@gmail.com"

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Привет,это Телебот")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "Полезный телебот")

@bot.message_handler(commands=["Creator_info"])
def send_info(message):
    bot.reply_to(message, "Почта:kubzero.1.0@gmail.com")


bot.infinity_polling()