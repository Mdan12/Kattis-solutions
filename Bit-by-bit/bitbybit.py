def checkforOR(item1, item2):
    if bit[item1]=="1" or bit[item2]=="1":
        return "1"
    elif bit[item1]=="?" or bit[item2]=="?": 
        return "?"
    else:
        return "0"
    
def checkforAND(item1, item2):
    if bit[item1]=="0" or bit[item2]=="0":
        return "0"
    elif bit[item1]=="?" or bit[item2]=="?":
        return "?"
    else:
        return "1"
bit = ["?"] * 32
n = int(input())

while n!=0:
    for i in range(n):
        instruction = list(input().split())
        if instruction[0] == "SET":
            bit[int(instruction[1])] = "1"
        elif instruction[0] == "CLEAR":
            bit[int(instruction[1])] = "0"
        elif instruction[0] == "OR":
            bit[int(instruction[1])] = checkforOR(int(instruction[1]),int(instruction[2]))
        elif instruction[0] == "AND":
            bit[int(instruction[1])] = checkforAND(int(instruction[1]),int(instruction[2])) 
            
    print(*reversed(bit),sep="")
    bit = ["?"] * 32
    n = int(input())