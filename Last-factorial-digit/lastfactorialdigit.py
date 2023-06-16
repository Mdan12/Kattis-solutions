from math import factorial

n = int(input())
for _ in range(n):
    factorial_number = int(input())
    last_factorial = str(factorial(factorial_number))[-1]
    print(last_factorial)
