'''hello = "ONE****TWO****THREE"

hello_list = hello.split('----')

print(hello_list)


from random import randint


class Dice:
    def __init__(self, faces):
        self.faces = faces
        self.history = []

    def dice_throw(self):
        res = randint(1, self.faces)
        self.history.append(res)
        return res

    def get_history(self, x):
        return self.history[-x:]


dice = Dice(4)
print(dice.dice_throw())
print(dice.dice_throw())
print(dice.dice_throw())
print(dice.dice_throw())
print(dice.get_history(2))

a = float(input("A: "))
b = (a * 10) // 1 % 10 % 10


print(b)


def multiply_range(start, end):
    result = 1

    if start > end:
        start, end = end, start

    for num in range(start, end + 1):
        result *= num

    return result


print(multiply_range(5, 10))


# пример функционального программирования
def progression(start, stop, step):
    if start > stop:
        start, stop = stop, start

    if start < stop:
        print(start)
        progression(start + step, stop, step)
    else:
        return


progression(0, 10, 1)
import turtle as t
from random import randint, choice


def go_snowy(length):

    t.speed(100)
    if length < 5:
       t.forward(length)
    else:
        go_snowy(length/3)
        t.left(60)
        go_snowy(length/3)
        t.right(120)
        go_snowy(length/3)
        t.left(60)
        go_snowy(length / 3)


for i in range(100):
    t.up()
    t.goto(randint(-400, 400), randint(-400, 400))
    t.down()

    for j in range(3):
        colors = ['green', 'yellow', 'pink', 'red', 'purple', 'black', 'olive', 'blue']
        t.color(choice(colors))
        go_snowy(50)
        t.right(120)

t.mainloop()



def double_performer(func, x):
    return func(func(x)) # (5*10)*10


def f(x): return x * 10


def f2(x): return x * x


def f3(x): return -x


# print(double_performer(f, 5))

f1 = f

for f in f1, f2, f3:
    print(double_performer(f, 5))

def f(x): return x * 10


A = (1, 2, 3, 4, 5)
C = map(f, A)

for y in C:
    print(y)


A = range(10)
B = (x for x in A if x % 2 == 0)
print(*B) # развертка
print(*(x * x for x in A if x % 2 == 1))
print(*map(lambda x: x*x, A))'''
import json
from pprint import pprint
from typing import List

import pygame

clock = pygame.time.Clock()


#
# A = (1, 2, 3, 4, 5)
# B = tuple(x * 10 for x in A)
#
# print(B)
# C = zip(A, B)
#
# # for i in C:
# #     print(i)
#
# i = iter(C)
# next(i)
#
#
# for i in C:
#     a, b = i
#     print(a, b, i[0] + i[1])


# print(*map(lambda i: i[0] * i[1], enumerate('Hello'))) # e ll lll oooo

# def arithm_progression(start, stop, step):
#     x = start
#     while x < stop:
#         print(f'now working on x = {x}')
#         yield x
#         x += step
#
#
# A = arithm_progression(1, 10, 2)
#
# for x in A:
#     print(x)

# numpy, itertools

# from itertools import starmap
#
# print(*starmap(lambda i, char: char * i, enumerate('Hello'))) # e ll lll oooo

# from functools import reduce
#
# A = (1, 2, 3, 4, 5, 6)
# print(reduce(lambda x, y: x + y, A))
#
# size = (600, 500) #размеры окна
# screen = pygame.display.set_mode(size) #создание окна
#
#
# while True:
#     my_rect = pygame.Rect(0, 0, 100, 100)
#     pygame.draw.rect(screen, 'red', my_rect)
#     # my_rect.centerx = (size[0] // 2)
#     my_rect.midtop = (size[0] // 2, 0)
#
#     pygame.display.update()#обновление экрана
#     clock.tick(15) # метод, ограничивающий FPS.

#
# with open("test.json", encoding='utf-8') as file:
#     data = json.load(file)
#
# # pprint(data)
# print(data["accounts"][-1]['name'])

#
# def get_sum(num1, num2, num3):
#     result = num1 + num2 + num3
#     return result
#
#
# print(get_sum(5, 5, 5))
#


# number = 5
# line = '5'

# print(type(number))
# print(type(line))

# print(dir(line))

# help(str.join)

#
# class Cat:
#     name = 'Barsik'
#     age = 5
#     color = "Red"
#
#     def speak(self):
#         print('Meow!')
#
#     def play(self):
#         print('Meow! Я играю')
#
# cat1 = Cat()
#
# print(cat1.color)
# print(cat1.age)
# print(cat1.name)
# cat1.speak()
# cat1.play()

#
# class Animal:
#     def __init__(self, name, color, age, food):
#         self.name = name
#         self.color = color
#         self.age = age
#         self.food = food
#
#     def eat(self):
#         print(f"I'm {self.name} and i'm eat {self.food}")
#
#     def __str__(self):
#         return f"I'm {self.__class__.__name__}. My name is {self.name}. I'm {self.age} and i'm eat {self.food}"
#
#
# class Cat(Animal):
#     def __init__(self, name, color, age, food, toy):
#         super().__init__(name, color, age, food)
#         self.toy = toy
#
#     def eat(self):
#         super().eat()
#         print(f'I like my toy {self.toy}')
#
#
# barsik = Cat("Barsik", "Red", 3, "meat", "rat")
# print(barsik)
# # barsik.eat()


# def meeting(*names: str) -> None:
#     for name in names:
#         print(f'Welcome, {name}!')
#
#
# meeting('ALex', 'Bob', 'Mary', 'Sarah','ALex', 'Bob', 'Mary', 'Sarah')


# class Item:
#     def __init__(self, name, amount, price):
#         self.name: str = name
#         self.amount: int = amount
#         self.price: int = price
#
#
# class Shop:
#     def __init__(self, *items):
#         self.stock: list = []
#
#         for item in items:
#             self.stock.append({'name': item.name, 'amount': item.amount, 'price': item.price})
#
#
# apple = Item('apple', 10, 20)
# banana = Item('banana', 20, 15)
#
# shop = Shop(apple, banana)
# print(shop.stock)


# class Cat:
#     def __init__(self, color, age, name, tail=True):
#         self.color: str = color
#         self.age: int = age
#         self.name: str = name
#         self.voice: str = 'Meow!'
#         self.tail: bool = tail
#
#     def counter(self, count: int = 0):
#         pass
#
#
# barsik = Cat('red', 5, "Barsik")
# print(barsik.voice)


# def add_num(*numbers: int):
#     num_list = []
#
#     for num in numbers:
#         try:
#             num_list.append(int(num))
#         except ValueError:
#             print('Ошибка ввода')
#             return
#
#     return num_list
#
#
# def check(num_list: list):
#     for num in num_list:
#         if num > 10:
#             return False
#
#     return True
#
#
# num_list = add_num(1, 2, '3f', 4)
# print(check(num_list))


# fruits = ['orange', 'apple', 'grape', 'banana']
#
# for fruit in fruits:
#     if fruit == 'berry':
#         print(fruit)
#     else:
#         continue
#

# import secrets
# import random
# def generate_password():
#     password = ''
#     chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
#
#     for i in range(random.randint(8, 12)):
#         password += secrets.choice(chars)
#
#     return password
#
# print(generate_password())
#
# day = "monday"
#
# match day:
#     case "monday":
#         print("It's Monday")
#     case "tuesday":
#         print("It's Tuesday")
#     case "wednesday":
#         print("It's Wednesday")
#     case "thursday":
#         print("It's Thursday")
#     case "friday":
#         print("It's Friday")
#     case "saturday":
#         print("It's Saturday")
#     case "sunday":
#         print("It's Sunday")
#     case _:
#         print("I don't know this day")
#


# def count_vowels_and_consonants(text: str):
#     """Ваш код"""
#
#     text = text.lower()
#     all_vowels ='ауоиэыяюеё'
#
#     vowels = sum(1 for letter in text if letter in all_vowels)
#     consonants = sum(1 for letter in text if letter.isalpha() and letter not in all_vowels)
#
#     return vowels, consonants
#
#
# input_string = input()
# vowels, consonants = count_vowels_and_consonants(input_string)
# print(vowels, consonants)
#
# def sort_products(input_strings: List[str]):
#     """ Обработка списка продуктов и вывод категорий с упорядоченными товарами. """
#     category_dict = {}
#     category_list = input_strings[0].split(',')
#
#     category_dict[category_list[1]] = (category_list[0], category_list[2])
#
#     return category_dict
#
#
# lines = []
# while True:
#     try:
#         line = input()
#         if line == "":
#             break
#     except EOFError:
#         break
#     lines.append(line)
#
# for string in sort_products(lines):
#     print(string)


