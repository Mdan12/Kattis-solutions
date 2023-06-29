n = int(input())

flights = [[int(i) for i in input().split()] for j in range(n)]
neg = []

for i in range(n):
    for j in range(n):
        if flights[i][j] != -1:
            neg.append("{} {} {}".format(i+1,j+1,flights[i][j]))
            
print(len(neg))
for i in neg:
    print(i)