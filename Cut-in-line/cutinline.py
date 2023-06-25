letters = []

for _ in range(int(input())):
    letters.append(input())

movement = []

for _ in range(int(input())):
    movement.append(input().split())
    
    
for i in movement:
    if len(i)==3:
        letters.insert(letters.index(i[2]),i[1])
    else:
        letters.remove(i[1])


for k in letters:
    print(k)