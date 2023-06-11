dominant = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
not_dominant = {"A": 11, "K": 4, "Q": 3,
                "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}

N, value = input().split(" ")
sum = 0
for _ in range(int(N)*4):
    start = input()
    card = start[0]
    suit = start[1]
    if suit == value:
        if card in dominant.keys():
            sum += dominant[card]
    else:
        if card in not_dominant.keys():
            sum += not_dominant[card]
print(sum)
