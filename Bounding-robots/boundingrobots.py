w, l = map(int, input().split())
while w!=0 and l!=0:
    rob_x, rob_y = 0, 0
    actual_x, actual_y = 0, 0
    for _ in range(int(input())):
        direction, spaces = input().split()
        if direction == "u":
            rob_y += int(spaces)
            actual_y+=int(spaces)
        elif direction == "d":
            rob_y -= int(spaces)
            actual_y-=int(spaces)
        elif direction == "l":
            rob_x -= int(spaces)
            actual_x-=int(spaces)
        elif direction == "r":
            rob_x += int(spaces)
            actual_x+=int(spaces)
        if actual_x>w-1:
            actual_x=w-1
        elif actual_x<0:
            actual_x=0
        elif actual_y>l-1:
            actual_y=l-1
        elif actual_y<0:
            actual_y=0
        
    print("Robot thinks",rob_x,rob_y)
    print("Actually at", actual_x, actual_y)
    print()
    w, l = map(int, input().split())