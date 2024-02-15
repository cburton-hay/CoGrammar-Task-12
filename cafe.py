# Code for running a cafe.

menu = ["coffee", "hot chocolate", "tea", "pastry"]

# How many portions of each item on the menu is in the cafe.
stock = {
    "coffee" : 200,
    "hot chocolate" : 100,
    "tea": 150,
    "pastry" : 50
}

# The cost per item on the menu.
price = {
    "coffee" : 3,
    "hot chocolate" : 2.5,
    "tea": 2,
    "pastry" : 1.25
}

# Looks for the item in both dictionaries and multiplies the stock quantity and price to calculate the total value of the stock.
total_stock_value = sum(price[x]*stock[x] for x in stock)
print(f"Total stock value = {total_stock_value}")