from math import sqrt

x, y, x1, y1, x2, y2 = map(int, input().split())

if x1 <= x <= x2 and y1 <= y <= y2:
        print(0.0)
    
closest_x = min(max(x1, x), x2)
closest_y = min(max(y1, y), y2)

distance = sqrt((x - closest_x) ** 2 + (y - closest_y) ** 2)
print(distance)