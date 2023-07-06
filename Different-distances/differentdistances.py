distances = input()
while distances!="0":
    x1, y1, x2, y2, p = map(float, distances.split())
    print(f"{(abs(x1-x2)**p+abs(y1-y2)**p)**(1/p):.10f}")
    distances = input()