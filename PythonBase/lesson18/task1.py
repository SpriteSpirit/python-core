from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print('Car moving')


class Motorcycle(Vehicle):
    def move(self):
        print('Moto moving')


car = Car()
moto = Motorcycle()

collection = [car, moto]

for vehicle in collection:
    vehicle.move()
