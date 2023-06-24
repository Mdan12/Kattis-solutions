word = set(input())
guesses = input()
x = 10
for guess in guesses:
    if guess in word:
        word.remove(guess)
        if len(word)==0:
            print("WIN")
            break
    else:
        x-=1
        if x==0:
            print("LOSE")
            break