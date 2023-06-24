terrace, n = map(int, input().split())
counter=0
placeholder = 0

for _ in range(n):
    path, people = input().split()
    if path == "enter":
        if placeholder+int(people)<=terrace:
            
            placeholder+=int(people)
        else:
            counter +=1
    else:
        placeholder-=int(people)
print(counter)