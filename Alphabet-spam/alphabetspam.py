word = input()
word_length = len(word)

whitespace = 0
lowercase = 0
uppercase = 0
symbols = 0
for letter in word:
    if letter.isupper():
        uppercase += 1
    elif letter.islower():
        lowercase += 1
    elif letter == "_":
        whitespace += 1
    else:
        symbols += 1

print(f"{whitespace/word_length:.16f}")
print(f"{lowercase/word_length:.16f}")
print(f"{uppercase/word_length:.16f}")
print(f"{symbols/word_length:.16f}")
