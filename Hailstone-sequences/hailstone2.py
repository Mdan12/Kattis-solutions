numbers = []
placeholder = int(input())
while placeholder!=1:
    numbers.append(placeholder)
    if placeholder%2!=0:
        placeholder=3*placeholder+1
    else:
        placeholder = placeholder/2
print(numbers)
print(len(numbers)+1)