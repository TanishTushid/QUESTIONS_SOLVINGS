import re
pattern = re.compile(r'^[+-]?(\d+\.\d+|.\d+)$')
n = int(input())
for _ in range(n):
    s = input()
    if pattern.match(s):
        try:
            float(s)
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)