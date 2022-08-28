def double(input):
    '''double input'''
    return input*2

print(type(double))


def triple(input):
    '''Triple input'''
    return input*3
#Iterates through the predefined functions 

functions = [double, triple]
for function in functions:
    print(function(3))

print ('############################')
#sorting using the first entry
items = [[ 0, 'a', 2 ], [5,'b',0],[2,'c',1]]
print(sorted(items))

def second(item):
    '''return second entry'''
    return item[1]

print(sorted(items,key=second))

# The top code ^ is to chunky so you would use lamda to simplify

print(sorted(items,key=lambda item: item[1]))
print(sorted(items, key=lambda item: item[2]))

#CAUTION: ^^ lamda can be poorly documented when used