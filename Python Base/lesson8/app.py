from lesson8.validators.validate_pin import validate_pin
from lesson8.validators.validate_card import validate_card

print("Введите ваш номер карты")
card_number = input()
print("Введите ваш ПИН-код")
card_pin = input()

if validate_pin(card_pin):
    pin = "ПИН-код допустимый"
else:
    pin = "ПИН-код недопустимый"

if validate_card(card_number):
    card = "Номер карты допустимый"
else:
    card = "Номер карты недопустимый"

print(card, pin, sep="\n")