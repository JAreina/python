file_input = open("motivation.txt",'w')
file_input.write("Never give up")
file_input.write("\nRise above hate")
file_input.write("\nNo body remember second place")
file_input.close()



list1 = ["Blood sweat and respect\n",
 "The first two you given\n"
 "The last you earn\n"
 "Give it Earn it"]
text_file = open("a.txt", 'w')
text_file.writelines(list1)
text_file.close()



print(" añadir")
file_input = open("motivation.txt",'a')
file_input.write("\nNever give up\n")
file_input.write("\nRise above hate\n")
file_input.write("No body remember second place")
file_input.close() 


'''
The "r+" opens a file for reading and writing. This mode places the pointer at the
beginning of the file.
The "w+" opens a file for reading and writing. If the file doesn't exist, then a new file is
created.  If the file exists, then the file is overwritten.
The "a+" opens a file for appending and reading. If the file doesn't exist, it creates a new
file. If the file already exists, the pointer is placed at the end of the file.
'''