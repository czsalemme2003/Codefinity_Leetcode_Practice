prices = [29.99, 45.50, 12.75, 38.20]
discount = [0.1, 0.2, 0.15, 0.05]
for x in range(len(prices)):
    prices[x] = prices[x] - (prices[x] * discount[x])
    updated_price = prices[x]
    print(f"Updated price for item {x}: ${updated_price:.2f}")