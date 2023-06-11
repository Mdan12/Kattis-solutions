problems = list(input().split(";"))
sum = 0
for i in problems:
    if i.__contains__("-"):
        lower, higher = map(int, i.split("-"))
        sum += higher-lower
    sum += 1

print(sum)
