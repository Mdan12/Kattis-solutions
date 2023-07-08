P, N = map(int, input().split())
parts = []
for i in range(N):
    parts.append(input())
    if len(set(parts))==P:
        print(i+1)
        exit()
print("paradox avoided")