
class Employee:
    coefficient = 2

    def __init__(self, name: str, surname: str, salary: int):
        self.name = name
        self.surname = surname
        self.salary = salary

    def raise_salary(self):
        self.salary *= self.coefficient

    def __add__(self, other):
        if isinstance(other, self.__class__): # проверяет принадлежность объекта к определенному классу
            return self.salary + other.salary

        if issubclass(other.__class__, self.__class__): # проверяет, наследуется ли один класс от другого
            return self.salary + other.salary

        return None


class Developer(Employee):
    coefficient = 1.5

    def __init__(self, name, surname, salary, lang):
        super().__init__(name, surname, salary)
        self.lang = lang


emp1 = Employee('Semen', 'Smirnov', 150_000)

dev1 = Developer('Ivan', 'Ivanov', 100_000, 'Python')
dev2 = Developer('Petr', 'Petrov', 130_000, 'Java')


print(dev1.__dict__)

total_pay = dev2 + dev1
print(total_pay)

