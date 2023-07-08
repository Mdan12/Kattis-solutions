basketballs = input()
A = 0
B = 0
for i in range(0,len(basketballs),2):
    if basketballs[i]=="A":
        A+=int(basketballs[i+1])
    else:
        B+=int(basketballs[i+1])
    if A>=11 and A-B>=2:
        print("A")
        break
    if B>=11 and B-A>=2:
        print("B")
        break