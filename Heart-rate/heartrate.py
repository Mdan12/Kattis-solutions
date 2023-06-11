n = int(input())
sum = 0
for i in range(n):
    b, p = map(float, input().split())
    print(f"{60*(b-1)/p:.4f} {60*b/p:.4f} {60*(b+1)/p:.4f}")
