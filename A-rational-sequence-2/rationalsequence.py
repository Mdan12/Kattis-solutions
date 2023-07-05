import re

for _ in range(int(input())):
    string = input()
    split_string = re.split(r'/| ', string)
    num = split_string[0]
    numerator = int(split_string[1])
    denominator = int(split_string[2])
    counter=0
    while numerator>1 or denominator>1:
        if numerator==1:
            numerator=denominator
            denominator-=1
        else:
            numerator-=1
            counter+=1
        counter+=1
    print(counter)
    
    
