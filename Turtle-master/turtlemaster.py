def turtle_master():
    
    def index_2d(t, map):
        for i, x in enumerate(map):
            for j, k in enumerate(x):
                if t==k:
                    return (i, j)

    direction = 0  # Facing right at start
    
    turtles = [list(input().strip()) for _ in range(8)]
    movements = [(0,1),(1,0),(0,-1),(-1,0)]
    turtle_dir = (7,0)
    diamond_dir = index_2d("D", turtles)
    
    moves = input().strip()
    def movement(turtle_dir, movements):
        return (turtle_dir[0]+movements[direction][0], turtle_dir[1]+movements[direction][1])
    
    for move in moves:
        if move == "F":
            new_movement = movement(turtle_dir, movements)
            if 0 > new_movement[0] >= 8 or 0> new_movement[1] >= 8 or turtles[new_movement[0]][new_movement[1]] in {"C", "I"}:
                print("Bug!")
                return
            else:
                turtle_dir = new_movement
        elif move == "R":
            direction = (direction+1)%4
        elif move == "L":
            direction = (direction-1)%4
        elif move == "X":
            new_movement = movement(turtle_dir, movements)
            if turtles[new_movement[0]][new_movement[1]] != "I":
                print("Bug!")
                return
            turtles[new_movement[0]][new_movement[1]]= '.'
    
    if turtle_dir==diamond_dir:
        print("Diamond!")
    else:
        print("Bug!")       
                

turtle_master()
