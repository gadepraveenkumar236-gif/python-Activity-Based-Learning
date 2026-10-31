n = int(input("Enter number of students: "))
s = []
for i in range(n):
    name = input("Name: ")
    m, sub, a, inc = map(int, input("Marks Subject Attendance Income: ").split())
    if m >= 75 and sub >= 40 and a >= 75 and inc <= 200000:
        s.append((m, a, name))
s.sort(reverse=True)
for x in s:
    print(x[2], "Scholarship Rank:", s.index(x)+1)
