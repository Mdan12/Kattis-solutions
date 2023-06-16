string = input()
placeholder = None
for i in string:
    if not i == placeholder:
        print(i, end='')
    placeholder = i
