n = int(input())
checkers = []
white = 0
black = 0

for _ in range(n):
    checkers.append(list(input()))

for i in checkers[0]:
    white += i.count("W")
    black += i.count("B")
    
for i in checkers:
    if i.count("B") != black or i.count("W") != white:
        print(0)
        exit()
    for j in range(0,len(i)-3):
        if i[j]==i[j+1]==i[j+2]:
            print(0)
            exit()

transposed_list = [[checkers[j][i] for j in range(n)] for i in range(len(checkers[0]))]

for i in transposed_list:
    check = i[0]
    if i.count("B") != black or i.count("W") != white:
        print(0)
        exit()
    for j in range(0,len(i)-3):
        if i[j]==i[j+1]==i[j+2]:
            print(0)
            exit()

print(1)