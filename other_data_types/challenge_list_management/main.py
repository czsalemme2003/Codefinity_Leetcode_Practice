meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp" ]
condiment = ["Mustard", 1.99, 75, "Spicy"]
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)
meat[2] = 100
print(meat)
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
deli_dept.remove(condiment)
deli_dept.sort()
print("Updated Deli List:", deli_dept)