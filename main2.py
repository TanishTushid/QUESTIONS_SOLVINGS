# tuples are hashable 

coords = set()
a = (1,2)
b = (2,2)

coords.add(a)
coords.add(a)
coords.add(a)
coords.add(b)
print(coords)
