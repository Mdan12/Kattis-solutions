Y, P = input().split()
vowels = ["a","i","o","u"]
if Y[len(Y)-1]=="e":
    print(Y,"x",P,sep="")
elif Y[len(Y)-1] in vowels:
    print(Y[:len(Y)-1],"ex",P,sep="")
elif Y[len(Y)-1]=="x" and Y[len(Y)-2]=="e":
    print(Y,P,sep="")
else:
    print(Y,"ex",P,sep="")