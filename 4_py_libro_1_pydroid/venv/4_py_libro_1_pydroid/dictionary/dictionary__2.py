list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c","d", "e"]
dict1 = {}
for i in range(len(list1)):
  dict1[list1[i]] = list2[i]
print (dict1)



print("\n   zip() ..............\n")


dict18={}
dict18 = dict([k for k in zip(list1,list2)])
print(dict18)