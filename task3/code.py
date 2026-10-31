b = float(input("Initial balance: "))
n = int(input("Number of transactions: "))
d = w = r = 0
for i in range(n):
    t, a = input("Enter D/W and amount: ").split()
    a = float(a)
    if a <= 0: r += 1
    elif t == 'D': b += a; d += 1
    elif t == 'W' and a <= b and a <= 10000: b -= a; w += 1
    else: r += 1
print("Balance:", b, "Deposits:", d, "Withdrawals:", w, "Rejected:", r)

Withdrawal limit: ₹10,000 per transaction.
