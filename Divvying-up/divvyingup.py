_ = input()
prize = sum(list(map(int, input().split())))
if prize%3==0:
    print("yes")
else:
    print("no")