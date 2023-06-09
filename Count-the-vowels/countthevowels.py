s = input().lower()
vowels = "aeiou"
sum = 0
for i in s:
    if i in vowels:
        sum += 1
print(sum)
