cap = int(input("Tank capacity: "))
level = int(input("Initial water level: "))
limit = int(input("Required threshold: "))
n = int(input("Number of days: "))
first = -1
for day in range(1, n + 1):
    i, o = map(int, input("Inflow and outflow: ").split())
    level += i - o
    if level > cap: print("Overflow"); level = cap
    if level < 0: print("Shortage"); level = 0
    if level >= limit and first == -1: first = day
    print("Day", day, "Water level:", level)
print("First threshold day:", first if first != -1 else "Not reached")

