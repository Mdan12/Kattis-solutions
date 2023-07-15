import sys

Keys = {"A#":"Bb", "C#":"Db", "D#":"Eb", "F#":"Gb", "G#":"Ab"}
counter = 1
for line in sys.stdin:
    key = line.split()
    if len(key[0]) == 1:
        print(f"Case {counter}: UNIQUE")
    for i, k in Keys.items():
        if i == key[0]:
            print(f"Case {counter}: {k} {key[1]}")
        if k == key[0]:
            print(f"Case {counter}: {i} {key[1]}")
    counter+=1