from textwrap import wrap

s = input()
s_list = wrap(s, 3)
P = 13
K = 13
H = 13
T = 13
print(set(s_list))
if len(set(s_list)) != len(s_list):
    print("GRESKA")
else:
    for i in s_list:
        if i[0] == "P":
            P -= 1
        elif i[0] == "K":
            K -= 1
        elif i[0] == "H":
            H -= 1
        else:
            T -= 1
    print(P, K, H, T)
