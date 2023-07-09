lines = int(input())

for i in range(lines):
    text = input()
    if text.startswith("simon says"):
        print(" ".join(text.split()[2:]))
    else:
        print()