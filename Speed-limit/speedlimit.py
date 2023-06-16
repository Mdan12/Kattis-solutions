n = int(input())
while n != -1:
    sum = 0
    placeholder = 0
    for i in range(n):
        x, y = map(int, input().split())
        sum += x*(y-placeholder)
        placeholder = y
    print(sum, "miles")
    sum = 0
    n = int(input())
