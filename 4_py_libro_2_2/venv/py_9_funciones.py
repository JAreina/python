def funct1(x, y, z):
 value = x + 2*y + z**2
 if value > 0:
  return x + 2*y + z**2
 else:
  return 0


u, v = 3, 4
print("funct1", funct1(u, v, 2))
print("funct1",funct1(u, z=v, y=2))


def funct2(x, y=1, z=1):
 return x + 2 * y + z ** 2


print("funct2",funct2(3, z=4))

def funct3(x, y=1, z=1, *tup):
 print((x, y, z) + tup)

funct3(2)
funct3(1, 2, 3, 4, 5, 6, 7, 8, 9)


def funct4(x, y=1, z=1, **dictionary):
 print(x, y, z, dict)

funct4(1, 2, m=5, n=9, z=3)
