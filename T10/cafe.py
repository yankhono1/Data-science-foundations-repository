print("\nWelcome\n")

# create a list called menu tha contains at least four items 
menu = ["Tea", "Coffee", "Cinnamon bun", "Croissant"]
# create a dictionary called stock containing the stock for each item on the menu
stock = {"Tea": 5, "Coffee": 10, "Cinnamon bun": 20, "Croissant": 15}
# create another dictionary called price containing the price for each item on the menu
price = {"Tea": 1.50, "Coffee": 2.10, "Cinnamon bun": 3, "Croissant": 2.50}
# calculate the total stock price
total_stock_price = 0

# loop through appropriate dictionaries and lists

for item in menu:
    # access the corresponding stock and price values
    # This line accesses the stock dictionary using the current item as the key. It retrieves the stock quantity for the current item.
    stock_value = stock[item]
    # This line accesses the price dictionary using the current item as the key. It retrieves the price for the current item.
    price_value = price[item]
    
    # calculate the value of items in stock
    item_value = stock_value * price_value
    # This line adds the item_value (the value of the current item in stock) to the total_stock_price variable.
    total_stock_price += item_value

print(f"The total stock price is: ${total_stock_price:.2f}")

# when you loop through the menu list items can be set as keys to access the corresponding stock and price values

# item_value = (stock[items] * price[items])
