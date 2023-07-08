sum = 0
counter = 0
penalty = {}
while True:
    a = input()
    if a == "-1":
        break
    num, letter, ans = a.split()
    print(ans)
    if ans == "wrong":
        if letter not in penalty:
            penalty[letter] = 0
        penalty[letter] += 20
    elif ans == "right":
        counter+=1
        if letter in penalty:
            sum+=int(penalty[letter])+int(num)
        else:
            sum+=int(num)    
            
print(counter, sum)