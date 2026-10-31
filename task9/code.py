budget = float(input("Enter budget: "))
n = int(input("Number of products: "))
items = []
total = 0
for i in range(n):
    name, p, q = input("Name, price, quantity: ").split()
    cost = float(p) * int(q)
    items.append([name, float(p), int(q)])
    total += cost
discount = 10 if total >= 1000 else 0
total *= (100 - discount) / 100
while total > budget:
    name, p, q = items[-1]; total -= p * q * (100 - discount) / 100; items.pop()
print("Final bill:", total, "Remaining products:", items)
