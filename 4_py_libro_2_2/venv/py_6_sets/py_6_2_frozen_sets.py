'''

frozensets are immutable and hashable, they can
be members of other sets:
'''


x = set([1, 2, 3, 1, 3, 5])
z = frozenset(x)
print(z)

#frozenset({1, 2, 3, 5})
try:
 z.add(6)
except:
    print("no se le puede add al frozenset")


x.add(z)
print(x)
#{1, 2, 3, 5, frozenset({1, 2, 3, 5})}