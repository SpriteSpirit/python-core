class House:
    def __init__(self, price: float):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value > 0 and not isinstance(value, str):
            self._price = value

    @price.deleter
    def price(self):
        del self._price


if __name__ == '__main__':
    house = House(50_000.0)

    # TestCase#1: Get price
    assert house.price == 50_000.0

    # TestCase#2: Set price
    house.price = 30_000.0
    assert house.price == 30_000.0

    # TestCase#3: Delete price
    del house.price
    assert house.price == 30_000.0


"""
Задача 2. Класс House

Реализуйте класс 
House
 с одним защищенным атрибутом — цена. Добейтесь следующего поведения от этого класса:

>>> house = House(50000.0)

>>> house.price
50000.0

>>> house.price = 45000.0  # обновили значение
>>> house.price
45000.0

>>> house.price = -50
Пожалуйста, введите корректное значение

>>> house.price
45000.0

>>> del house.price
>>> house.price
AttributeError: 'House' object has no attribute '_price'.
"""