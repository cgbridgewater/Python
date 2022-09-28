# list examples
# from this import d
from audioop import reverse


ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []



# combining lists
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)


drawers = ["documents", "envelopes", "pens"]
    
# access the drawer with index of 0 and print value
print(drawers[0])  #prints documents
# access the drawer with index of 1 and print value
print(drawers[1]) #prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2]) #prints pens
    
# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]
    
# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]


# play around with the drawers!
drawers = ['documents', 'envelopes', 'pens']

# Print the second value from the list (envelopes)
print(drawers[1])
# Change "pens" to "useless manuals"
drawers[2] = 'useless manuals'
# Change the first value to whatever is the second value
drawers[0] = drawers[1]
print(drawers)
# What should the list look like now?
print(drawers)
# Print the list! Does it match your prediction?


nums = [1,2,3,4,5]
nums.append(99)
print(nums)
#the output would be [1,2,3,4,5,99]
nums.append(102)
print(nums)

words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']
    
# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']

print('playing here')
print(words[2:5])

my_list = [1, 'Zen', 'hi']
print(len(my_list))
# output
3

my_list = [1,5,2,8,4]
my_list.pop()
print(my_list)
# output:
# [1,5,2,8]

# common list methods
my_list = [1,51,22,18,34]
print(sorted(my_list))
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)



# playground practice#
some_nums = [44,56,2,3,12,19,6]
print("Get started by writing your own code!")
print("origional numbers = ", some_nums)
# Some optional challenges to assess and refine your understanding:

print(len(some_nums))
# Print the length of the list.
print(sorted(some_nums))
# Use antoher python built-in function and print the result.
some_nums.pop()
print(some_nums)
# Remove an item from the list. Remember to verify that it was removed.
some_nums.reverse()
print(some_nums)
# Utilize a method from the documentation and print the result.