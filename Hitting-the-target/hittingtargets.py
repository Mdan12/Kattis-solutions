def dot_in_circle(x,y,r,x1,y1):
    return (x-x1)**2 + (y - y1)**2 <= r**2

def dot_in_rectangle(x, y, x1, y1, x2, y2):
    return x >= x1 and x <= x2 and y >= y1 and y <= y2

shapes = []

for _ in range(int(input())):
   shapes.append(list(input().split()))
    

for _ in range(int(input())):
    sum = 0
    x, y = map(int, input().split())
    for shape in shapes:
        if shape[0] == "rectangle" and dot_in_rectangle(x, y, int(shape[1]), int(shape[2]), int(shape[3]), int(shape[4])):
            sum += 1
        elif shape[0] == "circle" and dot_in_circle(int(shape[1]), int(shape[2]), int(shape[3]), x, y):
            sum += 1
    print(sum)