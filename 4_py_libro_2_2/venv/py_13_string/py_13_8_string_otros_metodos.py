import string

# isdigit(), isalpha() , islower, isupper,

x = "123"
x.isdigit()
#True
x.isalpha()
#False
x = "M"
x.islower()
#False
x.isupper()
#True


print(string.whitespace)
print(string.digits)
print(string.hexdigits)
print(string.digits)
print(string.octdigits)



# sumar

a = "ho" + "la"

# replicar
b = "--" * 10


'''

upper 

       Converts a string to uppercase --------------------------------x.upper()

lower 
      Converts a string to lowercase --------------------------------x.lower()

title 
      Capitalizes the first letter of each word in a string -------- x.title()

find, index 
       
      Searches for the target in a string ---------------------x.find(y) --- x.index(y)

rfind, rindex 
      
      Searches for the target in a string, from the end of the string  ---- x.rfind(y) --- x.rindex(y)

startswith, endswith 

      Checks the beginning or end of a string for a match ----- x.startswith(y) ----x.endswith(y)

replace 

      Replaces the target with a new string ---------------------- x.replace(y, z)

strip, rstrip, lstrip

       Removes whitespace or other characters from the ends of a string -------- x.strip()

encode 

       Converts a Unicode string to a bytes object  ----------------------x.encode("utf_8")


'''