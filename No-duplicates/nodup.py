n = input().lower().split()
if len(n) == len(set(n)):
    print('yes')
else:
    print('no')
