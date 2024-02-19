class Item:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price


class Shop:
    def __init__(self, *items):
        self.stock = {}
        for item in items:
            self.stock[item.name] = {'price': item.price, 'amount': item.amount}

        # создать метод show_info(), который выводит информацию о товаре и его количестве (что есть в магазине)

    def show_info(self, mandarin):
        print(f"В магазине есть {self.stock}")

    def sell(self, player):
        item_name = input("Какой товар хотите купить?: ")
        item_amount = int(input("Сколько вам нужно?: "))

        if item_name.lower() in self.stock:
            item = self.stock[item_name.lower()]
            if item['amount'] >= item_amount:
                if player.buy(item):
                    player.inventory[item_name.lower()] = item_amount
                    item['amount'] -= item_amount

                    print(f"{player.name} купил {item_name} в количестве {item_amount} штук ")
                    print(f"у {player.name} осталось {player.wallet} рублей")
                else:
                    print(f"У {player.name} нехватает денег")
            else:
                print(f"Такого количества {item_name} нет в наличии")
        else:
            print(f"Такого товара нет в наличии")


# класс покупателя, у которого есть кошелек, у которого инвентарь для купленных товаров
class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.inventory = {}

    def buy(self, product):
        print(type(product['price']))
        if self.wallet >= product['price']:
            return True
        else:
            return False


mandarin = Item('mandarin', 10, 50)
apple = Item('apple', 20, 30)

shop = Shop(mandarin, apple)
print(shop.stock)
# shop.show_info(mandarin)

person = Customer('Павел', 500)
# product1 = Item('apple', 20, 30)
# product2 = Item('watermelon', 30, 350)

shop.sell(person)
