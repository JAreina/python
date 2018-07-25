'''A Deque double-ended queue. It can be visualized similar to a hollow tube or pipe, which is
open at the both ends. Deques allows addition and removal of elements from either ends. It
will be more clear with examples:'''
import collections
de = collections.deque('JAreina')
print ('deque:', de)
print( 'Lenght :', len(de))
print ('left end:', de[0])
print( 'right end:', de[-1])
de.remove('a')
print( 'After removing:', de)