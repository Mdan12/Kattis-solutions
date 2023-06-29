import operator

ops = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}

a,b,c = map(int, input().split())

for i,k in ops.items():
    if k(a,b)==c:
        print(a,i,b,"=",c,sep='')
        break
    if k(b,c)==a:
        print(a,"=",b,i,c,sep='')
        break