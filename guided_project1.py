

item_list = ["Laptop", "Headset", "Second Monitor",
             "Mousepad", "USB Drive", "External Drive"]

print(item_list)

mandotary_item_list = item_list[0:3]
optional_item_list = item_list[3:6]
print("mandotary:", mandotary_item_list)
print("optional:", optional_item_list)

limit = 5000
price_sheet = {
    "Laptop": 1500,
    "Headset": 100,
    "Second Monitor": 200,
    "Mousepad": 50,
    "USB Drive": 70,
    "External Drive": 250
}
cart = []


def add_to_cart(item, quantity):
    cart.append((item, quantity))
    item_list.remove(item)


def create_invoice():
    total_amount_inc_tax = 0
    for item, quantity in cart:
        price = price_sheet[item]
        tax = 0.18 * price
        total = (tax + price) * quantity
        total_amount_inc_tax += total
        print('Item:', item, "\t", "Prices:", price, "\t", "Quantity:",
              quantity, "\t", "Tax:", tax, "\t", "Total:", total, "\n")
    print("After the tax applied the total amount is :",
          " \t", total_amount_inc_tax)

    return total_amount_inc_tax


def checkout():
    global limit
    total_amount = create_invoice()
    if limit == 0:
        print("You don't have any budget.")
    elif total_amount > limit:
        print("You exceede the limit.")
    else:
        limit -= total_amount
        print(
            f'The total amount (inc1 taxes) you have paid is {total_amount}, you have limit dollars left.')


add_to_cart("Laptop", 1)
add_to_cart("Headset", 8)
add_to_cart("Second Monitor", 1)
add_to_cart("Mousepad", 1)
add_to_cart("USB Drive", 2)
add_to_cart("External Drive", 4)

checkout()
