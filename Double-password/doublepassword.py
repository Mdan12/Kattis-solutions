psw1 = input()
psw2 = input()
counter = 0
for i in range(4):
    if psw1[i]!=psw2[i]:
        counter+=1
print(2**counter)