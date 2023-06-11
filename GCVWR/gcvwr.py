g, t, n = map(int, input().split())
w = list(map(int, input().split()))

max_weight = (g-t)*0.9
sum_of_items = sum(w)
print(int(max_weight-sum_of_items))
