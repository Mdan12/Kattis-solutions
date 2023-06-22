from collections import defaultdict
from heapq import *

n, cut = map(int, input().split())
nums = map(int, input().split())
dict_nums = defaultdict(lambda: 0)
for num in nums:
    dict_nums[num] -= 1

heapnums = list(dict_nums.values())
heapify(heapnums)

for _ in range(cut):
    heappush(heapnums, heappop(pq) + 1)
print(-heapnums[0])
