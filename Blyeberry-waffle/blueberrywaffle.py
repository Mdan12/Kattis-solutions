r, f = map(int, input().split())
rotation = ((180/r)*f)%180
if 90>=rotation>=0:
    print("up")
else:
    print("down")
