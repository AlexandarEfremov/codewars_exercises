def get_order(order):
    working_order = order
    menu_list = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]
    clean_order = []
    for item in menu_list:
        if item.lower() in working_order:
            while item.lower() in working_order:
                clean_order.append(item)
                working_order = working_order.replace(item.lower(), "", 1)
    clean_order = " ".join(clean_order)
    return clean_order

print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))

# https://www.codewars.com/kata/5d23d89906f92a00267bb83d