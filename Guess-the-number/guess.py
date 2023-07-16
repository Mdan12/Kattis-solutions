import sys

low = 1
high = 1000


while True:
    guess = (low+high)//2
    print(guess)
    sys.stdout.flush()
    
    response = input()

    if response == "lower":
        high = guess - 1
    elif response == "higher":
        low = guess + 1
    elif response == "correct":
        break