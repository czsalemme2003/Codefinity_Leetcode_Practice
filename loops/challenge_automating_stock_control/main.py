# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for key, items in inventory.items():
    print(f"Processing {key}")
    while inventory[key][0] < inventory[key][1]:
        inventory[key][0] += inventory[key][2]
        if inventory[key][0] > discount_threshold and inventory[key][3] == False:
            inventory[key][3] = True
        else:
            pass
print("Processing completed")       
            
            

        