'''Python facilitates you to create your own data type. In the Python collection, namedtuple
gives you a special feature to create your own data type. In the C language, you might have
used struct to create your own data type.
'''

'''
collections.namedtuple(typename, field_names[, verbose=False][,
rename=False])


Let's try to understand the syntax of namedtuple. In the preceding syntax:
The typename defines the name of the new data type
The field_names can be a sequence of strings such as ['x', 'y'] or string in
which values are whitespaced or , separated
If verbose is False, then the class definition would not be printed, it is a good
idea to keep it False
If rename is False, then the invalid field names are automatically replaced with
positional names, for example, 'def, age, empid' is converted to '_0 ,
age, empid' because def is a keyword
'''

import collections
print( "\n___________________________\n")

employee = collections.namedtuple('empleado','name, age, empid')
record1 = employee("Hamilton", 28, 12365 )
print ("Record is ", record1)
print ("name of employee is ", record1.name)
print ("age of employee is ", record1.empid)
print( "type is ",type(record1))

print("\n")
#JAreina
print( "\n___________________________\n")

'''
Adding values and creating a dictionary 
 how to add list values into namedtuple and how
to make dictionary from namedtuple:'''

empleado= collections.namedtuple('empleado','name, age, empid')
list1 = ['BOB', 21, 34567]
record2 =empleado._make(list1)
print (record2)
print ("\n")
print (record2._asdict())


'''
 by using  _make, we can add a list into a namedtuple and by using _asdict we can
create dictionary of namedtuple
'''

print( "\n___________________________\n")


''''
 consider a scenario where you would like to replace a value from namedtuple. Like
tuple, the namedtuple is also immutable. But you can use the  _replace function to
replace the value from namedtuple:'''

employee3= collections.namedtuple('empleado3','name, age, empid')
record1 = employee3("Marina", 28, 12365 )
print ("Record is ", record1)
print( "\n")
print  (record1._replace(age= 25))

print ("Record is ", record1)

record1 = record1._replace(age= 25)
print( "Record is ", record1)
print( "\n___________________________\n")
