r, c, zr, zc = map(int, input().split())
for i in range(r):
    letters = input()
    string = ""
    for k in letters:
        string += k*zc
    for j in range(zr):
        print(string)
