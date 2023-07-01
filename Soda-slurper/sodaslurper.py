from math import ceil

e, f, c = map(int, input().split())
counter = 0
placeholder = 0
sodas=e+f
while sodas>=c:
    placeholder = int(sodas/c)
    counter += placeholder
    mod = sodas%c
    sodas = mod + placeholder
    
print(int(counter))

# 10 - 5
# 5 - 2
# 3 - 1
# 2 - 1
# 0