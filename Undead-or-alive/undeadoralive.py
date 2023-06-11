a = input()
if ":)" in a and ":(" not in a:
    print("alive")
if ":(" in a and ":)" not in a:
    print("undead")
if ":)" in a and ":(" in a:
    print("double agent")
if ":)" not in a and ":(" not in a:
    print("machine")
