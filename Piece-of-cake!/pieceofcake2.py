a, b, c = map(int, input().split())

remaining_width = max(b, a - b)
remaining_height = max(c, a - c)
volume = remaining_width * remaining_height * 4

print(volume)
