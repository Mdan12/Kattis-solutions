from statistics import median

n = int(input())
my_day = list(map(int, input().split()))
first_colleague = list(map(int, input().split()))
second_colleague = list(map(int, input().split()))
for i in range(n):
    check_list = [my_day[i], first_colleague[i], second_colleague[i]]
    print(median(check_list), end=' ')