import collections

c = collections


#  JAreina
a = c.Counter([2,2,8,5,1,2,3,4,5,8])
print(a)

b = 'en un lugar de la mancha'
print( c.Counter(b))


d = ['a',"b",'c',"c",'z']
print(c.Counter(d))


print("\n ::::::::: update counter::::::::::::\n")

e = c.Counter()
print(e)
e.update("hola hola")
print(e)

#JAreina

e.update( {"a": 100} )
print(e)
