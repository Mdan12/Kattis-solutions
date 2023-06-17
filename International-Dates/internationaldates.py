day, month, year = map(int, input().split("/"))

if day <= 12 and month <= 12:
    print("either")
elif day <= 12 and month >= 12:
    print("US")
else:
    print("EU")
