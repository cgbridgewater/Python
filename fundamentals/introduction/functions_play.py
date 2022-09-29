
# returns end Function
# print statements are for debugging

# SYNTAX

def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8



# PARAMETERS AND ARGUMENTS
# ask for parameters
# receive arguments


def say_hi(name):
    print("Hi, " + name)

# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')
# Output 
# Hi, Michael
# Hi, Anna
# Hi, Eli

# adding a return - returns are needed if the result is to be used outside of the function. The result will be stored to be returned when requested

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

#sum 1 would be 10, sum 2 would be 5, sum 3 would be 15


# playground challenge

# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

def full_name(first, last):
    name = first + " " + last 
    return name

name = full_name("Eddie", "Aikau")
print(name) # should print Eddie Aikau

# Challenge 2: 
#   Call the function again using your own name and print the results!

name = full_name("Chris", "B-Dub")
print(name)

name = full_name("JimBob", "Ray")
print (name)




# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)
be_cheerful()    # output: good morning (repeated on 2 lines)
be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

