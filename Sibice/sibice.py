from math import sqrt

n, h, w = map(int, input().split())
box_size = sqrt(h**2+w**2)
for i in range(n):
    match_size = int(input())
    if box_size >= match_size:
        print("DA")
    else:
        print("NE")
