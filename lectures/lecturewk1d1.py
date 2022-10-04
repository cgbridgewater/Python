# primitive data types : boolean, string, int, float, numbers
# composite data types : dictionary, tuples, lists

age = 37
NAME = 'Aaron'
isCoder = True

id = 5

# print(NAME)

# print(isCoder + age)

#           0       1       2         3
fruit = ['dragon fruit', 'banana', 'kiwi']

# print(fruit[-2])

dictionary = {
    'word' : 'definition of the word.',
    'dog' : 'things that bark',
    'cat' : 'thigns that do not bark',
    'feet' : 'dogs barking'
}

southerner = {
    'name' : 'Aaron',
    'age' : '37',
    'hobbies' : ['fishing', 'motorcycling', 'sailing'],
    'pets' : [
        {
            'breed' : 'dog',
            'name' : 'Viktor',
        },
        {
            'breed': 'dog',
            'name': 'Samantha'
        }
    ],
    'isCoder' : True
}

x = 'name'
print(southerner[x])
print(southerner['name'])
print(x, 'this is ex')
print(southerner['pets'][1]['name'])


cat = ['saimaeeese', 'maincon', 'tiger'] #list

affirmative = ('si', 'hai', 'da') #tuple

myLists = (
    ['pizza', 'gin', 'chocolate'],
    ['study', 'lift', 'run', 'dog'],
)

# cat[1] = 'Mainecoon'
# print(cat)

# affirmative[1] = 'Hai'
# print(affirmative) #this doesnt work



foods = ['pizza', 'tamales', 'chocolate', 'steak']

# # for loop#
# for i in range(len(foods)):
#     print(foods[i])
# print('--space here--')
# # condensed for loop
# for food in foods:
#     print(food)

for i in range(len(foods)):
    print( str(i+1) + foods[i])
# add space by using comma instead of plus
for i in range(len(foods)):
    print( str(i+1) , foods[i])


dictionary = {
    'word' : 'definition of the word.',
    'dog' : 'things that bark',
    'cat' : 'thigns that do not bark',
    'feet' : 'dogs barking'
}

for key in dictionary:
    print(key, dictionary[key])

dictionary['ship'] = 'water vessel'


for key in dictionary:
    print(key, dictionary[key])


player = {
    'strength' : 100,
    'health' : 100,
    'weapons' : [],
}

for attribute in player:
    print(attribute, player[attribute])

name = 'chris'
age = 43

print(f'''i'm {name}, and {age} "years" old.''')

myString = '''
this
really
works
'''

print(myString)