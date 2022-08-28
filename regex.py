from distutils.filelist import findall
import re
from unicodedata import name

cc_list = '''
Ezra Koenig <ekoenig@vpwk.com>,
Rostam Batmanglij <rostam@vpwk.com>,
Chris Tomson <ctomson@vpwk.com,
Bobbi Baio <bbaio@vpwk.com,
'''
# Built in python search
print('Rostam' in cc_list)
# Regex search
print(re.search(r'Rostam' , cc_list))

if re.search(r'Rostam' , cc_list):
    print('Found Rostam')

#Using character sets , helps identify more than one group 

# locates based on set defined letters 
print(re.search(r'[R,B]obb[i,y]', cc_list))
# locates based on any letter ranging from a-z
print(re.search(r'Chr[a-z][a-z]', cc_list))

# using + and {} to define specification
# + <- matches one or more of the same character
# it picks up the first iteration as the same item
print(re.search(r'[A-Za-z]+' , cc_list))
# {} <- matches based on character specification
# Itereates on the deadukt value which is the first one
print(re.search(r'[A-Za-z]{6}' ,cc_list))

# matching a email address
print(re.search(r'[A-Za-z]+@[a-z]+\.[a-z]+' , cc_list))

# Character classes aka wildcards
# \w <- [a-zA-Z0-9_] (any words)
# \d <- [0-9] (any digits)

print(re.search(r'\w+', cc_list))

# a better example of email address lookup
print(re.search(r'\w+\@\w+\.\w+' ,cc_list))

# Groups
# groups are sections with parenthesis . can be used to 
# determine a specific value
print(re.search(r'(\w+)\@(\w+)\.(\w+)' , cc_list))
matched = re.search(r'(\w+)\@(\w+)\.(\w+)' , cc_list)
print(matched.group(0))
print(matched.group(1))
print(matched.group(2))
print(matched.group(3))
print("-------------------------------------------")
#setting names to groups
matched = re.search(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)',cc_list)
print(matched.group('name'))
print('----------------------------------------------------------------------------')
#This prints out the sentence appended with group ^^
print(f'''name: {matched.group("name")}
secondary Level Domain: {matched.group("SLD")}
Top Level Domain: {matched.group("TLD")}''')

#------------------------------------------
# the 'findall' finds our regex in the whole input instead of one
print("---------------------------------------------")
matched = re.findall(r'\w+\@\w+\.\w+', cc_list)
print(matched)
print('---------------------------------------------------')
#matching and storring in in groups
matched = re.findall(r'(\w+)\@(\w+)\.(\w+)', cc_list)
print(matched)
print('--------------------------------------------------------')
# sets x as the first group and stores it in names, prints out all names
names = [x[0] for x in matched]
print(names)




#--------------------------------------------------------------------

# Understanding what iterators are
# ITERATORS
# 'finditer' is an object that process text until it finds a match and stops
# passing it to the next function
print('-------------------------------------')
matched = re.finditer(r'\w+\@\w+\.\w+', cc_list) 
print(matched) 
print(next(matched))
print(next(matched))
print(next(matched))
# this can be used in a for loop
print ('------------------------------')
matched = re.finditer("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)" , cc_list)
# the grouping stores it in a dictionary
for m in matched:
    print(m.groupdict())

print('----------------------------------------')

# understanding substitution
#substitution can be used to substitute matched words

print(re.sub("\d", "#", "The passcode you entered was 09876"))
# logically : for every digit , replace with # 

users = re.sub("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", "\g<TLD>.\g<SLD>.\g<name>", cc_list)
# logically: for every email group , replace with what \g says in order
print(users)

print('----------------------------------------------------------------------------------------')
# Understanding compiling
# regex takes a lot of performance
# by using regex as an object it can be used constantly

# its setting a preset regex as an object so it can be used over again
# can be used with loops in conditionals


regex = re.compile(r'\w+\@\w+\.\w+')
print(regex.search(cc_list))
