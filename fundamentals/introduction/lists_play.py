# list examples
from this import d


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

