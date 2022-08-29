import re
# TODO 
# write a python function that takes a name as an argument and print that named

def name(input):
    print(f"Your name is {input}")
name("wes")

print("----------------------------------------")

# Write a Python function that takes a string as an argument and prints whether it is upper- or lowercase.
def classification(string):
        lower = re.findall(r'[a-z]' , string)
        upper = re.findall(r'[A-Z]' , string)


        for letter in range(0,len(string)) :
        
            if string[letter] in lower:
                print(string[letter] +  " This is a lower")
            elif string[letter] in upper:
                print(string[letter] +" this is a upper") 
            else:
                print('There was no match')
classification('HAHAHAHddd')


# Write a list comprehension that results in a list of every letter in the word smogtether capitalized.
def comprehension(string):
    my_list = []
    for letter in range(0,len(string)):
        cap_letter = string[letter].upper()
        my_list.append(cap_letter)
    print(my_list)

comprehension("smogtether")


# Write a generator that alternates between returning Even and Odd.

def odd_even(max_range):
    
    odd = []
    even = []
    
    for x in range(max_range):
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    print(odd)
    print('-----------------------------------')
    print(even)

odd_even(100)