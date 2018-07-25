import collections

co = collections.Counter()

file_txt = open("3.txt","r")
for line in file_txt:
        co.update(line.lower())
print( co)