str1 = "abcd ABCD"

a =str1.ljust(19, "#")

b =str1.rjust(29, "#")


print(a)
print(b)


c = str1.center(16, "#")

print(c)