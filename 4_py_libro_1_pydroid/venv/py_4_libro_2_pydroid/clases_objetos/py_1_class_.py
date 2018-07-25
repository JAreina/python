class JAreina():
 	pass
 	

j = JAreina()
print(j)

j.nombre = "Juan"
j.edad = "joven"
j.confianza = True

print(j.edad)


'''
The __init__() method must begin and end with two consecutive underscores. Here
__init__ works as the class's constructor. When a user instantiates the class, it runs
automatically

'''


class Eva():
  aumento = 1.2 #variable clase
  contador = 0
  def __init__(self,first,last,pay):
    self.f_name = first
    self.l_name = last
    self.pay_amt = pay
    self.full_name = first+" "+last
    Eva.contador = Eva.contador +1
    
  def make_email(self):
    return self.f_name+"."+self.l_name+"@xyz.com"
    
  def incrementpay(self):
    self.pay_amt = int(self.pay_amt * self.aumento)
    return self.pay_amt
    
e1 = Eva('E', 'V', 60000)
e2= Eva('Ella', 'Evi',70000)
print (e1.full_name)
print(e2.full_name)

print(e2.make_email())

print(Eva.make_email(e2))

print(e1.incrementpay())

print('total Evas :', Eva.contador)

print("\n  ATRIBUTOS INSTANCIA \n")

print ("instance space ", e1.__dict__)


print("\n  ATRIBUTOS CLASE \n")
print ("class space ", Eva.__dict__)