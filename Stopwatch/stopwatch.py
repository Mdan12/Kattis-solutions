n = int(input())
sum = 0
for i in range(n):
    a = int(input())
    if i % 2 == 0:
        sum -= a
    else:
        sum += a
if n % 2 != 0:
    print("still running")
else:
    print(sum)
