from heapq import *

h, c = map(int, input().split())

coworkers = []
for _ in range(c):
    a, d = map(int, input().split())
    coworkers.append((a, d))
    
heapify(coworkers)

for _ in range(h):
    pop_a, d = heappop(coworkers)
    heappush(coworkers, (pop_a + d, d))
    
    
ans = max(coworkers, key=lambda x: x[0]-x[1])
print(ans[0]-ans[1])