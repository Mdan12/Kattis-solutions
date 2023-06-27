n, k = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(k-1,len(nums), k):
    print(nums[i], end=" ")