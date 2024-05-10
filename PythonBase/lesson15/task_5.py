class Date(object):
    def __init__(self, day: int = 0, month: int = 0, year: int = 0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_data: str):
        day, month, year = map(int, date_data.split('-'))
        month = str(month)
        if month[0] == '0':
            month = int(month[-1])
        else:
            month = int(month)
        return cls(day, month, year)

    @staticmethod
    def is_valid(date_data: str):
        try:
            day, month, year = map(int, date_data.split('-'))
            return True if all([0 < day < 32, 0 < month < 13, len(str(year)) == 4]) else False
        except ValueError:
            return False


if __name__ == '__main__':
    date = Date.from_string('12-02-2024')

    # TestCase#1: From string
    assert date.day == 12
    assert date.month == 2
    assert date.year == 2024

    # TestCase#2: Is date valid
    assert Date.is_valid('12-02-2024') == True
    assert Date.is_valid('14/15/2022') == False
    assert Date.is_valid('33-11-2023') == False
    assert Date.is_valid('33-13-2023') == False


"""
Есть класс 
Date
:

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

Реализуйте два метода 
from_string
 и 
is_date_valid
. Метод 
from_string
 создает и инициализирует экземпляр 
Date
 из переданной строки. Метод 
is_date_valid
 проверяет, корректные ли формат и значение строки переданы.

>>> date = Date.from_string('23-09-2022')
>>> date.day
23
>>> date.month
9
>>> date.year
2022
>>> Date.is_date_valid('23-09-2022')
True
>>> Date.is_date_valid('23-15-2022')  # месяц
False
>>> Date.is_date_valid('32-09-2022')  # день
False
"""
