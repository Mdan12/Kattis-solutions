def reduced_id():
    n = int(input())
    if n == 1:
        print(1)
        return  
    a = 1
    turtles = [(int(input())) for _ in range(n)]
    asd = [i%a for i in turtles]
    while len(set(asd))<n:
        a+=1
        asd = [i%a for i in turtles]
    print(a)
reduced_id()