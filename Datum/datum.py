from datetime import datetime
n, a = map(int, input().split())
dt = datetime(2009, a, n)

print(dt.strftime('%A'))
