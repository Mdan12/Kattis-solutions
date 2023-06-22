victory_cards = {"Province": 8, "Duchy": 5, "Estate": 2}
treasure_cards = {"Gold": 6, "Silver": 3, "Copper": 0}

g, s, c = map(int, input().split())

value = g * 3 + s * 2 + c
print_list = []

for i, j in victory_cards.items():
    if value >= j:
        print_list.append(i)
        break

for k, l in treasure_cards.items():
    if value >= l:
        print_list.append(k)
        break

if len(print_list) > 1:
    print(print_list[0], "or", print_list[1])
else:
    print(print_list[0])
