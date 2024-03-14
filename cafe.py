# Code for running a cafe.

menu = ["pizza", "beer", "cider", "burrata"]

# How many portions of each item on the menu is in the cafe.
stock = {
    "pizza" : 100,
    "beer" : 50,
    "cider": 50,
    "burrata" : 25
}

# The cost per item on the menu.
price = {
    "pizza" : 12.5,
    "beer" : 6.5,
    "cider": 6,
    "burrata" : 7
}

# Looks for the item in both dictionaries and multiplies the stock quantity and price to calculate the total value of the stock.
total_stock_value = sum(price[x]*stock[x] for x in stock)
print(f"Total stock value = {total_stock_value}")
#Future menu

menu = ["pasta", "beer", "cider", "burrata"]

# How many portions of each item on the menu is in the cafe.
stock = {
    "penne" : 50,
    "rigatoni" : 50,
    "red wine": 30,
    "white wine": 30,
    "burrata" : 25
}

# The cost per item on the menu.
price = {
    "penne" : 10,
    "rigatoni" : 11,
    "red wine": 20,
    "white wine": 20,
    "burrata" : 7
}

# Looks for the item in both dictionaries and multiplies the stock quantity and price to calculate the total value of the stock.
total_stock_value = sum(price[x]*stock[x] for x in stock)
print(f"Total stock value = {total_stock_value}")

# New pasta menu for event nights.