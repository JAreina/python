import calendar
cal=calendar.month(2018, 7)
print(cal)


print("\n funciones \n")


a = calendar.firstweekday()
print(a)

print("\n año bisiesto\n")
#JAreina
print(calendar.isleap(2018))

calendar.setfirstweekday(1)
print(calendar.firstweekday())

print(calendar.weekday(2018,5,23))


#   http://docs.python.org.