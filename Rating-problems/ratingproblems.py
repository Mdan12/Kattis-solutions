n, k = map(int, input().split())
maxsum = 0
minsum = 0
for _ in range(k):
    a = int(input())
    maxsum += a
    minsum += a
maxsum += 3*(n-k)
minsum -= 3*(n-k)

print(minsum/n, maxsum/n)
