# Lazy Evaluation
# when dealing with large amounts of data , you do not want to process all the data before using the results.

# generatirs

# generators operate on chunks of data and pause (yield) in between calls
# can be used to store variables on every stop

# the yield stops the loop until it is called again
def count():
    n = 0
    while True:
        n += 1
        yield n

counter = count()
print(counter)
print(next(counter))
print(next(counter))
print(next(counter))
print('------------------------------------------')

# using the fibanacci generator for this

def fib():
    first = 0
    last = 1
    while True:
        first, last = last , first + last
        yield first
f = fib()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

# using a for loop for fibanacci 
print('--------------------------------------')
f = fib()
for x in f:
    print(x)
    if x > 12:
        break


# generator comprehension
#creating one liners
# comprehension itererates and ouputs all data (python sequence)
# by storing data in an object it compresses it

list_o_nums = [x for x in range(100)]
gen_o_nums = (x for x in range(100))
print(list_o_nums)
print("------------------")
# seeing the size diffrence
import sys
print(sys.getsizeof(list_o_nums))
print('-----')
print(sys.getsizeof(gen_o_nums))