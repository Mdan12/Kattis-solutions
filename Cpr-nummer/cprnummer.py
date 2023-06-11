n = list(map(int, (''.join(input().split("-")))))
a = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
sum = 0
for i in range(len(a)):
    sum += n[i]*a[i]
sum = sum % 11
if sum == 0:
    print(1)
else:
    print(0)
