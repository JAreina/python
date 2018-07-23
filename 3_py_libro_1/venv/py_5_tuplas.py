'''
tuplas inmutables
'''

a = ( 1,2,3,4)
print(a)

try:
    print(len(a))
    a[0]= 1111

    a[len(a)+1] = "nuevo"
    # JAreina
    print(a)
except:
    print("tuplas son inmutables")