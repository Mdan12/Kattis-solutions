n = int(input())
x_angle = [[]]
y_angle = [[]]
i = 0

while True:
    if n == 0:
        break
    
    x, y = map(int, input().split())

    if x == -1 and y == -1:
        max_x = max([sum(l) for l in x_angle])
        max_y = sum([max(l) for l in y_angle])
        print(f"{max_x} x {max_y}")
        n = int(input())
        x_angle = [[]]
        y_angle = [[]]
        i = 0
    else:
        if sum(x_angle[i]) + x <= n:
            x_angle[i].append(x)
            y_angle[i].append(y)
        else:
            i += 1
            x_angle.append([x])
            y_angle.append([y])


