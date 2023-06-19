inside_out = set()

for _ in range(int(input())):
    enter_exit, name = input().split()
    text = ""
    if enter_exit == "entry":
        if name in inside_out:
            text = name+" entered (ANOMALY)"
        else:
            text = name+" entered"
        inside_out.add(name)
    else:
        if name in inside_out:
            text = name+" exited"
        else:
            text = name+" exited (ANOMALY)"
        if name in inside_out:
            inside_out.remove(name)
    print(text)
        