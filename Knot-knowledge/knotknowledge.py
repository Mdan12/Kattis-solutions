n = int(input())
listi = list(map(int, input().split()))
listi1 = list(map(int, input().split()))
for i in listi:
    if i not in listi1:
        print(i)
