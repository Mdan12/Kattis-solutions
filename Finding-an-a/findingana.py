s = input()
a = 0
for i, k in enumerate(s):
    if k == "a":
        a = i
        break
print(s[a:len(s)])
