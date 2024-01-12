items_count = 0
items_sum = 0
row_index = 0

with open("shopping_list.txt") as file:
    for item_data in file:
        row_index += 1
        if item_data.count(":") < 2:
            print(f"There's an error in the {row_index} line")
            continue
        item, quantity, price = item_data.strip().split(":")
        items_count += 1
        items_sum = int(price) * int(quantity)

print(f"{items_count} items in the list. The sum of {items_sum} rubles")