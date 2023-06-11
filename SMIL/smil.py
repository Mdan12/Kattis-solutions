s = input()
for count, value in enumerate(s):
    if value == ":" or value == ";":
        try:
            if s[count+1] == ")":
                print(count)
            elif s[count+1] == "-" and s[count+2] == ")":
                print(count)
        except:
            continue
