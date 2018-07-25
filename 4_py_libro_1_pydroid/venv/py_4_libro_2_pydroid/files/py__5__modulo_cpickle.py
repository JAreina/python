import cPickle as pickle

# no me funciona en android

name = ["mohit","bhaskar", "manish"]
skill = ["Python", "Python", "Java"]

pickle_file = open("emp111.dat","wb")
pickle.dump(name,pickle_file)
pickle.dump(skill,pickle_file)
pickle_file.close()