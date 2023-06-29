n = int(input())
numbers = list(map(int, input().split()))
negative_numbers = [i for i in numbers if i < 0]
print(-sum(negative_numbers))