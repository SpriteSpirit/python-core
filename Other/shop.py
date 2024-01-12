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

    def __repr__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}"


class Shop:
    def __init__(self, *items):
        self.store = {"Sword": {"Price": 500, "Quantity": 30}}
        for item in items:
            self.store[item.name] = {'Price': item.price, 'Quantity': item.quantity}

    def show_info(self):
        return self.store

    def sell_item(self, buyer, item_name: str, amount: int):
        if item_name in self.store:
            if amount <= self.store[item_name]['Quantity']:
                total_price = amount * self.store[item_name]['Price']
                if total_price <= buyer.money:
                    buyer.money -= total_price
                    self.store[item_name]['Quantity'] -= amount
                    item = {"Name": item_name, "Quantity": amount}
                    buyer.get_item(item)
                else:
                    print('Недостаточно денег')
            else:
                print('Недостаточно товара')
        else:
            print('Такого товара нет')


class Player:
    def __init__(self, money):
        self.money = money
        self.inventory = []

    def get_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("Player inventory: ")
        for item in self.inventory:
            print(item)

    def show_money(self):
        print(f"Player money: {self.money}")


player = Player(1500)
sword = Item('Sword', 500, 30)
apple = Item('Apple', 50, 120)

shop = Shop(sword, apple)
print(shop.show_info())
player.show_money()
shop.sell_item(player, 'Sword', 2)
print(shop.show_info())

player.show_inventory()
player.show_money()
