import ast

import telebot
from telebot import types
import json

ITEMS_PER_PAGE = 4
TOKEN = "7498576649:AAH1bU_NZP4HoJLw_w0eswBWEwJBRLjFmEg"

user_data = {}

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "Бот запущен", reply_markup=handle_selection())


# Команда /add_info
@bot.message_handler(commands=['add_info'])
def add_info(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    msg = bot.send_message(chat_id, "Введите ваше имя:")
    bot.register_next_step_handler(msg, process_name_step)


# Обработка имени
def process_name_step(message):
    chat_id = message.chat.id
    user_data[chat_id]['name'] = message.text
    msg = bot.send_message(chat_id, "Введите ваш номер телефона:")
    bot.register_next_step_handler(msg, process_phone_step)


# Обработка номера телефона
def process_phone_step(message):
    chat_id = message.chat.id
    user_data[chat_id]['phone'] = message.text
    bot.send_message(chat_id,
                     f"Ваше имя: {user_data[chat_id]['name']}\nВаш номер телефона: {user_data[chat_id]['phone']}")
    save_client(message, user_data[chat_id]['name'], user_data[chat_id]['phone'])


def save_client(message, client_name, client_phone):
    try:
        # открытие файл и чтения
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"clients": []}
        print("Файл не найден")

    # добавление новой записи в "id"
    new_client = {"id": str(message.chat.id), "name": client_name, "phone": client_phone, "cart": []}

    # data["clients"].append([str(message.chat.id)] = message.text)
    for client in data['clients']:
        if client.get('id') == str(message.chat.id):
            client['name'] = client_name
            client['phone'] = client_phone
            # client['cart'] = []
            break
    else:
        data['clients'].append(new_client)

    # сохранения в файл json новые записи
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    bot.send_message(message.chat.id, "Ваши данные сохранены")


menu_items = [
    {"name": "Грибной суп", "price": "450 руб.", "photo": "mushroom_soup.png"},
    {"name": "Салат Цезарь", "price": "550 руб.", "photo": "caesar.png"},
    {"name": "Утка с апельсинами", "price": "700 руб.", "photo": "duck_orange.png"},
    {"name": "Бефстроганов", "price": "650 руб.", "photo": "stroganoff.png"},
    {"name": "Ризотто", "price": "500 руб.", "photo": "risotto.png"},
    {"name": "Тирамису", "price": "400 руб.", "photo": "tiramisu.png"},
    {"name": "Блины", "price": "300 руб.", "photo": "pancakes.png"},
    {"name": "Паста Карбонара", "price": "550 руб.", "photo": "carbonara.png"},
    {"name": "Гаспачо", "price": "350 руб.", "photo": "gazpacho.png"},
    {"name": "Фалафель", "price": "400 руб.", "photo": "falafel.png"}

]


# создание клавиатуры
def generate_markup(page=0):
    # print('generate_markup')
    markup = types.InlineKeyboardMarkup()
    start_index = page * ITEMS_PER_PAGE
    end_index = start_index + ITEMS_PER_PAGE

    for item in menu_items[start_index:end_index]:
        button = types.InlineKeyboardButton(f'{item["name"]}: {item["price"]}',
                                            callback_data=f"item_{menu_items.index(item)}")
        markup.add(button)

    # Кнопки навигации
    if page > 0:
        markup.add(types.InlineKeyboardButton(text="<<", callback_data=f'page_{page - 1}'))
    if end_index < len(menu_items):
        markup.add(types.InlineKeyboardButton(text=">>", callback_data=f'page_{page + 1}'))

    return markup


# обработка меню
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # print('echo_all')
    if message.text == "Меню 🥩":
        bot.send_message(message.chat.id, "Выберите блюдо:", reply_markup=generate_markup())

    elif message.text == "Корзина 🛒":
        items_in_cart = get_cart(message.chat.id)
        markup = types.InlineKeyboardMarkup()

        for item in items_in_cart:
            minus_button = types.InlineKeyboardButton("-", callback_data=f"minus_{item}")
            name_button = types.InlineKeyboardButton(f"{item[0]} x{item[1]}", callback_data=f"name_{item}")
            plus_button = types.InlineKeyboardButton("+", callback_data=f"plus_{item}")

            markup.add(minus_button, name_button, plus_button)

        bot.send_message(message.chat.id, 'Корзина:', reply_markup=markup)

    elif message.text == "Заказать 🛍️":
        items_in_cart = get_cart(message.chat.id)
        markup = types.InlineKeyboardMarkup()
        sum_items = 0

        for item in items_in_cart:
            name_button = types.InlineKeyboardButton(f"{item[0]}: {item[1]}шт. x {item[2]} ₽", callback_data=f"name_{item}")
            markup.add(name_button)

            sum_items += item[1] * item[2]

        sum_button = types.InlineKeyboardButton('Заказать',
                                                callback_data=f"sum_{sum_items}")

        # Добавляем кнопки в строку markup
        if sum_items != 0:
            markup.add(sum_button)
            bot.send_message(message.chat.id, f'Сумма заказа: {sum_items} ₽', reply_markup=markup)


# получение всех товаров в корзине
def get_cart(client_id):
    with open("data.json", 'r', encoding="utf-8") as file:
        data = json.load(file)

    clients = data.get("clients", [])

    for client in clients:
        if client.get("id") == str(client_id):
            return client.get("cart", [])

    return None  # Возвращаем None, если клиент с указанным ID не найден


# обновление корзины
def update_cart(chat_id):
    items_in_cart = get_cart(chat_id)

    markup = types.InlineKeyboardMarkup()

    for item in items_in_cart:
        minus_button = types.InlineKeyboardButton("-", callback_data=f"minus_{item}")
        name_button = types.InlineKeyboardButton(f"{item[0]} x{item[1]}", callback_data=f"name_{item}")
        plus_button = types.InlineKeyboardButton("+", callback_data=f"plus_{item}")

        # Добавляем кнопки в строку markup
        markup.add(minus_button, name_button, plus_button)

    return markup


# добавление товара в корзину
def add_to_cart(client_id, item):
    with open("../bot3/data.json", 'r', encoding="utf-8") as file:
        data = json.load(file)

    clients = data.get("clients", [])

    for client in clients:
        if client.get("id") == str(client_id):
            for cart_item in client["cart"]:
                # print(type(cart_item[0]))
                print(cart_item)
                if cart_item[0] == item['name']:
                    cart_item[1] += 1
                    # cart_item[2] *= cart_item[1]
                    break
            else:
                client["cart"].append([item['name'], 1, int(item['price'].split()[0])])
    # print(data['clients'][1]['cart'])

    with open("../bot3/data.json", 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# удаление товара из корзины
def delete_from_cart(client_id, item):
    with open("../bot3/data.json", 'r', encoding="utf-8") as file:
        data = json.load(file)

    clients = data.get("clients", [])
    for client in clients:
        if client.get("id") == str(client_id):
            for cart_item in client["cart"]:
                if cart_item[0] == item:
                    cart_item[1] -= 1
                    # cart_item[2] *= cart_item[1]
                    # print(cart_item[1])

                    if cart_item[1] == 0:
                        client["cart"].remove(cart_item)

                    break
        # print(data['clients'][1]['cart'])

    with open("../bot3/data.json", 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# обработка данных
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    # print('query_handler')
    bot.answer_callback_query(call.id)
    chat_id = call.message.chat.id

    if call.data.startswith('page_'):
        _, page = call.data.split('_')
        markup = generate_markup(int(page))

        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text="Выберите элемент:",
                              reply_markup=markup)
    elif call.data.startswith('item_'):
        _, item_index = call.data.split('_')
        msg = bot.send_message(call.message.chat.id,
                               f'{menu_items[int(item_index)]["name"]} добавлено',
                               reply_markup=generate_markup())

        bot.delete_message(chat_id, msg.message_id - 1)
        add_to_cart(chat_id, menu_items[int(item_index)])
    # обработка нажатия на '+', преобразование строки в список
    # добавление товара в корзину, обновление корзины и удаление предыдущего сообщения
    elif call.data.startswith('plus_'):
        _, item = call.data.split('_', 1)
        item = ast.literal_eval(item)  # Преобразуем строку в список
        add_to_cart(chat_id, item[0])

        msg = bot.send_message(chat_id, "Корзина:", reply_markup=update_cart(chat_id))
        bot.delete_message(chat_id, msg.message_id - 1)
    # обработка нажатия на '-', преобразование строки в список
    # удаление товара в корзину, обновление корзины и удаление предыдущего сообщения
    elif call.data.startswith('minus_'):
        _, item = call.data.split('_')
        item = ast.literal_eval(item)  # Преобразуем строку в список
        delete_from_cart(chat_id, item[0])

        msg = bot.send_message(chat_id, "Корзина:", reply_markup=update_cart(chat_id))
        bot.delete_message(chat_id, msg.message_id - 1)

    elif call.data.startswith('sum_'):
        _, sum = call.data.split('_')
        # print(type(sum), sum)

        bot.send_message(chat_id, 'Ваш заказ принят! Мы с Вами свяжемся в ближайшее время.')


def handle_selection():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button1 = types.KeyboardButton("Меню 🥩")
    button2 = types.KeyboardButton("Корзина 🛒")
    button3 = types.KeyboardButton("Заказать 🛍️")

    keyboard.add(button1, button2, button3)
    return keyboard


if __name__ == "__main__":
    bot.polling(non_stop=True)
