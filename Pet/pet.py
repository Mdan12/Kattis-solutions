max_grade = 0
student = 1
for grade in range(5):
    grades = list(map(int, input().split()))
    scores = 0
    for i in grades:
        scores += i
    if scores > max_grade:
        max_grade = scores
        student = grade+1

print(student, max_grade)
