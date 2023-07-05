for j in range(int(input())):
    print('Test',j+1)
    n, m = map(int, input().split())
    array =[]
    for i in range(n):
        array.append(list(input()))
    for x in array[::-1]:
        for l in x[::-1]:
            print(l, end="")
        print()