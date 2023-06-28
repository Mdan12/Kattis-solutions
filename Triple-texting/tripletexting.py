import textwrap

text = input()

string = textwrap.wrap(text,int(len(text)/3))
if string[0]==string[1] or string[0]==string[2]:
    print(string[0])
else:
    print(string[1])