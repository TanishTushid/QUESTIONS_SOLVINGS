import re

T = int(input())

invalid_repeaters = ['*+', '+*', '?+', '+?', '++', '**', '??']

for _ in range(T):
    pattern = input()
    if any(rep in pattern for rep in invalid_repeaters):
        print("False")
    else:
        try:
            re.compile(pattern)
            print("True")
        except re.error:
            print("False")