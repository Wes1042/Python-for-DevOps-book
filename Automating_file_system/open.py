from cgitb import text


file_path = 'bookofdreams.txt'
open_file = open(file_path, 'r')
text = open_file.read()
print(len(text))

print(text[56])
print(open_file)

open_file.close()