cases = int(input())
for _ in range(cases):
    grades = list(map(int, input().split()))
    n = grades[0]
    grades = grades[1:]
    average = sum(grades) / n
    above_average = len([x for x in grades if x > average])
    print(f"{100 * above_average / n:.3f}%")
