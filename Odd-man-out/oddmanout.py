from collections import Counter

n = int(input())
for i in range(1, n+1):
    a = int(input())
    num = map(int, input().split())
    list_num = list(num)
    counter_num = Counter(list_num)
    for key, value in counter_num.items():
        if value == 1:
            print(f"Case #{i}: {key}")
