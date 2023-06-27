player = int(input())
n = int(input())
timer = 0
for _ in range(n):
    time, char = input().split()
    timer += int(time)
    if timer>=210:
        break
    if char=="T":
        player+=1
player = player%8
if player ==0:
    print("8")
else:
    print(player)