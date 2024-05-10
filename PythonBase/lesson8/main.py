'''from pin import check_pin

print("Введите ваш ПИН-код")
user_input = input()

if check_pin(user_input):
    print("Такой ПИН-код подходит")
else:
    print("Такой ПИН-код НЕ подходит")'''

from datetime import datetime as dt

now = dt.now()
now_date = dt.now().date()
my_date = dt(2024, 5, 24, 14, 5, 7)
now_time = dt.now().time()

print(f"Now date: {now_date}")
print(f"Now time: {now_time}")
print(f"My date: {my_date}")

print("Год", now.year)
print("Месяц", now.month)
print("День", now.day)
print("Час", now.hour)
print("Минута", now.minute)
print("Секунда", now.second)

thedate = dt.fromisoformat("2021-05-04")

print(thedate.year)
print(thedate.month)
print(thedate.day)

thetime = dt.strptime("23:14", "%H:%M")

print(thetime.hour)
print(thetime.minute)

thedate = dt.fromisoformat("2020-12-06 23:14")

print(thedate.year)
print(thedate.month)
print(thedate.day)

print(thedate.hour)
print(thedate.minute)

date_formatted = thedate.strftime("%d %B %Y ")  # День Месяц Год

print(date_formatted)


