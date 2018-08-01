def compare_num_of_chars(string1):
 return len(string1)


word_list = ['Python', 'is', 'better', 'than', 'C']
word_list.sort()
print(word_list)
#['C', 'Python', 'better', 'is', 'than']
word_list = ['Python', 'is', 'better', 'than', 'C']
word_list.sort(key=compare_num_of_chars)
print(word_list)
#['C', 'is', 'than', 'Python', 'better']

