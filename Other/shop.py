class Item:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity


class Shop:
    def __init__(self, *items):
        self.stock = {}
        for item in items:
            self.stock[item.name] = {
                "Cost": item.cost,
                "Quantity": item.quantity
            }

    def display_info(self):
        return self.stock


apple = Item("apple", 20, 15)
shop = Shop(apple)
shop.display_info()


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # def __repr__(self):
    #     return f"Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}"

    def __str__(self):
        return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'


class Shop:
    def __init__(self, *items):
        self.store = []

        for item in items:
            self.store.append({'Name': item.name, 'Price': item.price, 'Quantity': item.quantity})

    def show_info(self):
        # for item in self.store:
        #     print(f"{item['Name']}: {item['Price']} coins [{item['Quantity']} pieces]")
        return self.store

    def sell_item(self, buyer, item_name: str, amount: int):
        for item in self.store:
            if item['Name'] == item_name:
                if item['Quantity'] >= amount:
                    total_price = amount * item['Price']
                    if buyer.money >= total_price:
                        buyer.money -= total_price
                        item['Quantity'] -= amount
                        item = {"Name": item_name, "Quantity": amount}
                        buyer.get_item(item)
                        return 'Спасибо за покупку!'
                    else:
                        return 'Недостаточно денег'
                else:
                    return 'Недостаточно товара'
            else:
                continue
        else:
            return 'Такого товара нет'


class Player:
    def __init__(self, money):
        self.money = money
        self.inventory = []

    def get_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("Player inventory: ")
        for item in self.inventory:
            print(f"{item['Name']} [{item['Quantity']} pieces]")

    def show_money(self):
        return f"Player money: {self.money}"


player = Player(1500)
sword = Item('Sword', 500, 30)
apple = Item('Apple', 50, 120)

print(player.show_money())

shop = Shop(sword, apple)

print('')

for item in shop.show_info():
    print('Список товаров:')
    print(f"Name: {item['Name']}\nPrice: {item['Price']}\nQuantity: {item['Quantity']}")
    print('')

print(shop.sell_item(player, 'Sword', 2))

print('')
# shop.show_info()

print('')
player.show_inventory()
print(player.show_money())
print()

# print(repr(apple))
print(apple)
