n = int(input())
for i in range(n):
    word1 = input()
    word2 = input()
    print(word1)
    print(word2)
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            print(".", end="")
        else:
            print("*", end="")
    print("\n")
