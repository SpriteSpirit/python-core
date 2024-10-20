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


@bot.message_handler(commands=["add_info"])
def handle_add_info(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    msg = bot.send_message(chat_id, "Введите имя: ")
    bot.register_next_step_handler(msg, get_user_name)


def get_user_name(message):
    chat_id = message.chat.id
    user_data[chat_id]["name"] = message.text
    msg = bot.send_message(chat_id, "Ваше имя сохранено. Теперь введите ваш номер телефона: ")
    bot.register_next_step_handler(msg, callback=get_user_phone)


def get_user_phone(message):
    chat_id = message.chat.id
    user_data[chat_id]["phone"] = message.text
    add_client(message, user_data[chat_id]["name"], user_data[chat_id]["phone"])
    bot.send_message(chat_id,
                     f"Ваше имя {user_data[chat_id]['name']} сохранено. Ваш номер телефона {user_data[chat_id]['phone']} сохранён ")


def add_client(message, client_name, client_phone):
    try:
        # открытие файл и чтения
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"clients": []}
        print("Файл не найден")

    # добавление новой записи в "clients"
    new_client = {"id": str(message.chat.id), "name": client_name, "phone": client_phone, "cart": []}

    for client in data["clients"]:
        if client.get("id") == str(message.chat.id):
            client["name"] = client_name
            client["phone"] = client_phone
            break
    else:
        data["clients"].append(new_client)

    # сохранения в файл json новые записи
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def handle_selection():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button1 = types.KeyboardButton("Меню 🥩")
    button2 = types.KeyboardButton("Корзина 🛒")
    button3 = types.KeyboardButton("Заказать 👛")

    keyboard.add(button1, button2, button3)
    return keyboard


dishes = [
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


def generate_menu(page=0):  # начинаем с 0 страницы

    start_index = page * ITEMS_PER_PAGE
    end_index = start_index + ITEMS_PER_PAGE

    keyboard = types.InlineKeyboardMarkup()

    for dish in dishes[start_index:end_index]:  # от 0 до 4
        button = types.InlineKeyboardButton(text=f"{dish['name']}: {dish['price']}",
                                            callback_data=f"dish_{dishes.index(dish)}")
        keyboard.add(button)

    # РАЗОБРАТЬСЯ ЗДЕСЬ
    if page > 0:
        keyboard.add(types.InlineKeyboardButton(text="<<", callback_data=f"page_{page - 1}"))
    if end_index < len(dishes):
        keyboard.add(types.InlineKeyboardButton(text=">>", callback_data=f"page_{page + 1}"))

    return keyboard


def generate_cart(client_id):
    items_cart = get_cart(client_id)  # словарь
    keyboard = types.InlineKeyboardMarkup()
    # print(items_cart)

    for item in items_cart:
        minus_button = types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}")
        plus_button = types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}")
        name_button = types.InlineKeyboardButton(text=f"{item[0]} x {item[1]}", callback_data=f"name_{item}")

        keyboard.add(minus_button, name_button, plus_button)

    bot.send_message(client_id, "Корзина", reply_markup=keyboard)


def get_cart(client_id):
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    clients = data.get("clients", [])
    for client in clients:
        if client.get("id") == str(client_id):
            return client.get("cart", [])
    return None


# ПРОВЕРИТЬ
def add_to_cart(client_id, item):
    with open("data.json", "r", encoding="utf-8") as file:
        cart = json.load(file)

    clients = cart.get("clients", [])

    for client in clients:
        if client.get("id") == str(client_id):
            for cart_item in client["cart"]:
                if cart_item[0] == item['name']:
                    cart_item[1] += 1
                    break
            else:
                client["cart"].append([item['name'], 1])

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(cart, file, ensure_ascii=False, indent=4)


# ПРОВЕРИТЬ
def delete_to_cart(client_id, item):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    clients = data.get("clients", [])

    for client in clients:
        if client.get("id") == str(client_id):
            for cart_item in client["cart"]:
                if cart_item[0] == item['name']:
                    if cart_item[1] > 0:
                        cart_item[1] -= 1
                        print(f"Позиция '{cart_item}' уменьшена на один")
                        if cart_item[1] == 0:
                            client["cart"].remove(cart_item)
                            print(f"Позиция '{cart_item}' удалена из корзины")

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# РАЗОБРАТЬСЯ ЗДЕСЬ
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    chat_id = call.message.chat.id

    if call.data.startswith("page_"):
        text, page = call.data.split("_")
        print(text, page)
        keyboard = generate_menu(int(page))
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=call.message.message_id,
            text="Основное меню:",
            reply_markup=keyboard)

    elif call.data.startswith("dish_"):
        text, dish_index = call.data.split("_")
        bot.send_message(chat_id, text=f"Блюдо {dishes[int(dish_index)]['name']} добавлено в заказ",
                         reply_markup=generate_menu())
        add_to_cart(chat_id, dishes[int(dish_index)])

    elif call.data.startswith("plus_"):
        text, item = call.data.split("_")
        item = item.replace("'", '')
        item_list = item[1:-1].split(",")

        for dish in dishes:
            if dish['name'] == item_list[0]:
                add_to_cart(chat_id, dish)
                bot.send_message(chat_id, text=f"Блюдо {dish['name']} добавлен в заказ...",
                                 reply_markup=generate_cart(chat_id))

    elif call.data.startswith("minus_"):
        text, item = call.data.split("_")
        item = item.replace("'", '')
        item_list = item[1:-1].split(",")

        for dish in dishes:
            # print(dish)
            if dish['name'] == item_list[0]:
                delete_to_cart(chat_id, dish)
                bot.send_message(chat_id, text=f"Блюдо {dish['name']} убрано из заказа...",
                                 reply_markup=generate_cart(chat_id))


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    if message.text == "Меню 🥩":
        bot.send_message(message.chat.id, "Основное меню: ", reply_markup=generate_menu())
    elif message.text == "Корзина 🛒":
        generate_cart(message.chat.id)
    elif message.text == "Заказать 👛":
        bot.send_message(message.chat.id, "/ ")


if __name__ == "__main__":
    bot.polling(non_stop=True)