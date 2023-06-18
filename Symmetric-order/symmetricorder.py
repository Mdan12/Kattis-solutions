n = int(input())
set = 1
while n != 0:
    names = [0]*n
    for i in range(int(n/2)):
        name1 = input()
        name2 = input()
        names[i] = name1
        names[n-1-i] = name2
    if n % 2 != 0:
        names[int(n/2)] = input()
    print("SET", set)
    set += 1
    for i in names:
        print(i)
    n = int(input())
