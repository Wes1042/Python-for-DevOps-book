# This is a dict refresher

# How dictionaties work
values = {'first': 'wesley', 'last': 'T'}
print("Won't you come home {first} {last}?".format(**values))

print('\n')

#How to create a format to display easy loops
text = "|{0:>22}||{0:<22}|"
print(text.format('0','0'))

# easy loops format
text2 = "|{0:<>22}||{0:><22}|"
print(text2.format('0', '0'))


#fstring usage
a = 1
b = 2
print(f"\na is {a}, b is {b}. Adding them results in {a+b}")

#fstring with value expression (regex)
count = 43
print(f"|{count:5d}")

#fstring with value expression pt2
padding = 10
print(f"|{count:{padding}d}")

# using an import to get similar fumction to bash script 
from calendar import c
from string import Template
greeting = Template("$hello, Mark Anthony")
print(greeting.substitute(hello="Bonjour"))

#understanding dictionaries
map = dict()
print(type(map))

kv_list = [['key-1', 'value-1'], ['key-2', 'value-2']]
print(dict(kv_list))

#creating dict using curly braces
map = {'key-1': 'value-1', 'key-2': 'value-2'}
print(map)

#accesing values of key using square brackets
print(map['key-1'])
print(map['key-2'])

# setting values to a key in dict
map['key-3'] = 'value-3'
print(map)

#overwritting values
map['key-1'] = 13
print(map)

# if key isn't defined , a KeyError will appear
#print(map['key-4'])

# Checking if the key is in our dict
if 'key-4' in map:
    print(map['key-4'])
else:
    print('key-4 not there')

# fstring version
key = 'key-1'
if key in map:
    print(f" {map[key]}")
else:
    print(f'{key} is not there...')

# using the get() method. 
print(map.get('key-4', 'default-value'))

# using del to remove a key-value
del(map['key-1'])
print (map)

#using keys() method to see all dict_keys objects
print(map.keys())

#using values() method to see all dict_values objects
print(map.values())
#using for loop to print values corresponsing to keys
for key, value in map.items():
    print(f"{key}: {value}")


# understanding iterations 
letters = 'abcde'
# mapping individual letters to their upper-case representations
cap_map = {x: x.upper() for x in letters}
print(cap_map['b'])