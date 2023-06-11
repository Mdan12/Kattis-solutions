P = int(input())
for i in range(P):
    K, b, n = map(int, input().split())
    sum = 0
    while n > 0:
        dig = n % b
        n = n // b
        sum += dig * dig
    print(K, sum)
