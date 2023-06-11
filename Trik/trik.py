a = input().upper()
listi = ["1", "2", "3"]
for i in a:
    if i == "A":
        listi[0], listi[1] = listi[1], listi[0]
    if i == "B":
        listi[1], listi[2] = listi[2], listi[1]
    if i == "C":
        listi[0], listi[2] = listi[2], listi[0]
print(listi.index("1")+1)
