n = int(input())
teams = int(input())
placeholder = int(teams % n)
teams_in_room = int(teams/n)
for _ in range(n):
    if placeholder > 0:
        print((teams_in_room+(int(placeholder/placeholder)))*"*")
        placeholder = placeholder - 1
    else:
        print(teams_in_room*"*")
