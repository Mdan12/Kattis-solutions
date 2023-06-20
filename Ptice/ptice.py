from math import ceil

n = int(input())
Adrian = "ABC" * ceil(n/3)
Bruno = "BABC" * ceil(n/4)
Goran = "CCAABB" * ceil(n/6)
Score = {"Adrian":0, "Bruno":0,"Goran":0}
string = input()
for key, value in enumerate(string):
    if Adrian[key]==value:
        Score["Adrian"]+=1
    if Bruno[key]==value:
        Score["Bruno"]+=1
    if Goran[key]==value:
        Score["Goran"]+=1

placeholder=0
for i in Score.values():
    if i>placeholder:
        placeholder=i
print(k)
for j,k in Score.items():
    if k==placeholder:
        print(j)
        
