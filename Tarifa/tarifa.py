x = int(input())
n = int(input())
totaldata = x*(n+1)
for _ in range(n):
    data = int(input())
    totaldata -= data
print(totaldata)
