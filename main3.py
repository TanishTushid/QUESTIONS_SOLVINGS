
import sys

data = sys.stdin.read().splitlines()

x, k = map(int, data[0].split())
poly = data[1]

print(eval(poly, {"__builtins__": None}, {"x": x}) == k)
