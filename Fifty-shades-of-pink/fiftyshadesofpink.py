n = int(input())
sum = 0
for i in range(n):
    color = input()
    if "pink" in color.lower() or "rose" in color.lower():
        sum += 1
if sum == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(sum)
