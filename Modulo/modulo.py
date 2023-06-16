sum = []
for _ in range(10):
    number = int(input())
    modulo = number % 42
    sum.append(modulo)
print(len(set(sum)))
