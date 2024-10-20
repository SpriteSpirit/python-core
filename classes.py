class Person:
    def __init__(self, name, age):
        self.name: str = name
        self.age: int = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id: int = id

    def greet(self):
        print(super().greet())
        return f"I am student with ID: {self.id}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject: str = subject

    def study(self):
        return f"I am studying {self.subject}."


masha = Student("Masha", 17, 56789)
maria_ivanovna = Teacher("Maria Ivanovna", 35, "Math")

print(masha.greet())
print(maria_ivanovna.greet())
print(maria_ivanovna.study())
print(maria_ivanovna.__dict__)
