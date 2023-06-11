n = int(input())
sum = 0
for _ in range(n):
    a = input()
    sum += int(a[:len(a)-1])**int(a[len(a)-1])
print(sum)
