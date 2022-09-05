

# reading the whole text
file_path = 'bookofdreams.txt'
open_file = open(file_path, 'r')
text = open_file.read()
print(len(text))


print(text[56])
print(open_file)

open_file.close()

print('########################################')
# Reading lines using the os method

open_file = open(file_path, 'r')
text = open_file.readlines()
print(len(text))
print(text[100])

open_file.close()

# Using for loops 
with open(file_path, 'r') as open_file:
    text = open_file.readlines()

print(text[101])
print(open_file.closed)


# understanding \n characters using while loop
file_path = 'bookofdreamsghos00lang.pdf'
with open(file_path, 'rb') as open_file:
    btext = open_file.read()

print(btext[0])

print(btext[:25])
# opens with line-ending conversion ^^^^





# Using development environment 
#setting enironment variables


# direnv sets up envirnment variables and application run times in the file name .envrc
# setting environments variable STAGE to PROD
# setting environment variable TABLE_ID to token-storage-1234 
# in a file where python using open will write
print('#########################################')
text = '''export STAGE=PROD
export TABLE_ID=token-storage-1234'''

with open('.envrc', 'w') as opened_file:
    opened_file.write(text)

# printing the environments
print('printing envirnments')
env = '.envrc'
with open(env , 'r') as env_file:
        count = 0
        for line in env_file:
            count += 1
            print(line.strip())


      
env_file.close()

    

# The open function creates a file that doesnt all ready exist
# the "a" flag appends to the orginal file at the end of the file
# to write binary data , you use the b flag that stands for binary
# appending to binary only works for pdf and related files
# ex "wb" = write binary and "ab" = append binary


