lawns = float(input())
amount = int(input())
placeholder = 0
for i in range(amount):
    a, b = input().split()
    a = float(a)
    b = float(b)
    placeholder += a*b
print(placeholder*lawns)
