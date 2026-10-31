n = int(input("Number of subjects: "))
total = 0
for i in range(n):
    s = input("Subject: ")
    a, b = map(int, input("Previous and current marks: ").split())
    total += b
    print(s, "Improvement/Decline:", b-a, "Weak" if a < 40 and b < 40 else "")
avg = total / n
print("Average:", avg)
print("Result:", "Excellent" if avg >= 80 else "Good" if avg >= 60 else "Needs Improvement")

