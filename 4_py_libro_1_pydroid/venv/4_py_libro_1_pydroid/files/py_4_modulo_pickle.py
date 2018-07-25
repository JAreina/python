import pickle


#  escribir

name = ["mohit","bhaskar", "manish"]
skill = ["Python", "Python", "Java"]

pickle_file = open("emp1.dat","wb")


pickle.dump(name,pickle_file)
pickle.dump(skill,pickle_file)

pickle_file.close()

#  leer    JAreina

pickle_file = open("emp1.dat",'rb')

name_list = pickle.load(pickle_file)

skill_list =pickle.load(pickle_file)

print (name_list ,"\n", skill_list)
pickle_file.close()





pickle_file = open("emp2.dat",'wb')

leapx_team = {

     'z' : ["Mohit", "Ravender", "Himmat", "Robbin"],

     'zz' : ["Python","Data Analytic", "Information Security", "SAP"]

}


pickle.dump(leapx_team,pickle_file)

pickle_file.close() 


#  leer

pickle_file = open("emp2.dat",'rb')

aaa= pickle.load(pickle_file)


print (aaa ,"\n")
print('\n     :::::::::::::::: \n')
print(aaa['z'])
print(aaa['zz'])
pickle_file.close()