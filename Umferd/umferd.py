from collections import Counter

m = int(input())
n = int(input())

sum = m * n
counter = 0

for _ in range(n):
    count_letter = Counter(input())

    counter += count_letter["."]

print(counter / sum)
