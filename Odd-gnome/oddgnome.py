n = int(input())
for _ in range(n):
    gnomes = list(map(int, input().split()))[1:]
    for i in range(1,len(gnomes)-1):
        if gnomes[i]-gnomes[i-1]!=1:
            print(i+1)
            break