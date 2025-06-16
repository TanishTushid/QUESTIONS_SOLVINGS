import cmath

z = complex(input())
r = abs(z)
theta = cmath.phase(z)
print(f"{r : .3f}")
print(f"{theta: .3f}")