#1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

from multiprocessing.dummy import Array


num = 5
def countdown(num):
    for i in range(num,-1,-1):
        output.append(i)
    return output
output=[]
countdown(num)
print(output)

#2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(x):
    print(x)
    new_number = (x)+1
    return new_number

new_number = print_and_return(1)
print(new_number)


#3First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(list):
    return len(list) + list[0]

print(first_plus_length([1,2,3,4,5]))


# 4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(nums):
    for i in range(len(nums)):
        if i > nums[1]



        def values_greater_than_second(input):
    if(input[1] > len(input)):
        print("Too big")
    elif(input[0] < len(input)):
        print("Too small")
    else:
        print("Just right")

values_greater_than_second([2,13,7,54,2])