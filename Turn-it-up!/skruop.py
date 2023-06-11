n = int(input())
volume = 7
for i in range(n):
    s = input()
    if s == "Skru op!" and volume < 10:
        volume += 1
    if s == "Skru ned!" and volume > 0:
        volume -= 1
print(volume)
