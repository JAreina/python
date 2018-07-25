'''

The OrderedDict is a subclass of the dictionary and it remembers the order in which the
elements are added:
'''
import collections

print ('Regular Dictionary')
d = {}

d['g']= "aaaa"
d['a']= 'SAS'
d['bbbb']= 'PYTHON'
d['c']= 'R'

for k,v in d.items():
        print (k, ":",v)
        
        
print( '\n Ordered dictionary')

d1 = collections.OrderedDict()
d1['a']= 'SAS'
d1['b']= 'PYTHON'
d1['c']= 'A'

for k,v in d1.items():
        print (k, ":",v)