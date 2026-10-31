n = int(input("Enter number of candidates: "))
a = []
for i in range(n):
    name = input("Name: ")
    m1, m2, m3 = map(int, input("Enter 3 subject marks: ").split())
    total = (m1 + m2 + m3) / 3
    if min(m1, m2, m3) >= 40 and total >= 60:
        a.append((total, name))
a.sort(reverse=True)
print("Admission Rank List:")
for marks, name in a: print(name, marks)
