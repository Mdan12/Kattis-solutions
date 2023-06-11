summa = 0
integer = 1
counter = 0
number = int(input())
while summa <= number:
    summa += integer*integer
    integer += 2
    counter += 1
print(counter-1)
