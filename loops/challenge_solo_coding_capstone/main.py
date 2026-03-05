# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}
for key, item in inventory.items():
    if inventory[key][0] < 30:
        print(f"{key} need restocking.")
    elif inventory[key][0] > 100:
        discount_price = inventory[key][2]
        print(f"{key} should be sold at the discounted price of {discount_price}.")
    elif 30 < inventory[key][0] < 100:
        regular_price = inventory[key][1]
        print(f"{key} should be sold at the regular price of {regular_price}.")
    else:
        pass
    