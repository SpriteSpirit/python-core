# Метод random.shuffle() используется для перемешивания данных списка или другой изменяемой последовательности
# Метод random.sample() используется, когда требуется выбрать несколько элементов из заданной последовательности.
# Метод random.choice() используется, когда вам нужно получить один случайный элемент из последовательности.

"""
gifts = ["berries", "circles", "bunnies"]

gift = random.sample(gifts, 1)[0]

print(f"You win {gift}")


import math

print(math.e)
print(math.pi)
print(math.factorial(15))
print(math.sqrt(256))


def random_gift():
    gifts = ["berries", "circles", "bunnies"]
    count = 2
    gift = random.sample(gifts, count)[random.randint(0, count - 1)]

    return gift


while True:
    input("press ENTER to continue...")
    gift = random_gift()
    print(f"You win {gift}")

# У вас есть функция times_ten(number), которая получает число, умножает его на 10 и выводит в консоль.
# Вызовите эту функцию трижды с аргументами 5, 15, 155.


def times_ten(number):
    print(number * 10)


times_ten(5)
times_ten(15)
times_ten(155)
# Вызовите ту же функцию для 15
# Вызовите ту же функцию для 155


# Напишите три функции:
# get_first_element() — возвращает первый элемент из списка,
# get_last_element() — последний,
# get_list_length() — длину списка.

# Примеры вызова функций:
# get_first_element() вернет "Alpha"
# get_last_element() вернет "Echo"
# get_list_length() вернет 5


letters = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]


def get_first_element(words: data_list) -> str:
    return words[0]


def get_last_element(words: data_list) -> str:
    return words[-1]


def get_list_length(words: data_list) -> int:
    return len(words)


# Не удаляйте код ниже, он нужен для проверки

print(get_first_element(letters))
print(get_last_element(letters))
print(get_list_length(letters))


# Напишите три функции:
# text_length() — вернет количество символов без пробелов,
# text_length_full() — вернет количество символов c пробелами,
# text_word_count() — вернет количество слов (количество пробелов + 1).

# Примеры вызова функций (значения приведены для примера):
# text_length() # Вернет 200
# text_length_full() # Вернет 220
# text_word_count() # Вернет 80

text = "The quick brown fox jumps over the lazy dog"


def text_length(text_words: str) -> int:
    len_without_space = len(text_words.replace(" ", ""))
    return len_without_space


def text_length_full(text_words: str) -> int:
    return len(text_words)


def text_word_count(text_words: str) -> int:
    words = text_words.count(" ") + 1
    return words


# Не удаляйте код ниже, он нужен для вызова и тестирования функции

print(text_length(text))
print(text_length_full(text))
print(text_word_count(text))


# Допишите функцию mymax так, чтобы она возвращала большее число из двух переданных, а не печатала его.
#
# Пример работы функции:
# mymax(10, 100) # Возвращает 100
# mymax(10, 10) # Возвращает 10
# mymax(0, 1) # Возвращает 1


def my_max(first, second):
    if first > second:
        return first
    else:
        return second


# Код ниже нужен для проверки и вызова функции, не удаляйте его!

print(my_max(10, 100))
print(my_max(10, 10))
print(my_max(0, 1))

# Функция get_distance(time, speed) вычисляет расстояние, которое можно пройти за некоторое время. Функция вызывается
# один раз с аргументами (1, 50). Вызовите ее еще 2 раза с указанными в закомментированных строках параметрами.


def get_distance(time, speed):
    distance = time * speed
    print(distance)


get_distance(1, 50)
get_distance(2, 100)
get_distance(3, 10)
# вызовите функцию 2 часа со скоростью 100 километров в час
# вызовите функцию 3 часа со скоростью 10 километров в час


# Напишите функцию has_rrr(word), которая проверяет картавость слова (содержит ли слово маленькие или большие буквы
«Р»), а возвращает булево значение. В качестве аргумента в функцию всегда передается строка. # # Пример ввода: #
has_rrr("Речка") # Вернет True # has_rrr("ручка") # Вернет True # has_rrr("уточка") # Вернет False # has_rrr(
"птичка") # Вернет False # has_rrr("") # Вернет False


def has_rrr(word_for_check: str) -> bool:
    check_r = True if "р" in word_for_check.lower() else False
    return check_r


# Не удаляйте код ниже, он нужен для проверки

word = input("word: ")
result = has_rrr(word)
print(result)


# Напишите функцию get_grade(grade), которая принимает целое число от 2 до 5 и возвращает оценку.
#
# Оценки:
# 2:"Плохо"
# 3:"Удовлетворительно"
# 4:"Хорошо"
# 5:"Отлично"

# Пример ввода:
# 3

# Пример вывода:
# Удовлетворительно

# Пример ввода:
# 4

# Пример вывода:
# Хорошо

grades = {2: "Плохо", 3: "Удовлетворительно", 4: "Хорошо", 5: "Отлично"}


def get_grade(value: int) -> str:
    return grades[value]


# Не удаляйте код ниже, он нужен для вызова функции и проверки

grade = int(input("grade: "))
print(get_grade(grade))


# Напишите функцию get_grade(points), которая принимает количество баллов и возвращает оценку.
#
# Количество баллов — целое число от 0 до 100.
# 0–40 баллов — Плохо
# 41–60 баллов — Удовлетворительно
# 61–80 баллов — Хорошо
# 81–100 баллов — Отлично
# get_grade(35) # Вернет Плохо
# get_grade(45) # Вернет Удовлетворительно
# get_grade(100) # Вернет Отлично


def get_grade(points: int) -> str:
    result = ""

    if 0 <= points <= 40:
        result = "Плохо"
    elif 41 < points <= 60:
        result = "Удовлетворительно"
    elif 61 < points <= 80:
        result = "Хорошо"
    elif 81 < points <= 100:
        result = "Отлично"
    return result


# Не удаляйте код ниже, он нужен для проверки

points = int(input("points: "))
grade = get_grade(points)
print(grade)

# Напишите функцию get_period(hour), которая принимает час и возвращает время суток.
#
# Час — это целое число в диапазоне от 0 до 23.
#
# Если время 0–6 — ночь
# Если время 7–11 — утро
# Если время 12–17 — день
# Если время 18–23 — вечер

# Примеры вызова:
# get_period(8) # Вернет "утро"
# get_period(17) # Вернет "день"
# get_period(0) # Вернет "ночь"


def get_period(hour: int) -> str:
    result = ""
    if 0 <= hour <= 6:
        result = "ночь"
    elif 7 < hour <= 11:
        result = "утро"
    elif 12 < hour <= 17:
        result = "день"
    elif 18 < hour <= 23:
        result = "вечер"
    return result


# Не удаляйте код ниже, он нужен для проверки

time_of_day = get_period(int(input("hour: ")))
print(time_of_day)


# Напишите функцию avg(items), которая принимает список и вычисляет среднее арифметическое элементов.
#
# Среднее арифметическое — это сумма всех числел (sum), разделенная на их количество (len).
#
# Пример:
# avg([1,2,3]) # Вернет 2.0
# avg([5,5,5,5]) # Вернет 5.0
# avg([2,8]) # Вернет 5.0


def avg(all_items: data_list) -> float:
    return sum(all_items) / len(all_items)


# Не удаляйте код ниже, он нужен для проверки

items = [int(x) for x in input().split(" ")]
items_avg = avg(items)
print(items_avg)


# Напишите функцию get_rur_kop(value), которая получает сумму в копейках, а возвращает количество полных рублей.
# В качестве value всегда передается целое число.
#
# Подсказка: деление нацело — x // y
# get_rur_kop(100) # Возвращает 1
# get_rur_kop(755) # Возвращает 7
# get_rur_kop(1234) # Возвращает 12
# get_rur_kop(99) # Возвращает 0


def get_rur_kop(value):
    return value // 100


# Не удаляйте код ниже, он нужен для проверки

value = int(input("value: "))
result = get_rur_kop(value)
print(result)


# Напишите функцию get_min_sec(sec), которая принимает время в секундах, возвращает словарь в формате:
#
# {"min": мин, "sec": сек}
# Минуты и секунды — целые числа.
#
# Подсказка: деление нацело — x//y , остаток от деления — x%y
#
# get_min_sec(120) # Вернет {"min": 2, "sec": 0}
# get_min_sec(150) # Вернет {"min": 2, "sec": 30}
# get_min_sec(15) # Вернет {"min": 0, "sec": 15}


def get_min_sec(sec):
    minutes = sec // 60
    seconds = sec % 60

    return f"{{'min': {minutes}, 'sec': {seconds}}}"


value = int(input())
result = get_min_sec(value)
print(result)


# Допишите функцию, которая получает два числа и возвращает количество процентов, которое составляет первое от второго.
# Значение возвращается в виде строки со знаком процента. Результат округляется до целого числа.
#
# get_percent_rounded(10, 10) # Вернет "100%"
# get_percent_rounded(5, 15) # Вернет "33%"
# get_percent_rounded(0, 5)  # Вернет "0%"


def get_percent_rounded(num1: int, num2: int) -> str:
    percent = round((num1 * 100) / num2)
    return f"{percent}%"


# Не удаляйте код ниже, он нужен для проверки

a = int(input("a: "))
b = int(input("b: "))
print(get_percent_rounded(a, b))

# У вас есть текст, в котором встречаются #хештеги. Напишите функцию get_hash(text). Верните все хештеги одним списком.
#
# get_hashtags("Котята #еда #закат море") # Вернет список ['еда', 'закат']
# get_hashtags("#код #функция #решение") # Вернет ['код', 'функция', 'решение']
# get_hashtags("Котята") # Вернет []


def get_hashtags(text: str) -> data_list:

    words = text.split(" ")
    hashtags = []
    for word in words:
        if "#" in word:
            hashtags.append(word[1:])
    return hashtags


# Не удаляйте код ниже, он нужен для проверки

words = input("words: ")
result = get_hashtags(words)
print(result)



# Напишите функцию, которая возвращает площадь круга, принимая его радиус.
#
# Формула вычисления площади:
# радиус ** 2 * Пи.
# Пи в этом задании можно считать равным 3.14.
# get_square(1) # Вернет 3.14
# get_square(2) # Вернет 12.56
# get_square(3) # Вернет 28.26


def get_square(radius: float) -> float:
    return round(radius**2 * 3.14, 2)


# Не удаляйте код ниже, он нужен для проверки

radius = int(input("radius: "))
square = get_square(radius)
print(square)


# Напишите функцию get_longest(words), которая получает список строк и возвращает самое длинное слово из списка.
# Список может быть пустым, но все элементы из списка — строки.
#
# get_longest(["еж" , "мышь", "стриж"]) # Вернет "стриж"
# get_longest(["aaa", "aa", "a"]) # Вернет "aaa"
# get_longest(["——-", "—-", "-"]) # Вернет "——-"
# get_longest(["a", "a", "a"]) # Вернет "a"


def get_longest(words: data_list) -> str:
    max_word = max(words, key=len)
    return max_word


# Не удаляйте код ниже, он нужен для проверки

words = input().split(" ")
result = get_longest(words)
print(result)


# Напишите функцию get_discount(summ), которая возвращает уровень скидки или бонусной карты в зависимости от суммы покупок.
#
# Уровень — это целое число!
#
# Правила вычисления уровня:
# до 5000 вернет 1
# до 10000 вернет 2
# до 20000 вернет 3
# до 35000 вернет 4
# до 50000 вернет 5
# от 50000 и выше вернет 6

# Примеры вызова функции:
# get_discount(2000) # Вернет 1
# get_discount(7500) # Вернет 2
# get_discount(45000) # Вернет 5
# get_discount(75000) # Вернет 6


def get_discount(summ: int) -> int:
    discount_levels = {
        5_000: 1,
        10_000: 2,
        20_000: 3,
        35_000: 4,
        50_000: 5,
    }
    hight_level: int = 6

    for amount, discount in discount_levels.items():
        if summ < amount:
            return discount

    return hight_level


# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_discount(value)
print(result)
"""
the_int = 0
the_float = 0.0
the_str = "-"
the_bool = False
the_list = [0]
the_dict = {0: 0}


def the_change():
    the_int = 1
    the_float = 1.0
    the_str = "+"
    the_bool = True
    the_list.append(1)
    the_dict[1] = 1


the_change()

print(the_int)
print(the_float)
print(the_str)
print(the_bool)
print(the_list)
print(the_dict)
