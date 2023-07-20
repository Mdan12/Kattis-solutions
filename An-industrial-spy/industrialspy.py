import itertools

def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

for _ in range(int(input())):
    
    n = input()
    counter = set()
    nums = list(n)

    for r in range(1, len(nums) + 1):
        all_permutations = itertools.permutations(nums, r)
        for tpl in all_permutations:
            num = int(''.join(tpl))
            if isPrime(num):
                counter.add(num)

    print(len(counter))

