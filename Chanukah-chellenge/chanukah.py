n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    sum = -1
    for i in range(1, b+2):
        sum += i
    print(a, sum)
