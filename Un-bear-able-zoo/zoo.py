animals = {}
counter = 1
while True:
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        animal = input().split()
        name = animal[len(animal)-1].lower()
        if name not in animals:
            animals[name]=1
        else:
            animals[name]+=1
    print(f"List {counter}:")
    counter+=1
    animals = dict(sorted(animals.items()))
    for i,k in sorted(animals.items()):
        print(i,"|", k)
    animals={}
    
        