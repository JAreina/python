'''

NUMBERS
Integers—1, –3, 42, 355, 888888888888888, –7777777777
 Floats—3.0, 31e12, –6e-4
 Complex numbers—3 + 2j, –4- 2j, 4.2 + 6.3j
 Booleans—True, False
'''

import math

import cmath

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

print("\n ............\n")

print( 5 + 2 - 3 * 2)
#1
print( 5 / 2 ) # floating point result with normal division
#2.5
print( 5 / 2.0) # also a floating point result
#2.5
print(5 // 2 )# integer result with truncation when divided using '//'
#2
print(30000000000) # This would be too large to be an int in many languages
#30000000000
print(30000000000 * 3)
#90000000000
print(30000000000 * 3.0)
#90000000000.0
print(2.0e-8) # Scientific notation gives back a float
#2e-08
print(3000000 * 3000000)
#9000000000000
int(200.2)
#200
int(2e2)
#200
float(200)


print("   FUNCIONES ")
'''
abs, divmod, cmp, coerce, float, hex, int, long, max, min, oct,
pow, round
'''

print( "funciones modulo math")

'''
The math module provides the following functions and constants:

acos, asin, atan, atan2, ceil, cos, cosh, e, exp, fabs, floor, fmod,
frexp, hypot, ldexp, log, log10, mod, pi, pow, sin, sinh, sqrt, tan,
tanh


----------------
advanced numeric operations:  NumPy
 www.scipy.org
 
 
'''


print( "   COMPLEX NUMBERS")


'''
Complex numbers are created automatically whenever an expression of the form nj is
encountered, with n having the same form as a Python integer or float. j is, of course,
standard engineering notation for the imaginary number equal to the square root of
–1


 functions, which can operate on complex numbers, are provided in
the cmath module:
acos, acosh, asin, asinh, atan, atanh, cos, cosh, e, exp, log, log10,
pi, sin, sinh, sqrt, tan, tanh.
'''

numeroComplejo = 232+2j
print( numeroComplejo.real, numeroComplejo.imag)

print(3 + 2j - (4+4j)) #(-1-2j)
print((1+2j) * (3+4j))#(-5+10j)



print(cmath.sqrt(-1))


'''
The None value

In addition to standard types such as strings and numbers, Python has a special basic
data type that defines a single special data object called None

representa un valor vacío, por ejemplo el retorno de una función que no retorna nada

'''


print(not None)
print(None)

