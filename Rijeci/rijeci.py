A = 1
B = 0

for _ in range(int(input())):
    placeholder = A+B
    A=B
    B=placeholder
print(A, B)


# 1 0
# 0 1
# 1 1
# 1 2
# 2 3     B A B B A
# 3 5     B A B B A B A B
# 5 8     B A B B A B A B B A B B A
# 8 13    B A B B A B A B B A B B A B A B B A B A B