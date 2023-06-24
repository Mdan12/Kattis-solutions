from math import pi

r,m,c = map(float, input().split())
while r!=0 and m!=0 and c!=0:
    print(r*r*pi, 4*c/m*r*r)
    r,m,c = map(float, input().split())