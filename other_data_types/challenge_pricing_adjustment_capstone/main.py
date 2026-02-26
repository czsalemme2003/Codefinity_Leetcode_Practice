grocery_inventory = {"Milk":("Dairy", 3.50, 8),
                    "Eggs": ("Dairy", 5.50, 30),
                    "Bread": ("Bakery", 2.99, 15),
                    "Apples": ("Produce", 1.50, 50)}
print(grocery_inventory["Eggs"][1])
if grocery_inventory["Eggs"][1] > 5:
    print("eggs are too expensive, reducing the price by $1.")
    temp_list = list(grocery_inventory["Eggs"])
    temp_list[1] = 4.50
    grocery_inventory["Eggs"] = tuple(temp_list)
else:
    print("The price of Eggs is reasonable.")
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
print(grocery_inventory["Milk"][2])
if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    temp_list = list(grocery_inventory["Milk"])
    temp_list[2] = 28
    grocery_inventory["Milk"] = tuple(temp_list)
else: 
    print("Milk has sufficient stock")
if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop["Apples"]
    print("Apples removed from inventory due to high price.")
else: 
    pass
print("Updated Inventory:", grocery_inventory)