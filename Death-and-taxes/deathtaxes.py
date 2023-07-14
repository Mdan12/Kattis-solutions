import sys

shares = 0
avg_cost = 0
profit = 0

for line in sys.stdin:
    event = line.split()
    if event[0] == "buy":
        new_share = shares + int(event[1])
        avg_cost = (shares * avg_cost + int(event[1]) * int(event[2])) / new_share
        shares = new_share
    elif event[0] == "sell":
        shares -= int(event[1])
    elif event[0] == "split":
        shares *= int(event[1])
        avg_cost /= int(event[1])
    elif event[0] == "merge":
        shares //= int(event[1])
        avg_cost *= int(event[1])
    else:
        if int(event[1]) > avg_cost:
            print(shares * (int(event[1]) - (int(event[1]) - avg_cost) * 0.3))
        else:
            print(shares * int(event[1]))