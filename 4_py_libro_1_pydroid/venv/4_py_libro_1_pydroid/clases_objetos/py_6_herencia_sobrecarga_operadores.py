class X():
   def __init__(self,first,last,pay):
      self.f_name = first
      self.l_name = last
      self.pay_amt = pay
      self.full_name = first+" "+last
      
   def make_email(self):
      return self.f_name+ "."+self.l_name+"@xyz.com"
      
      # sobrecsrga operador +
   def __add__(self,other):
     result = self.pay_amt+ other.pay_amt
     return result
      
      # sobrecsrga operador  >
   def __gt__(self,other):
      return self.pay_amt>=other.pay_amt
      
   def __str__(self):
        str1 = "instance belongs to "+self.full_name
        return str1  
      
      #sobrecarga  #
   def __len__(self):
        return len(self.f_name+self.l_name) 
        
        
a = X('JAreina', 'CCC', 60000)
b = X('Juan', 'DDD',70000)
print( a+b)


print( "a > b ?  ",a > b)

print(a)
print(len(a))