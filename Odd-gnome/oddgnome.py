n = int(input())
for _ in range(n):
    gnomes = list(map(int, input().split()))[1::]
    for i in range(0,len(gnomes)-1):
        if gnomes[i+1]-gnomes[i]!=1:
            print(i+1)