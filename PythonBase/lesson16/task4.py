# class MyOpen:
#
#     def __init__(self, filename, mode):
#         self.__filename = filename
#         self.__mode = mode
#
#     def __enter__(self):
#         self.__file = open(self.__filename, self.__mode)
#         return self.__file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.__file.close()
#
#
# with MyOpen('hello', 'w') as file:
#     print(file.write('hello world'))
#
# with MyOpen('hello', 'r') as file:
#     print(file.read())
import math


# import math
#
# number = 501
# rounded_number = math.ceil(number / 10) * 10
#
# print(rounded_number)  # Выведет 230
# next_hp = 0
# hp = 150
# next_hp += math.ceil(((hp//2) + hp) / 10) * 10
# print(next_hp)

# level = 1
# exp = 15
#
# level = 1 + (exp//15)
# print(level)
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.experience = 0
        self.level = 1

    def get_level(self):
        return self.level

    def get_health(self):
        return self.health

    def add_experience(self, exp):
        self.experience += exp

        next = 15
        level_exp = [15, 30, 60, 120]
        print(level_exp)
        level = 1
        health = 100

        for e in range(5):
            level_exp.append(15 * 2)

        # for exp_needed in level_exp:
        #     if self.experience >= exp_needed:
        #         level += 1
        #         health = math.ceil(health * 1.5/10)*10
        #     else:
        #         break

        self.level = level
        self.health = health

        print("New level:", self.level)
        print("New health:", self.health)


hero = Hero('Hello')

print(f'get_level: {hero.get_level()}')
print(f'get_health: {hero.get_health()}')
hero.add_experience(300)
print(f'get_level: {hero.get_level()}')
print(f'get_health: {hero.get_health()}')


