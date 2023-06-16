from math import sin, radians, ceil

height, angle = map(int, input().split())
degrees = radians(angle)
ladder = height/sin(degrees)
print(ceil(ladder))
