for _ in range(int(input())):
    num = input()
    if num == "P=NP":
        print("skipped")
    else:
        num = num.split("+")
        print(int(num[0])+int(num[1]))