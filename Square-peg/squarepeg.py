from math import sqrt,pow

L, R = map(int, input().split())
diameter = R*2
print("fits" if diameter>=sqrt(pow(L,2)+pow(L,2)) else "nope")