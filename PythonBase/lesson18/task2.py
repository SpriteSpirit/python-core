from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, surname, salary):
        print('Добавлен сотрудник')
        self.name = name
        self.surname = surname
        self.salary = salary


class MixinLog:
    ID = 0

    def __init__(self, name, surname, salary):
        super().__init__(name, surname, salary)
        MixinLog.ID += 1
        print(f'Добавлен сотрудник с номером: {self.ID}')


class Developer(MixinLog, Employee):

    def __init__(self, name, surname, salary, lang):
        print('Добавлен разработчик')
        super().__init__(name, surname, salary)
        self.lang = lang


dev1 = Developer('Ivan', 'Ivanov', 150_000, 'Python')
dev2 = Developer('Petr', 'Petrov', 160_000, 'C#')
dev3 = Developer('Semen', 'Semenov', 180_000, 'Java')
# print(dev.__dict__)
print(Developer.__mro__)
