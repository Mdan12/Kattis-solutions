n = int(input())
asda = n
counter = 0
a = input().split()
for i in range(n):
    i = int(i)
    if int(a[i]) == -1:
        asda -= 1
    else:
        counter += int(a[i])
print(counter/asda)
