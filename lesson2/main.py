"""# Создайте список из семи элементов с цветами радуги: red, orange, yellow, green, blue, indigo, violet.

colors  = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Не удаляйте код ниже, он нужен для проверки
for color in colors:
  print(color)

# Создайте список дней недели на русском языке.
# Названия дней недели запишите с большой буквы.

weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for day in weekdays:
  print(day)

# Создайте список номиналов монет и банкнот в рублях начиная от 1 рубля.
# Храните числа, а не строки.
# Информацию о монетах и банкнотах в рублях смотрите на сайте: https://www.banki.ru

numbers = [1, 2, 5, 10, 50, 100, 200, 500, 1_000, 2_000, 5_000]

# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for number in numbers:
  print(number)

# У вас есть список фруктов. Напишите код, который выведет грушу.
fruits = ["яблоко", "груша", "ананас", "апельсин", "виноград"]

element = fruits[1]

print(element)

# У вас есть прогноз погоды на 3 дня с температурой и описанием погоды.
# Выведите прогноз на 3 дня в формате:
# Понедельник +10 ясно
# Вторник +13 дождь
# Среда +9 град

temp = ["+10", "+8", "+7"]
weather = ["ясно", "дождь", "град"]
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

for i in range(3):
    print(weekdays[i], temp[i], weather[i])


# У вас есть список вещей, которые можно взять на необитаемый остров. Со стандартного ввода подаются два индекса. Выведите две вещи на соответствующих позициях.
# Позиции нумеруются с нуля.
# Пример вывода:
# палатка
# зефирки

items = ["палатка", "спички", "одеяло", "нож", "зефирки", "крючок", "консервы"]

index_1 = int(input("index 1: "))
index_2 = int(input("index 2: "))

print(f"{items[index_1]}\n{items[index_2]}")

# У вас есть три списка. Выведите длину каждого.
list_1 = ["apple", "banana", "blueberry", "strawberry", "melon"]
list_2 = ["blue", "orange", "blue", "blue", "yellow"]
list_3 = [True, False, True, True, False, True]

list_1_len = len(list_1)
list_2_len = len(list_2)
list_3_len = len(list_3)

print(list_1_len, list_2_len, list_3_len)

# У нас есть список fruits. Выведите принтом количество элементов в нем.
# Пример вывода:
# В списке элементов: 5

fruits = ["banana", "orange", "apple"]

print(f"В списке элементов: {len(fruits)}")

# Добавьте в список фруктов лимон, банан и киви.
fruits = ["яблоко", "груша"]
fruits.extend(["лимон", "банан", "киви"])
# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for fruit in fruits:
  print(fruit)

# У вас есть список букв. Со стандартного ввода подаются три символа. Добавьте их в конец списка с помощью метода extend.
symbols = ["m", "o", "n"]

symbol_1 = input("char 1: ")
symbol_2 = input("char 2: ")
symbol_3 = input("char 3: ")

symbols.extend([symbol_1, symbol_2, symbol_3])

# Не удаляйте код ниже, он нужен для проверки
print("".join(symbols))

# У вас есть список с числительными на языке, близком к русскому.
# Замените часть слов так, чтобы получились корректные числительные женского рода — одна, две, три и т. д.

numbers = ["нула", "една", "две", "три", "четири", "пет", "шест"]
changed = ["ноль", "одна", "две", "три", "четыре", "пять", "шесть"]

for i in range(len(numbers)):
    numbers[i] = changed[i]
# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for number in numbers:
  print(number)

# У вас есть список дежурств на неделю. В списке дежурств нужно заменить Дениса на Татьяну.
managers = ["Алексей", "Денис", "Юля", "Руслан",  "Алексей", "Денис", "Юля"]

for manager in managers:
    if manager == "Денис":
        manager = "Татьяна"
    print(manager)

# Со стандартного ввода подается номер месяца.
# Выведите правильное название месяца на основе имеющегося списка.
# Обратите внимание: позиции элементов списка начинаются с 0, а номера месяцев, которые вводит пользователь, начинаются с 1, поэтому полученное от пользователя число нужно будет уменьшить.
# Пример ввода:
# 2
# Пример вывода:
# февраль

months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
months_id = int(input("month: "))

print(months[months_id-1])
# У вас есть список дней недели на иностранном языке. Создайте новый список, в котором будут только будние дни.
weekdays = [
"pirmdiena",
"otrdiena",
"trešdiena",
"ceturtdiena",
"piektdiena",
"sestdiena",
"svētdiena"]

workdays = weekdays[:-2]

# Не удаляйте код ниже, он нужен для проверки

for workday in workdays:
  print(workday)

# У вас есть список временных интервалов:
# timespans = ["7-8", "8-9", "9-10", "10-11", "11-12", "12-13" ]
# Со стандартного ввода вы получаете число N.
# Верните первые N интервалов, выведите их.
# Пример вывода:
# ["7-8", "8-9", "9-10"]

timespans = ["7-8", "8-9", "9-10", "10-11", "11-12", "12-13" ]
n = int(input("n: "))

print(timespans[:n])

# У вас есть список букв алфавита, который заканчивается символом "–".
# Со стандартного ввода подается номер позиции буквы.
# Верните букву и следующую за ней.
# А — это буква с номером 0.

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g',
  'h', 'i', 'j', 'k', 'l', 'm', 'n',
  'o', 'p', 'q', 'r', 's', 't', 'u',
  'v', 'w', 'x', 'y', 'z', '-'
]

position = int(input("position: "))
print(alphabet[position:position+2])

# У вас есть список букв алфавита.
# Со стандартного ввода подается число num, не равное 0.
# Выведите последние num элементов.

alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g',
  'h', 'i', 'j', 'k', 'l', 'm', 'n',
  'o', 'p', 'q', 'r', 's', 't', 'u',
  'v', 'w', 'x', 'y', 'z'
]

num = int(input("num: "))
if num != 0:
    sliced = alphabet[-num:]
else:
    print("Input more than 0")
print(sliced)

# У вас есть два списка букв. Со стандартного ввода подается число count.
# Возьмите первые count букв из второго списка и добавьте к первому, используя метод extend.
letters_1 = ["A", "B", "C", "D"]
letters_2 = ["E", "F", "G", "K", "L", "M", "N"]

count = int(input("count: "))

letters_1.extend(letters_2[:count])

# Не удаляйте код ниже, он нужен для проверки

print("".join(letters_1))

# У вас есть список покупок. Со стандартного ввода подаются три продукта.
# С помощью метода remove удалите их из списка, затем выведите остальные продукты.
#
# Пример ввода:
# Хлопья
# Молоко
# Яблоки
#
# Пример вывода:
# ["Печенье", "Шоколад"]

shopping_list = ["Молоко", "Печенье", "Хлопья", "Шоколад", "Яблоки"]

item_to_remove_1 = input("product 1: ")
item_to_remove_2 = input("product 2: ")
item_to_remove_3 = input("product 3: ")

remove_items = [item_to_remove_1, item_to_remove_2, item_to_remove_3]

for i in range(len(remove_items)):
    if remove_items[i] in shopping_list:
        shopping_list.remove(remove_items[i])

print(shopping_list)

# Используя метод remove, удалите красные элементы из списка.
# Обратите внимание: по умолчанию метод remove удаляет один элемент за раз.

colors = ["красный", "оранжевый", "красный", "синий", "красный", "черный"]

for i in range(len(colors)):
    if "красный" in colors:
        colors.remove("красный")
# Не удаляйте код ниже и не редактируйте его, он нужен для проверки

for color in colors:
  print(color)

# У вас есть список лекарств. Со стандартного ввода подаются два индекса. Нумерация в передаваемых индексах начинается с нуля.
# Удалите с помощью оператора del соответствующие лекарства. Выведите оставшиеся лекарства.
# Обратите внимание, после удаления нумерация элемента может поменяться.

medications = ["Пепамицин", "Дилитарил", "Флоутолар", "Россум-лайт"]

index_to_remove_1 = int(input("remove medication: "))
index_to_remove_2 = int(input("remove medication: "))

if 0 <= index_to_remove_1 < len(medications):
    del medications[index_to_remove_1]
if 0 <= index_to_remove_2 < len(medications):
    del medications[index_to_remove_2]

print(medications)

# Используя del, удалите красный элемент из списка.
colors = ["красный", "оранжевый", "синий", "черный"]

for i in range(len(colors) - 1): # 0 1 2 3
    if colors[i] == "красный":
        del colors[i]
# Не удаляйте код ниже и не редактируйте его, он нужен для проверки
for color in colors:
    print(color)

# У вас есть список имен. Удалите первый и последний элементы с помощью метода pop.
# Выведите удаленные элементы.
#
# Пример вывода:
# Алиса
# Георгий
# Остались: ['Борис', 'Василий', 'Диана']

guests = ["Алиса", "Борис", "Василий", "Диана", "Георгий"]

print(f"{guests.pop(0)}\n{guests.pop()}")
# Это код, который помогает проверить задание, не удаляйте его
print("Остались:", guests)

# Список полезных продуктов хранится в good_food.
# Со стандартного ввода подается название продукта.
# Если продукт в списке полезной еды, выведите «Это полезно».
# Если его там нет, выведите «Возможно, это вредно».

good_food = ["яблоко", "сельдерей", "брокколи"]

questionable = input("food: ")

if questionable in good_food:
    print("Это полезно")
else:
    print("Возможно, это вредно")

# Перечень дней месяца, когда Денис занимался программированием, хранится в списке.
# Со стандартного ввода подается число. Если в этот день Денис занимался, выведите «Это был полезный день». Иначе — «Это был бесполезный день».
active_days = [1, 5, 6, 8, 10, 12, 15, 19, 22, 27, 30]

current_day = int(input("day: "))

if current_day in active_days:
    print("Это был полезный день")
else:
    print("Это был бесполезный  день")

ice_cream = ["Choco", "Cream", "Starwsberry", "Vanilla"]
# добавление элементов в начало списка
ice_cream[:0] = ["Buble Gum", "Ice"]
print(ice_cream)

ice_cream = ["Choco", "Cream", "Vanilla"]
# вставка элементов
ice_cream.insert(0,  "Starwsberry")
ice_cream.insert(-1, ["Buble Gum", "Ice"])
print(ice_cream)

ice_cream = ["Choco", "Cream", "Vanilla"]
# поиск индекса
print(ice_cream.index("Vanilla", 0))

ice_cream = ["Choco", "vanilla", "cream"]
# сортировка списка по регистру
# мы вызываем ice_cream.sort(key=str.lower), список ice_cream будет отсортирован по алфавиту, причем регистр символов будет игнорироваться.
ice_cream.sort(key=str.lower)
print(ice_cream)

ice_cream = ["Choco", "vanilla", "cream"]
# sorted() возвращает новый отсортированный список
new_ice_cream = sorted(ice_cream)
print(f"new: {new_ice_cream}\nold: {ice_cream}")
"""

# удаление элементов списка
colors = ["Pink", "Yellow", "Red", "Blue", "Green", "White"]
# оператор del
del colors[-1]
print(f"Colors after [del] [White color]: {colors}")
# метод remove()
colors.remove("Blue")
print(f"Colors after [remove] [Blue color]: {colors}")
# метод pop()
print(f"Colors after [pop] {colors.pop()}: {colors}")

# копия списка
copy_colors = colors.copy()
print(f"Copy colors after used [copy()]: {colors} & {copy_colors}")

# генерация списка
new_numbers = [num**2 for num in range(2, 10, 2)] # квадрат чисел
print(new_numbers)
