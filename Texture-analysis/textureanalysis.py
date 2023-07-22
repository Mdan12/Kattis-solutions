from collections import Counter
text = input()
counter = 1
while text!= "END":
    if len(Counter(text))==1:
        print(f"{counter} EVEN")
    else:   
        othertext = "*"
        i=1
        while text[i]!="*":
            othertext+=text[i]
            i+=1
        othertext = othertext * int(len(text)/len(othertext)) + "*"
        if othertext == text:
            print(f"{counter} EVEN")
        else:
            print(f"{counter} NOT EVEN")
    counter+=1
    text = input()

