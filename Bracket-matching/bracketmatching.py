input()
word = input()
while len(word)>0:
    if "{}" not in word and "[]" not in word and "()" not in word:
        print("Invalid")
        exit()
    word = word.replace("()","")
    word = word.replace("[]","")
    word = word.replace("{}","")
print("Valid")