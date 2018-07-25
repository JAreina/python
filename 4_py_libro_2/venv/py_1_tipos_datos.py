'''

NUMBERS
Integers—1, –3, 42, 355, 888888888888888, –7777777777
 Floats—3.0, 31e12, –6e-4
 Complex numbers—3 + 2j, –4- 2j, 4.2 + 6.3j
 Booleans—True, False
'''

import math

a = 4 + 4 * 10
print(a)
b = a / 3
print(b)
c = a // 3
print(c)
d = 1010101010 ** 3
print(d)
# complex
e = (3+2j) ** (2+3j)
print(e)
print("parte real {} --- parte imaginaria {} ".format(e.real,e.imag))


print(round(3.3333))
print(math.ceil(3.3333))


f = True     # 1
g = False    # 0
h = f * 2
print(h)
i = g * 2
print(i)