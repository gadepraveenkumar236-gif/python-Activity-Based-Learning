d = float(input("Journey distance: "))
n = int(input("Number of vehicles: "))
reserve = float(input("Reserve fuel: "))
best = float('inf')
for i in range(n):
    name = input("Vehicle name: ")
    m, p, available = map(float, input("Mileage, fuel price, available fuel: ").split())
    fuel = d / m + reserve
    cost = fuel * p
    if fuel <= available and cost < best: best, choice = cost, name
    print(name, "Fuel:", fuel, "Cost:", cost)
print("Lowest cost:", choice, best) if best < float('inf') else print("No feasible vehicle")
