def star_battles():
    def check_surrounding(row, column):
        stars = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0<=row+i<10 and 0<=column+j<10:
                    if puzzle[row+i][column+j][1]=="*":
                        stars+=1
        if stars>1:
            return False
        return True

    nums = []
    dots = []

    score = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for _ in range(10):
        nums.append(input())

    for _ in range(10):
        dots.append(input())

    puzzle = [[] for _ in range(10)]

    for i in range(10):
        for j in range(10):
            puzzle[i].append([int(nums[i][j]), dots[i][j]])

    for i, k in enumerate(puzzle):
        for j, l in enumerate(k):
            if l[1] == "*":
                if not check_surrounding(i, j):
                    print("invalid")
                    return
                score[int(l[0])] += 1

    for z in score.values():
        if z != 2:
            print("invalid")
            return

    for i in range(10):
        row_counter = 0
        col_counter = 0
        for j in range(10):
            if puzzle[i][j][1] == "*":
                row_counter += 1
            if puzzle[j][i][1] == "*":
                col_counter +=1
        if row_counter != 2 or col_counter != 2:
            print("invalid")
            return

    print("valid")
    
star_battles()
