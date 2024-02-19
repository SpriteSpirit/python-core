"""import requests
import random


class Lesson:
    def __init__(self, lesson_name=""):
        self.name = lesson_name

    def __repr__(self):
        return f"Lesson('{self.name}')"


# URL сервера npoint.io, где хранятся уроки
url = "https://api.npoint.io/d0e35babc9ee62c44208"

# Запрос данных с сервера
response = requests.get(url)

# Проверка, успешно ли выполнен запрос
if response.status_code == 200:
    # Извлечение списка уроков из ответа сервера
    lessons = response.json()
    print(lessons)

    # Создание списка объектов уроков
    lesson_objects = [Lesson(lesson_name) for lesson_name in lessons]

    # Вывод случайного урока
    random_lesson = random.choice(lesson_objects)
    print(random_lesson)
else:
    print("Ошибка при получении данных с сервера")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


circle = Circle(5)
print(circle.diameter)  # Выводит 10

circle.diameter = 15
print(circle.radius)  # Выводит 7.5

import random
import turtle

for i in range(10):
    for j in range(4):
        turtle.forward(100)
        turtle.left(90)
    random_x = random.randint(-250, 250)
    random_y = random.randint(-300, 300)
    turtle.goto(random_x, random_y)

turtle.mainloop()

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

count = 0

if a == b == c:
    count = 3
elif a == c or a == b:
    count = 2
elif a != b != c:
    count = 0
print("Количество одинаковых чисел:", count)"""

'''import unittest


class TodoList:

    def __init__(self):
        # Конструктор класса TodoList, инициализирует список задач
        self._tasks = []

    def add_task(self, new_task):
        # Метод для добавления новой задачи в список задач
        self._tasks.append(new_task)

    def fetch_tasks(self):
        # Метод для получения списка задач
        return self._tasks


class TodoListTests(unittest.TestCase):

    def test_add_task(self):
        # Создаем экземпляр класса TodoList
        todo_list = TodoList()

        # Добавляем задачи в список
        todo_list.add_task("Задача 1")
         todo_list.add_task("Задача 2")

        # Проверяем, что список задач содержит добавленные задачи
        self.assertEqual(todo_list.fetch_tasks(), ["Задача 1", "Задача 2"])

    def test_fetch_tasks(self):
        todo_list = TodoList()
        todo_list.add_task("Задача 1")
        todo_list.add_task("Задача 2")

        tasks = todo_list.fetch_tasks()

        # Сравниваем содержимое списков, а не ссылки на них
        self.assertListEqual(tasks, ["Задача 1", "Задача 2"])


if __name__ == '__main__':
    unittest.main()

import unittest


def get_average(numbers):
    return sum(numbers) / len(numbers)


class TestGetAverage(unittest.TestCase):
    def test_get_average(self):
        # Проверяем, что среднее арифметическое корректно вычисляется
        self.assertEqual(get_average([1, 2, 3]), 2)
        self.assertEqual(get_average([4, 5, 6]), 5)
        self.assertEqual(get_average([10, 20, 30]), 20)

    def test_empty_list(self):
        # Проверяем, что функция возвращает None для пустого списка
        self.assertEqual(get_average([]), None)

    def test_single_item(self):
        # Проверяем, что функция возвращает значение элемента для списка из одного элемента
        self.assertEqual(get_average([5]), 5)


if __name__ == '__main__':
    unittest.main()
'''

""""import unittest
from parameterized import parameterized


def has_rrr(word):
    return "р" in word.lower()


class TestHasRrr(unittest.TestCase):

    @parameterized.expand([
        ("речка", True),
        ("уточка", False),
        ("Ромашка", True),
        ("Арбуз", False)
    ])
    def test_has_rrr(self, word, expected_result):
        self.assertEqual(has_rrr(word), expected_result)


if __name__ == '__main__':
    unittest.main()




import unittest
from parameterized import parameterized
def get_min_sec(sec):

    sec_only = sec %  60
    min_only = sec // 60
    return {"min": min_only, "sec": sec_only}

# Не удаляйте код ниже, он нужен для проверки

value = int(input())
result = get_min_sec(value)
print(result)

class GetMinSecTest(unittest.TestCase):

    @parameterized.parameterized.expand(

        [(120, f"{'min': \\{2}, 'sec': \\{0}}"),

         (150, f"{'min': \\{2}, 'sec': \\{30}}"),

         (15, f"{'min': \\{0}, 'sec': \\{15}}")])
    def test_get_min_sec(self, sec, expected_result):
        self.assertEqual(get_min_sec(sec), expected_result)



a = input("a: ")

try:
    a = int(a)
    raise ValueError("Некорректное значение")
except ValueError as e:
    # Обработка исключения
    print("Произошла ошибка:", str(e))
"""
from random import randint
class Dice:

    def __init__(self, faces):
        self.faces = faces
        self.history = []

    def dice_throw(self):
        face = randint(1, self.faces)
        self.history.append(face)
        return face

    def get_history(self, x=0):
        return self.history[-x:]


dice_4 = Dice(4)
print(dice_4.dice_throw())
print(dice_4.dice_throw())
print(dice_4.dice_throw())
print(dice_4.dice_throw())
print(dice_4.get_history(3))
