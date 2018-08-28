import string

a = "               hola \t\t"
print(a.strip())
print(a)

print(a.rstrip())
print(a.lstrip())

print(string.whitespace)
print(" \t\n\r\v\f")

b = "aaaaabbbbbccccHOLA"
print(b)
print(b.strip("a"))
print(b.strip("HOLA"))