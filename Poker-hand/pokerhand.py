from collections import Counter

cards = list(input().split())
suits = []
suits_string = "CDHS"
for i in cards:
    suits.append(i[:1])
counts = Counter(suits)
print(max(counts.values()))
