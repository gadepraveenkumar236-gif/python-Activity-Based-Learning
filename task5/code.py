v = input("Vehicle (B/C): ").upper()
e, x = map(int, input("Entry and exit hours (0-23): ").split())
if v not in ['B', 'C'] or not(0 <= e <= 23 and 0 <= x <= 23): print("Invalid input")
else:
    h = (x - e) % 24 or 24
    rate = 20 if v == 'B' else 40
    fee = min(h * rate, 200 if v == 'B' else 400)
    if x < e: fee += 50
    if h > 12: fee += 100
    print("Parking hours:", h, "Total fee: Rs.", fee)
