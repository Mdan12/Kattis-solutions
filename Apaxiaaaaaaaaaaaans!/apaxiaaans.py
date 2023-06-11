word = input()
placeholder = ""
for i in word:
    if placeholder != i:
        print(i, end="")
    placeholder = i
