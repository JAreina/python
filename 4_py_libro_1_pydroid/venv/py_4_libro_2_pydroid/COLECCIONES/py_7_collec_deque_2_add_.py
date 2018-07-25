'''

deque is a double-ended queue, hence it means elements can
be added from either side or the deque can be populated from either side. In order to add
elements or populate the deque, we have four functions: extend(), append(),
extendleft(), and appendleft().
'''

import collections

d1 = collections.deque("JAreina")
print (d1)
d1.extend('EXTEND')
print ("after extend :\n", d1)
d1.append('APPEND')
print ("After append :\n",d1)
d1.extendleft("EXTEND_LEFT")

print ("after extend left\n ", d1)
d1.appendleft("APPEND_LEFT")
print ("after append left\n ", d1)