n = int(input())
nums = sorted(list(map(int, input().split())))
sum = 0
for num in range(1,n):
    sum += nums[0]+nums[num]
print(sum)