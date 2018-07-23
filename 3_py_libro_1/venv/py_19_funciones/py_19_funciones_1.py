
def funcion_publica() :
    print("soy la función pública")

funcion_publica()

print("\n")

def saludate(nombre):
    print("hola",nombre)
    return


saludate("Juan")

print("\n")

def calculateBattingAverage(atBats, hits, walks):
 battingAverage = hits/(atBats-walks)
 print(battingAverage)

calculateBattingAverage(200,54,12)
calculateBattingAverage(300,108,6)

print("\n")


def greetTwoPeople(person1, person2):
#This function greets two people
 print("Greetings", person1)
 print("Hello, How are you?", person2)
 return


greetTwoPeople("Mark", "Brett")
greetTwoPeople(person1="Mark", person2="Brett")


print("\n")


def calculateBa (atBats, hits, walks):
 ba = hits/(atBats-walks)
 print(ba)
 return


calculateBa(walks=25, atBats=317, hits=67)


print("\n argumentos por defecto :::::: \n")

def employeeInformation(name="Juan", ssn="182", position=""):
 print("Name:", name)
 print("Ssn:", ssn)
 print("Position:", position)
 return



employeeInformation(position="founder")



print("\n otros argumenots pasados :::::::: \n" )

def moreEmployee(name, *other):
 print("Employee Info:")
 print("Name:", name)
 for var in other:
  print(var)
 return

#JAreina
moreEmployee("Mark Lassoff", "Founder", "9-1-2009", "206")



print("\n  return   ::::::::::::::::\n")

def calculateDogYears(humanYears):
 dogYears= humanYears * 7
 print("Dog Years:", dogYears)
 return


print(calculateDogYears(9.5))



def calculateDogYears2(humanYears):
 dogYears= humanYears * 7
 return dogYears

myDogYears = calculateDogYears2(9.5)
print("AÑOS PERROS:", myDogYears)