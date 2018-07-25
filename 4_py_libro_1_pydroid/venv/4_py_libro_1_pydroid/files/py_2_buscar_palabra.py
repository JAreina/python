word = input("busca una palabra\n ")
word = word.lower()
file_txt = open("jareina.txt", "r")
count = 0
for each in file_txt:
    if word in each.lower():
        count = count+1
    
#  JAreina 
# operador ternario   
vez = "veces" if count >1 else "vez"

print (" ", word ,"se encuentra ",count,vez)