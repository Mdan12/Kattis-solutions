n = int(input())
color_cups = {}
for i in range(n):
    first, second = input().split()
    if first.isdigit():
        first, second = second, int(first)/2
    color_cups[first] = int(second)


dict_sorted = dict(sorted(color_cups.items(), key=lambda item: item[1]))
for i in dict_sorted.keys():
    print(i)
