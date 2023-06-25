counter = 0
for i in range(int(input())):
    battle = input()
    if "CD" not in battle:
        counter+=1
print(counter)