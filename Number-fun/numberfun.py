n = int(input())
for i in range(n):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if a+b == c or a-b == c or a*b == c or a/b == c or b-a == c or b+a == c or b/a == c or b*a == c:
        print("Possible")
    else:
        print("Impossible")
