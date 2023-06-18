n = int(input())
for _ in range(n):
    simon_text = input()
    if "Simon says " in simon_text:
        simon_improved = simon_text.replace("Simon says ", "")
        print(simon_improved)
