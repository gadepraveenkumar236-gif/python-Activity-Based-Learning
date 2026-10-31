n = int(input("Number of products: "))
for i in range(n):
    name = input("Product name: ")
    o, inc, dis, c = map(int, input("Opening, Incoming, Dispatched, Closing: ").split())
    expected = o + inc - dis
    diff = expected - c
    print("Product:", name)
    print("Discrepancy:", diff if diff != 0 else "No discrepancy")
    print("Replenishment:", max(0, 50 - c))

