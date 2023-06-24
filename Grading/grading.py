grades = list(zip("ABCDE", map(int, input().split()))) + [("F", 0)]
n= int(input())
print(next(c for c, s in grades if n >= s))