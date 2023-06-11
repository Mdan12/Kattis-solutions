no_code = True
for i in range(1, 6):
    code = input()
    if "FBI" in code:
        print(i)
        no_code = False
if no_code:
    print("HE GOT AWAY!")
