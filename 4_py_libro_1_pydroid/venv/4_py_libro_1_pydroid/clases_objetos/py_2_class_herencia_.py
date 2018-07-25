
class SuperEva():
	soy_super= " SOY SUPEREVA"
	
	def __init__(self,felicidad):
	   	self.felicidad = felicidad


class Eva(SuperEva):
  aumento = 1.2 #variable clase
  contador = 0
  def __init__(self,first,last,pay,felicidad):
    #constructor padre
    SuperEva.__init__(self,felicidad)
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
    
e1 = Eva('E', 'V', 60000,True)
e2= Eva('Ella', 'Evi',70000,True)
print (e1.full_name)
print(e2.full_name)

print(e2.make_email())

print(Eva.make_email(e2))

print(e1.incrementpay())

print('total Evas :', Eva.contador)

print(e2.soy_super)

print("FELICIDAD",e2.felicidad)