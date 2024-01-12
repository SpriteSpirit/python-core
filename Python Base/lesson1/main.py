"""print(round(4.5555,0))
print("Введите в терминале \"да\" или \"нет\" ")

title = "Book"
price = 1200
discount = 11
sales = 241

if sales > 150:
    title += "[Popular!]"

if discount > 0:
    title += "[Sale!]"

if discount > 10:
    title += "[Action!]"

print(title)

monday = input() == "True"
tuesday = input() == "True"
wednesday = input() == "True"
thursday = input() == "True"
friday = input() == "True"
saturday = input() == "True"
sunday = input() == "True"

# Начните писать код здесь

if monday:
    print("Понедельник")

if thursday:
    print("Четверг")

if friday:
    print("Пятница")

word = input("word: ")

has_r = "r" in word
has_l = "l" in word
has_s = "s" in word

print("Слово", word)

if has_r:
    print("Есть буква R")
if has_l:
    print("Есть буква L")
if has_s:
    print("Есть буква S")



messages_count = int(input("mes_count: "))

if messages_count > 0:
    print("Есть новые сообщения")


word1 = input("word1: ")
word2 = input("word2: ")

counter = 0

if "р" in word1:
  counter += 1

if "р" in word2:
  counter += 1


print(counter)

residency = int(input("residency: "))
salary = int(input("salary: "))
experience = int(input("experience: "))


counter = 0


if residency >= 2:
    counter += 1
if salary >= 50_000:
    counter += 1
if experience >= 2:
    counter += 1

print(f"Ваш кредитный рейтинг - {counter}")

luggage_weight = int(input("luggage_weight: "))

if luggage_weight <= 5:
    print("Можно взять в салон")
else:
    print("Нужно сдать в багаж")

# Получаем данные от пользователя
user_input = input("word: ")

# Проверяем первый вариант
if user_input == "bird":
    print("это птица")

# Проверяем второй вариант
if user_input == "plane":
    print("это самолет")

our_speed = int(input("speed: "))
max_speed = int(input("max speed: "))

if our_speed <= max_speed:
    print(True)
else:
    print(False)

first_number = int(input("1: "))
second_number = int(input("2: "))

if first_number == second_number:
    print(True)
else:
    print(False)

number = int(input("number: "))

if number % 10 == 1:
    print(True)
else:
    print(False)
filename = input("filename: ")

if ".gif" in filename:
    print(True)
else:
    print(False)

balance = int(input("balance: "))
course_price = int(input("price: "))

if balance >= course_price:
    print(True)
else:
    print(False)

while True:
    python_count = int(input("How much pythons?\n"))
    morphy = ""
    if 11 <= python_count <= 20:
        morphy = "питонов"
        print(python_count, morphy)
    elif python_count % 10 == 1:
        morphy = "питон"
        print(python_count, morphy)
    elif 2 <= python_count % 10 <= 4:
        morphy = "питона"
        print(python_count, morphy)
    else:
        morphy = "питонов"
        print(python_count, morphy)
    if python_count == -1:
        break



deposit = int(input("deposit: "))

if deposit >= 500:
    print("Средств достаточно")
else:
    print("Средств недостаточно")

avg_temp = int(input("temp: "))

if avg_temp <= 8:
    print("Пора включать отопление")
else:
    print("Померзни еще")

humidity = int(input("Humidity: "))

if 40 <= humidity <= 60:
    print("Влажность комфортная")
else:
    print("Обратите внимание на влажность")

temp = float(input("temp: "))

if temp <= 36.5:
    print("Температура понижена")
elif 36.5 <= temp <= 36.7:
    print("Температура в норме")
else:
    print("Температура повышена")

number = int(input("number: "))

if number == 0:
    print("ноль")
elif number == 1:
    print("один")
elif number == 2:
    print("два")
elif number == 3:
    print("три")
elif number == 4:
    print("четыре")

#Введите оценку звездочками ***
stars = input("stars: ")
count_star = "*"

if stars == count_star:
    print("Ужасно")
elif stars == count_star * 2:
    print("Очень плохо")
elif stars == count_star * 3:
    print("Средненько")
elif stars == count_star * 4:
    print("Всё в порядке")
elif stars == count_star * 5:
    print("Прекрасная поездка!")

age = int(input("age: "))

if 7 > age or age > 60:
    print("бесплатно")
elif 7 <= age <= 17:
    print("100 рублей")
elif 18 <= age <= 24:
    print("200 рублей")
elif 25 <= age <= 60:
    print("300 рублей")

water_delivered = int(input("water_delivered: "))
norm = 20_000

if norm <= water_delivered <= norm + (norm * 0.5):
    bonus_percent = 10
elif water_delivered >= norm + (norm * 0.5):
    bonus_percent = 20
else:
    bonus_percent = 0

print(f"Бонус = {bonus_percent}%")


space_total = 110
space_os = 30
space_docs = 22
space_free = space_total - (space_os + space_docs)

print(space_free)

megabytes_count = 6
kilobytes_in_megabyte = 1024

result = kilobytes_in_megabyte * megabytes_count

print(result)

number = int(input("number: "))

number_exp_2 = number ** 2
number_exp_3 = number ** 3
number_exp_4 = number ** 4

print(number_exp_2)
print(number_exp_3)
print(number_exp_4)

summ = int(input("summ: "))

# Половина
half = summ/2
# Четверть
quarter = summ/4
# Десятая часть
decimal = summ/10

print("Половина", half)
print("Четверть", quarter)
print("Десятая", decimal)

number_1 = int(input("num1: "))
number_2 = int(input("num2: "))
number_3 = int(input("num3: "))

min_of = min(number_1, number_2, number_3)
max_of = max(number_1, number_2, number_3)
avg_of = sum((number_1, number_2, number_3)) / 3

print(f"Минимум: {min_of}")
print(f"Максимум: {max_of}")
print(f"Среднее: {avg_of}")

income = int(input("income: "))

necessity_jar = round(income * 0.55) # Текущие расходы
financial_freedom_jar = round(income * 0.1)  # Финансовая свобода
education_jar = round(income * 0.1)  # Образование
savings_jar = round(income * 0.1) # Резервный фонд
play_jar = round(income * 0.1) # Развлечения
give_jar =  round(income * 0.05) # Благотворительность и подарки

print(f"Текущие расходы {necessity_jar}")
print(f"Финансовая свобода {financial_freedom_jar}")
print(f"Образование {education_jar}")
print(f"Резервный фонд {savings_jar}")
print(f"Развлечения {play_jar}")
print(f"Благотворительность и подарки {give_jar}")

students_count = int(input("students_count: "))
students_online = int(input("students_online: "))

online_percent = round(students_online * 100 / students_count)

print(f"На встречу пришло {online_percent} процентов")

number = int(input("number: "))

if number % 3 == 0  :
	print("Число делится на 3")
else:
	print("Число НЕ делится на 3")

number_of_students = int(input("number_of_students: "))

number_of_groups = number_of_students//4

print(f"Получится {number_of_groups} полных групп")

# 4 строки ниже записывают булевые переменные, не меняйте их

has_education = input() == "True"
has_portfolio = input() == "True"
has_experience = input() == "True"
has_device = input() == "True"

result = int(has_education) + int(has_portfolio) + int(has_experience) + int(has_device)

print(result)
is_dark = bool(int(input("is_dark: ")))
is_experience_less_1y = bool(int(input("is_experience_less_1y: ")))
is_raining = bool(int(input("is_raining: ")))
is_driver_tired = bool(int(input("is_driver_tired: ")))

max_speed = 90

speed = max_speed - is_dark * 20 - is_experience_less_1y * 10 - is_raining * 10 - is_driver_tired * 10

print(speed)

score = int(input("score: "))
age = int(input("age: "))

if score >= 20 and age >= 18:
    print("Вот ваши права")
else:
    print("Мы не можем выдать вам права")

day = int(input("day: "))
month = int(input("month: "))

if 1 <= day <= 30 and 1 <= month <= 12:
    print("Корректная дата")
else:
    print("Некорректная дата")

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x <= y <= z < 50 :
    print("Размер ОК")
else:
    print("Размер ПРЕВЫШЕН")


x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x > 100 or y > 100 or z > 100 :
    print("Размер ПРЕВЫШЕН")
else:
    print("Размер ОК")"""

hour = int(input("hour: "))

if 7 <= hour < 11 or 18 <= hour < 23:
    print("Прием открыт")
else:
    print("Прием закрыт")