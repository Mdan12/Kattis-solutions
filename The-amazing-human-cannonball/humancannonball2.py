from math import sin, cos, radians

n = int(input())
for _ in range(n):
    v0, degrees, x1, h1, h2 = map(float, input().split())
    t = x1/(v0 * cos(radians(degrees)))
    ballrange = v0 * t * sin(radians(degrees)) - 0.5*9.8*((t)**2)
    if ballrange + 1 < h2 and ballrange - 1 > h1:
        print("Safe")
    else:
        print("Not Safe")
