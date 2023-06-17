n = int(input())
days = []
for _ in range(n):
    day1, day2 = map(int, input().split())
    for i in range(day1, day2+1):
        days.append(i)
print(len(set(days)))
