h, m = input().split()
h = int(h)
m = int(m)-45
minutes = 0
if m < 0:
    minutes = 60+m
    h = h-1
if m > 0:
    minutes = m
if h < 0:
    h = 23
print(h, minutes)
