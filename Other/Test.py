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


def get_sum(num1, num2, num3):
    result = num1 + num2 + num3
    return result


print(get_sum(5, 5, 5))

