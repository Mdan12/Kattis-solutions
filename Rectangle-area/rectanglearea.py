from math import dist, hypot, sqrt

x1, y1, x2, y2 = map(float, input().split())

print(abs(max(x1, x2)-(min(x1,x2)))*abs(max(y1, y2)-min(y1,y2)))