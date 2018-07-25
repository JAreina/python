from collections import defaultdict#JAreina

def func():
        return "JAreina"
        
        
game = defaultdict(func)

print(len(game))
print(game)
game["A"]= "bbbb"
game["B"] = "cccc"
print (game)
print (game["A"])
print (game["B"])
print (game["C"])#JAreina

'''
function func acts as a default_factory function. We have
assigned game["A"]= "bbbb", where  "A" is the key. If key is new (not found in the
dictionary "game"), then defaultdict does not give an error; instead, it returns the
default value, which is returned by the default_factory() function
'''


print(" \n   con lambda  ::::::::::::\n")

gam = defaultdict(lambda : "JAreina")
gam["A"]= "xxxx"
gam["B"] = "yyyy"#JAreina
print (gam)
print( gam["A"])
print (gam["B"])
print (gam["C"])




print(" \n   con int  ::::::::::::\n")

gam2 = defaultdict(int)
gam2["A"]= "xxxx"
gam2["B"] = "yyyy"
print (gam2)
print( gam2["A"])#JAreina
print (gam2["B"])
print (gam2["C"])



print(" \n   con int  con value distinto de cero::::::::::::\n")


game2 = defaultdict(int)
list1 = ['cricket', 'badminton', 'hockey' 'rugby', 'golf', 'baseball' ,
'football']

for each in list1:
        game2[each]= game2[each]+100
print (game2)

#JAreina


print(" \n   con tuplas::::::::::::\n")

game3 = defaultdict(list)

tuple_list_county =  [('US', 'Visconsin'), ('Germany', 'Bavaria'), ('UK',
'Bradfordshire'), ('India', 'punjab'), ('China', 'Shandong'), ('Canada',
'Nova Scotia')]
#JAreina
print (game3["any_value"])
for k,v in tuple_list_county:
	     game3[k].append(v)
print (game3)