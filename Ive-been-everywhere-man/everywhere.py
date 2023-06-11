n = int(input())
for i in range(n):
    a = int(input())
    la = []
    for j in range(a):
        b = input()
        la.append(b)
    print(len(set(la)))
