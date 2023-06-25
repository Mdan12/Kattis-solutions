from math import prod

n = [int(i) for i in input() if i!='0']
while len(n)!=1:
    result = str(prod(n))
    n = [int(i) for i in result if i!='0']
print(n[0])