text = """Вечер
Как тихо веет над долиной
Далекий колокольный звон,
Как шорох стаи журавлиной, —
И в шуме листьев замер он.

Как море вешнее в разливе,
Светлея, не колыхнет день, —
И торопливей, молчаливей
Ложится по долине тень.

dict1 = {}
list_tuple = []

for word in text.split():
    dict1[word] = dict1.get(word, 0) + 1

for key, value in dict1.items():
    list_tuple.append((value, key))


sort_list = sorted(list_tuple, reverse=True)

for item in sort_list[:5]:
    print(item)

# print(list_tuple)
"""
#
#
# def summary_numbers(num1: int, num2: int) -> int:
#     return num1 + num2
#
#
# print(summary_numbers([1, 2], ['3.8', '1.8']))

#
# class Cat:
#
#     def __init__(self, name, color, age):
#         self.name = name
#         self.color = color
#         self.age = age
#
#
# cat1 = Cat("Барсик", "Белый", 3)
# cat2 = Cat("Мурзик", "Чёрный", 7)
# cat3 = Cat("Василий", "Рыжий", 2)
#
# print(cat1.name, cat2.name, cat3.name)
# print(cat1.color, cat2.color, cat3.color)
# print(cat1.age, cat2.age, cat3.age)
#
#
# class Game:
#     def __init__(self):
#         self.money = 10
#         self.coins_per_second = 1
#         self.costs_of_upgrade = {100: False, 1000: False, 5000: False, 10000: False}
#
#     def increase_money(self):
#         for cost, check in self.costs_of_upgrade.items():
#             if not check and self.money >= cost:
#                 self.coins_per_second += 1
#                 self.money -= cost
#                 self.costs_of_upgrade[cost] = True
#                 break
#

# import re
#
# str = '3 товара за 200.99'
# pat = r'\d+.\d'
# match = re.search(pat, str)
#
# print(match.group())

from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def move(self):
        pass
    

class Queen(Piece):
    def move(self):
        print('The queen moves.')


a = Piece()
b = Queen()

a.move(), b.move()
