total = int(input("Total classes: "))
attended = int(input("Attended classes: "))
threshold = 75
percentage = attended / total * 100
print("Attendance:", percentage, "%")
if percentage >= threshold:
    print("Eligible")
else:
    required = (threshold * total - 100 * attended) / (100 - threshold)
    required = int(required) + (required % 1 > 0)
    print("Required classes:", required)
