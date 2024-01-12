'''class Hero:

    def go_right(self):
        print("Я иду направо")

    def go_left(self):
        print("Я иду налево")

    def observe(self):
        print("Я осматриваюсь")

    def go_up(self):
        print("Я иду наверх")

    def go_down(self):
        print("Я иду вниз")

    def rest(self):
        print("Я отдыхаю")


hero = Hero()

hero.go_up()
hero.go_up()
hero.observe()
hero.go_down()
hero.go_down()
hero.rest()


class Hero:

  def go_right(self):
    print("Я иду направо")

  def go_left(self):
    print("Я иду налево")

  def observe(self):
    print("Я осматриваюсь")


pythomir = Hero()
flaskomir = Hero()
djangomir = Hero()

heroes = [pythomir, flaskomir, djangomir]

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)
assert len(heroes) == 3, "в списке не три героя"
assert isinstance(pythomir, Hero), "pythomir – не экземпляр Hero"
assert isinstance(flaskomir, Hero), "flaskomir – не экземпляр Hero"
assert isinstance(djangomir, Hero), "djangomir – не экземпляр Hero"
print("Условия выполнены")



class Hero:

    def __init__(self):
        self.print_init()

    def print_init(self):
        print("Я инициализировался!")


# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

print("Проверка:")
pythomir = Hero()



class Hero:
    def __init__(self, name, motto):
        self.name = name
        self.motto = motto


pythomir = Hero("Питомир", "Кусь за Русь")
flaskomir = Hero("Фласкомир", "Это нужно отметить")
djangomir = Hero("Джангомир", "Работает – и ладно!")

# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

if not hasattr(pythomir, "name"): print("Имя не задано")
if not hasattr(pythomir, "motto"): print("Девиз не задан")
print("Условия выполнены")



class Hero:

    def __init__(self, name, motto):
        self.name = name
        self.motto = motto

    def say(self):
        print(f"{self.name} говорит: {self.motto}")


# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

pythomir = Hero("Питомир", "Кусь за Русь!")
pythomir.say()
djangomir = Hero("Джангомир", "Работает - и ладно!")
djangomir.say()
'''


class Hero:

    def __init__(self, name):
        self.name = name
        self.things = []

    def collect(self, thing):
        self.things.append(thing)


# Не удаляйте код ниже, это проверка (иначе мы укусим вас за бочок)

pythomir = Hero("Питомир")
pythomir.collect("Усы хитрости")
pythomir.collect("Рукавички пряморукости")

if len(pythomir.things) == 2:
    print("Проверка пройдена")
else:
    print("Добавление в список things работает некорректно")
