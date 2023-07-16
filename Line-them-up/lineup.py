n = int(input())
names = []
for _ in range(n):
    names.append(input())

if names==sorted(names):
    print("INCREASING")
elif names[::-1]==sorted(names):
    print("DECREASING")
else:
    print("NEITHER")