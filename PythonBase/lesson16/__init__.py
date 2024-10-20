import datetime


class Employee:
    coefficient = 2

    def __init__(self, name: str, surname: str, salary: int):
        self.name = name
        self.surname = surname
        self.__salary = salary

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.surname}, {self.__salary})'

    def __str__(self):
        return f'{self.fullname} ({self.__salary})'

    def __len__(self):
        return len(self.fullname)

    def __add__(self, other):
        return self.__salary + other.__salary

    def raise_salary(self):
        self.__salary *= self.coefficient

    @classmethod
    def from_string(cls, data_sting: str):
        name, surname, salary = data_sting.split()
        salary = int(salary)

        return cls(name, surname, salary)

    @classmethod
    def set_raise_amount(cls, new_coef: int):
        cls.coefficient = new_coef

    @staticmethod
    def is_workday():
        now = datetime.datetime.now()
        if now.weekday() == 5 or now.weekday() == 6:
            return False
        return True

    @property
    def salary(self):
        return self.__salary

    @property
    def email(self):
        return f"{self.name.lower()}.{self.surname.lower()}@myjobmail.com"

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, data_string: str):
        name, surname = data_string.split()
        self.name = name
        self.surname = surname

    # def __repr__(self):
    #     return f"Name: {self.name}\nSurname: {self.surname}\nSalary: {self.salary} rub."


if __name__ == '__main__':
    employee1 = Employee("Ivan", "Ivanov", 60_000)
    employee2 = Employee.from_string('Petr Petrov 70_000')

    print(repr(employee1))
    print(employee1)
    print(len(employee1))
    print(employee1 + employee2)

    # TestCase#1: email
    assert employee1.email == "ivan.ivanov@myjobmail.com"

    # TestCase#1.1: email
    employee1.name = "Semen"
    assert employee1.email == "semen.ivanov@myjobmail.com"

    # TestCase#2: RaiseSalary
    employee1.raise_salary()

    assert 60_000 * Employee.coefficient == employee1.salary
    assert employee1.salary == 120_000

    # TestCase#3: New object

    assert isinstance(employee2, Employee)
    assert employee2.name == "Petr"
    assert employee2.surname == "Petrov"
    assert employee2.salary == 70_000

    # TestCase#4: Set raise amount
    Employee.set_raise_amount(3)
    assert Employee.coefficient == 3
    assert employee1.coefficient == 3
    assert employee2.coefficient == 3

    # TestCase#5: Is workday
    assert Employee.is_workday() == False

    # TestCase#6: Get fullname
    assert employee1.fullname == 'Semen Ivanov'
    assert employee2.fullname == 'Petr Petrov'

    # TestCase#7: Set fullname (name, surname)
    employee1.fullname = 'Joseph Monterey'
    assert employee1.name == 'Joseph'
    assert employee1.surname == 'Monterey'



