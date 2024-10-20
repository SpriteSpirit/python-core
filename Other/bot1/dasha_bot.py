import telebot
import json
import random

TOKEN = "7130331980:AAHmoXTbpj1-cM-hR5FmE9U8aBTDVv8y5dQ"

bot = telebot.TeleBot(TOKEN)

with open("user_data.json", "r", encoding="utf-8") as file:
    user_data = json.load(file)


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет. Рада тебя видеть!")
    bot.send_message(message.chat.id, "Для того, чтобы разобраться как работает бот, нажми на команду /help")


@bot.message_handler(commands=["learn"])  # /learn 5
def handle_learn(message):
    # bot.send_message(message.chat.id, user_data)
    user_words = user_data.get(str(message.chat.id), {})  # берёт выборку слов пользователя
    print(len(user_words))

    try:
        words_number = int(message.text.split()[1])  # берёт количество слов для повторения
        ask_translation(message.chat.id, user_words, words_number)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка ввода. Введите количество в числовом значении")
    except IndexError:
        bot.send_message(message.chat.id, "Ошибка ввода. Введите количество слов для изучения")


def ask_translation(chat_id, user_words, words_left):
    if words_left > 0:
        word = random.choice(list(user_words.keys()))
        translation = user_words[word]
        bot.send_message(chat_id, f"Как переводится слово {word}")
        # следующие, что введет пользователь, должно обработать check_translation
        bot.register_next_step_handler_by_chat_id(chat_id, check_translation, translation, words_left)
    else:
        bot.send_message(chat_id, "Урок закончен")


def check_translation(message, expected_translation, words_left):
    user_translation = message.text.strip().lower()

    if user_translation == expected_translation.lower():
        bot.send_message(message.chat.id, "Молодец! Это верный перевод")
    else:
        bot.send_message(message.chat.id, f"Неверно, правильный перевод - {expected_translation}")
    words_left -= 1
    ask_translation(message.chat.id, user_data[str(message.chat.id)], words_left)


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, "Это бот для обучения английского языка.Для того чтобы проверить свои умения,"
                                      " нужно ввести: /learn ... (вместо троеточия должна быть цифра - количество "
                                      "карточек, которые появятся в чате. С помощью команды /addword можно добавить"
                                      " новые слова. Пример ввода: /addword *слово* *перевод слова*")


@bot.message_handler(commands=["addword"])
def handle_addword(message):
    global user_data  # делаем ее глобальной, чтобы могли ее изменять
    chat_id = str(message.chat.id)
    # user_dict = user_data.get(chat_id, {})  # вытаскиваем слова для пользователя
    user_dict = user_data.get(chat_id, {})  # Используем setdefault для получения или создания словаря

    words = message.text.split()[1:]

    if len(words) == 2:
        word, translation = words[0].lower(), words[1].lower()
        user_dict[word] = translation  # словарь пользователя

        user_data[chat_id] = user_dict

        with open("user_data.json", "w", encoding="utf-8") as file:
            json.dump(user_data, file, ensure_ascii=False, indent=4)
        bot.send_message(chat_id, f"Слово {word} успешно добавлено")
    else:
        bot.send_message(chat_id, "Произошла ошибка, попробуйте еще раз. Пример ввода: /addword *слово* *перевод*")


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    if message.text.lower() == "как тебя зовут?":
        bot.send_message(message.chat.id, "У меня пока что нету имени")
    elif message.text.lower() == "расскажи о себе":
        bot.send_message(message.chat.id, "Я бот для изучения английского языка")
    elif message.text.lower() == "сколько тебе лет?":
        bot.send_message(message.chat.id, "Мне 16")
    elif message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, "Отлично! Буду рад тебе в изучении английского")
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.polling(non_stop=True)