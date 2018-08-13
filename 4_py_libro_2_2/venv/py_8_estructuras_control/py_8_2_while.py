u, v, x, y = 0, 0, 100, 30
while x > y:
 u = u + y # 30
 x = x - y # 70
 if x < y + 2:
  print(y)
  v = v + x
  x = 0
 else:

  print("y",y)
  v = v + y + 2 #32
  x = x - y - 2 #38
  print("else",v ," ..",x)
print(u, v,x,y)