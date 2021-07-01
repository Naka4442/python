import telebot

bot = telebot.TeleBot("1882504670:AAFRTjFnT62hv9kIp6v9FxKHCSLQz9xeLyU")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, "Привет! Я бот, который поможет тебе найти любимую песню!")

@bot.message_handler(commands=["findArtist"])
def findArtist(message):
    bot.send_message(message.from_user.id, "Вы решили найти артиста? Напишите его имя")
    bot.register_next_step_handler(message, getArtistName)

def getArtistName(message):
    name = message.text

bot.polling(none_stop=True)