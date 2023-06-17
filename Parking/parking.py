n = int(input())
for _ in range(n):
    n1 = int(input())
    numbers = list(map(int, input().split()))
    parking_dist = (max(numbers)-min(numbers))*2
    print(parking_dist)
