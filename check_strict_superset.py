main_set = set(input().split())
N = int(input())

is_strict_superset = True

for _ in range(N):
    other_set = set(input().split())

    if not (main_set > other_set):
        is_strict_superset = False
        break
print(is_strict_superset)