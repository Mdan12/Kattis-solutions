n = int(input())
sum = ""
while n != 0:
    sum += str(n % 2)
    n = n//2
revsum = sum[::-1]
summa = 0
x = 0
for i in revsum:
    if int(i) == 1:
        summa += 2**x
    x += 1
print(summa)
