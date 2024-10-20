import telebot
import json
from telebot import types
from datetime import date, timedelta


TOKEN = "7440216915:AAHDKvA34Gs-Fqo9x9JdnsISLqMehQ5FOvI"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "Бот для записи на процедуры запущен")


@bot.message_handler(commands=["set_name"])
def handle_set_name(message):
    bot.send_message(message.chat.id, "Как вас зовут?")
    bot.register_next_step_handler_by_chat_id(message.chat.id, lambda message: save_client(message))


@bot.message_handler(commands=["add_review"])
def handle_add_review(message):
    bot.send_message(message.chat.id, "Напишите отзыв:")
    bot.register_next_step_handler_by_chat_id(message.chat.id, save_review)


def save_review(message):
    client_id = message.chat.id
    review_text = message.text
    # запись отзыва в файл
    add_review(client_id, review_text)
    bot.send_message(message.chat.id, "Спасибо за ваш отзыв")


def save_client(message):
    try:
        # открытие файл и чтения
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"appointments": [], "review": [], "clients": {}}
        print("Файл не найден")

    # добавление новой записи в "id"
    data["clients"][str(message.chat.id)] = message.text

    # сохранения в файл json новые записи
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    bot.send_message(message.chat.id, "Ваше имя сохранено")


@bot.message_handler(commands=["make_an_appointment"])
def handle_show_dates(message):
    keyboard_3 = generate_procedure_keyboard()
    bot.send_message(message.chat.id, "Выберите процедуру: ", reply_markup=keyboard_3)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if "procedure" in call.data:
        chosen_procedure = call.data.replace("procedure: ", "")
        # print(chosen_procedure)
        bot.send_message(call.message.chat.id, f"Вы выбрали процедуру {chosen_procedure}")
        bot.send_message(call.message.chat.id, "Выберите дату:", reply_markup=generate_date_keyboard(chosen_procedure))
    elif "День" in call.data:
        # print(call.data)
        chosen_procedure, chosen_data = call.data.split(": ")[1], call.data.split(": ")[2]
        bot.send_message(call.message.chat.id, f"Вы выбрали дату {chosen_data}")
        print(chosen_data)
        bot.send_message(call.message.chat.id, "Выберите время:", reply_markup=generate_time_keyboard(chosen_procedure, chosen_data))
    elif "meeting" in call.data:
        # print(call.data)
        chosen_time, chosen_date, chosen_procedure = call.data.split(": ")[2], call.data.split(": ")[1], call.data.split(": ")[3]
        add_appointment(chosen_date, chosen_time, call.message.chat.id, chosen_procedure)
        bot.send_message(call.message.chat.id, f"Вы записаны на процедуру {chosen_procedure} на {chosen_date} в "
                                               f"{chosen_time}. Ждём вас!")


def generate_date_keyboard(procedure):
    # клавиатура
    keyboard = types.InlineKeyboardMarkup()
    days = []

    # добавление неск. кнопок
    for i in range(7):
        days.append(date.today() + timedelta(days=3 + i))

    for day in days:
        button_text = day.strftime("%d-%m-%Y")
        callback_data = f"День: {procedure}: {button_text}"
        button = types.InlineKeyboardButton(text=button_text, callback_data=callback_data)
        keyboard.add(button)

    return keyboard


def generate_time_keyboard(procedure, date):
    keyboard_2 = types.InlineKeyboardMarkup()
    times = ["10:00", "12:00", "15:00", "17:00"]

    with open("data.json", "r", encoding="utf-8") as file:
        file = json.load(file)

        for appointment in file["appointments"]:
            if appointment["date"] == date:
                times.remove(appointment["time"])

    for time in times:
        callback_time = f"meeting: {date}: {time}: {procedure}"
        button = types.InlineKeyboardButton(text=time, callback_data=callback_time)
        keyboard_2.add(button)
    return keyboard_2


def generate_procedure_keyboard():
    keyboard_3 = types.InlineKeyboardMarkup()
    procedures = ["чистка лица", "наращивание ресниц", "массаж лица, шеи, головы", "химический пилинг",
                  "окрашивание волос"]

    for procedure in procedures:
        callback_procedure = f"procedure: {procedure}"
        button = types.InlineKeyboardButton(text=procedure, callback_data=callback_procedure)
        keyboard_3.add(button)
    return keyboard_3


def add_appointment(new_date, new_time, client, new_procedure):
    try:
        # открытие файл и чтения
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"appointments": [], "review": [], "clients": {}}
        print("Файл не найден")

    # добавление новой записи в "appointment"
    new_appointment = {"date": new_date, "time": new_time, "client": client, "procedure": new_procedure}
    data["appointments"].append(new_appointment)

    # сохранения в файл json новые записи
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_review(client, text):
    try:
        # открытие файл и чтения
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"appointments": [], "review": [], "clients": {}}
        print("Файл не найден")

    # добавление новой записи в "review"
    new_review = {"client": client, "text": text}
    data["review"].append(new_review)

    # сохранения в файл json новые записи
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    bot.polling(non_stop=True)