numbers = list(map(int, input().split()))
letters = input()
someday = sorted(numbers)
for i in letters:
    if i == "A":
        print(someday[0], end=" ")
    elif i == "C":
        print(someday[2], end=" ")
    else:
        print(someday[1], end=" ")
