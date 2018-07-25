num = int(input(" ESCRIBE \t\n UN NÚMERO DEL 1 AL 5\t\n"))

if num > 5:
         s= 'he dicho menor de 5'
elif num < 1:
          s= 'he dicho mayor de 1'
else:
          s= 'buen número {}'.format(num)
print (s)