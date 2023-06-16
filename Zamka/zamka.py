l = int(input())
d = int(input())
x = int(input())

mintemp = d
maxtemp = 0


for i in range(l, d + 1):
    nums = sum([int(nums) for nums in str(i)])
    if nums == x:
        if i < mintemp:
            mintemp = i
        if i > maxtemp:
            maxtemp = i

print(mintemp)
print(maxtemp)
