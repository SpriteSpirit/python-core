"""f = open('mydata.txt', 'a', encoding="utf-8")
f.write("\nТеперь тут новые данные!")
f.close()
"""

filename = "user_data.txt"
data_list = []
f = open(filename, "r", encoding="utf-8")

for user_data in f.readlines():
    data_list += user_data.strip().split()

name, surname, email, phone = data_list

print(f"{name} {surname} – это вы. Ваша почта {email}, ваш телефон {phone}")
