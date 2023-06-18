n = int(input())

time1, glucose1 = map(float, input().split())
sum = 0
for _ in range(n-1):
    time, glucose = map(float, input().split())
    sum += ((glucose1+glucose)/2)*(time-time1)/1000
    time1 = time
    glucose1 = glucose
print(sum)
