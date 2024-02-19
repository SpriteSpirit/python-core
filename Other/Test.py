'''hello = "ONE****TWO****THREE"

hello_list = hello.split('----')

print(hello_list)


from random import randint


class Dice:
    def __init__(self, faces):
        self.faces = faces
        self.history = []

    def dice_throw(self):
        res = randint(1, self.faces)
        self.history.append(res)
        return res

    def get_history(self, x):
        return self.history[-x:]


dice = Dice(4)
print(dice.dice_throw())
print(dice.dice_throw())
print(dice.dice_throw())
print(dice.dice_throw())
print(dice.get_history(2))

a = float(input("A: "))
b = (a * 10) // 1 % 10 % 10


print(b)


def multiply_range(start, end):
    result = 1

    if start > end:
        start, end = end, start

    for num in range(start, end + 1):
        result *= num

    return result


print(multiply_range(5, 10))
'''