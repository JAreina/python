print("\n for strings  :::::::::::::::::\n")
e = 'JAreina 2018'
for F in e:
    if (F == ' '):
        print('This is a space character')
    print ('LETRA -->', F)


print("\n for LISTAS :::::::::::::::::: \n")
B = ['A', 'B', 'C', 'D', 'E']
for b in B:
 print ("---->", b)


name = ['a', 'b', 'c', 'd', 'e', 'f']
for x in name:
    y = 0
    while y < 5:
        print(x)
        y = y + 1


print("\n break  :::::::: \n")

statement = 'JAreina'
for letter in statement:

 if letter == 'i':
     break
 print('-->>', letter)

print("\n  continue :::::::: \n")

for letter in statement:
 if letter == "J":
  continue
 print ("==>>", letter)