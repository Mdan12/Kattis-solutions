def queensgame():
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    for _ in range(n):
        row, col = map(int, input().split())
        arr[row][col] = 1

    cols = [[] for _ in range(n)]
    rows = [[] for _ in range(n)]
    fdiag = [[] for _ in range(n + n - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -n + 1

    for x in range(n):
        for y in range(n):
            cols[x].append(arr[y][x])
            rows[y].append(arr[y][x])
            fdiag[x+y].append(arr[y][x])
            bdiag[x-y-min_bdiag].append(arr[y][x])

    for i in range(n):
        if cols[i].count(1)>1:
            return "INCORRECT"
        if rows[i].count(1)>1:
            return "INCORRECT"
    for i in range(len(fdiag)):
        if fdiag[i].count(1)>1:
            return "INCORRECT"
        if bdiag[i].count(1)>1:
            return "INCORRECT"
    return "CORRECT"
print(queensgame())