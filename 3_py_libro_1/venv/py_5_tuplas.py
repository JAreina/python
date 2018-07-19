'''
tuplas inmutables
'''

a = ( 1,2,3,4)
print(a)

try:
    a[0]= 1111
    a[len(a)+1] = "nuevo"

    print(a)
except:
    print("tuplas son inmutables")