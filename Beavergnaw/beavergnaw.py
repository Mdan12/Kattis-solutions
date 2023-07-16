import math

while True:
    D, V = map(int, input().split())
    if (D and V)==False:
        break
    print (round(pow((pow(D, 3) * math.pi / 6 - V) / (math.pi / 6), 1.0/3), 9))