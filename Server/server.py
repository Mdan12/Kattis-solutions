n, time = map(int, input().split())
sum = 0
count = 0
tasks_time = list(map(int, input().split()))
for tasks in tasks_time:
    if sum + tasks <= time:
        sum += tasks
        count+=1
    else:
        break
    
print(count)
