n = int(input())
x = input().split()
summa = 0
for i in range(n):
    if int(x[i]) < 0:
        summa += 1
print(summa)
