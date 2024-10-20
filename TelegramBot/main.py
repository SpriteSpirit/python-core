import telebot

TOKEN = '6835394679:AAHuENYE6SgJyMNq1sEzB_filMsLGT8MOL4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hello! I'm bot.")


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(non_stop=True)
