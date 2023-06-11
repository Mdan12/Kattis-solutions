n = int(input())
for _ in range(n):
    voltage = list(map(int, input().split()))
    print(sum(voltage)-2*voltage[0]+1)
