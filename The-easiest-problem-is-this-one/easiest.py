import sys


def sumOfDigits(num):
    return sum(int(i) for i in str(num))


for line in sys.stdin:
    curr = int(line)
    if curr == 0:
        break
    match = sumOfDigits(curr)
    count = 11
    while sumOfDigits(count * curr) != match:
        count += 1
    print(count)
