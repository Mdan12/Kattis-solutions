cases = int(input())
quality = 0
for _ in range(cases):
    q, y = map(float, input().split())
    quality += q*y
print(f"{quality:.3f}")
