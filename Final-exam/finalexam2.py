answers = []
counter = 0

for _ in range(int(input())):
    answers.append(input())

for i in range(0,len(answers)-1):
    if answers[i]==answers[i+1]:
        counter +=1
        
print(counter)