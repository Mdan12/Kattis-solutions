width = int(input())
n = int(input())
sum = 0
for _ in range(n):
    w, l = map(int, input().split())
    sum += w*l
print(int(sum/width))
