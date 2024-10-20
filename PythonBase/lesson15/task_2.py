import datetime


class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def from_birth_year(self):
        now_year = datetime.date.today().year
        self.__age = now_year - self.__age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if 0 < age < 120:
            self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if name.isalpha() and isinstance(name, str):
            self.__name = name


if __name__ == '__main__':
    men1 = Person('Patrick', 2000)
    men2 = Person('Holly', 25)

    # TestCase#1: from birth year
    men1.from_birth_year()
    assert men1.age == 24
    assert men2.age == 25

    # TestCase#2: Get age
    assert men1.age == 24
    assert men2.age == 25

    # TestCase#3: Set age
    men1.age = 25
    assert men1.age == 25
    men2.age = 26
    assert men2.age == 26

    # TestCase#4: Get name
    assert men1.name == 'Patrick'
    assert men2.name == 'Holly'

    # TestCase#5: Set name
    men1.name = 'Barry'
    assert men1.name == 'Barry'
    men2.name = 'Tom'
    assert men2.name == 'Tom'
