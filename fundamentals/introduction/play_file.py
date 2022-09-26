is_hungry = True
has_freckles = False

age = 35 # storing an int
weight = 160.57 # storing a float

name = "Joe Blue"

dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
# dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11 



float = 3.14

number = 4

sum = number + int(float)
print(type (sum), sum)

print(type(24))
print(type(3.9))
print(type(3j))


# int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
# print(int_to_float)
print(float_to_int)
print(int_to_complex)
# print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

import random
print(random.randint(2,50)) # provides a random number between 2 and 50
