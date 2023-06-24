n = int(input())
num = list(map(int,str(n)))

while n%sum(num)!=0:
    n+=1
    num = list(map(int,str(n)))
print(n)
