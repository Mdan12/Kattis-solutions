s = input()
n = input()
numbers = [n[i:i+3] for i in range(0, len(n), 3)]
for i in numbers:
    print(s[int(i)-1], end="")
