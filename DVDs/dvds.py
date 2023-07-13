def bubble_dvds():
    n = int(input())
    for _ in range(n):
        dvds_len = int(input())
        dvds = list(map(int, input().split()))
        index = 1
        for i in dvds:
            if i == index:
                index+=1
        index-=1
        print(dvds_len-index)
bubble_dvds()
