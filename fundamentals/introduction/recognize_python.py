num1 = 42  #variable statment
num2 = 2.3  #variable statment
boolean = True  # boolean initialized, variable statement
string = 'Hello World'  #variable statment, string initialized


pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# list initialized, variable decleration

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# variable decleration, dictionary initilized

fruit = ('blueberry', 'strawberry', 'banana')
# tuple initilized, variable decleration

print(type(fruit))
# log statement, type check

print(pizza_toppings[1])
# log statment, list access value

pizza_toppings.append('Mushrooms')
# list add value

print(person['name'])
# log statment, dicionary access value

person['name'] = 'George'
# dictionary change value

person['eye_color'] = 'blue'
# dictionary change value


print(fruit[2])
# log statement, tuple access value


if num1 > 45: 
    print("It's greater")
else:
    print("It's lower")
# conditional, if, evaluation, log statement, else, log statement


if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# conditional, if, length check, string, evaluation, log statment, else if, length check, string, evaluation, log statment, else, log statement



for x in range(5):
    print(x)
# for loop, increases until reaches 5, log statement


for x in range(2,5):
    print(x)
# for loop, increase from 2 until reaches 5, log statement


for x in range(2,10,3):
    print(x)
# for loop, increase from 2 until reaches 10 in increments of 3, log statement


x = 0  
while(x < 5):
    print(x)
    x += 1
#variable declaration, while, evaluation, log statement, incrementing


pizza_toppings.pop()
# list, delete value


pizza_toppings.pop(1)
# list, access value, delete value indexed


print(person)
# log dictionary

person.pop('eye_color')
# dictionary delete value

print(person)
# log dictionary

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# looping through list, if, evaluate, continue, loge statement, if, evaluate, stop/break the loop


def print_hello_ten_times():
    for num in range(10):
        print('Hello')
# declare function, for loop from 0 until 10, console log


print_hello_ten_times()
# call function


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
# declare function, for loop from 0 until x, console log 


print_hello_x_times(4)
# call function, argument of 4



def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
# declare function, for loop from 0 up to 10 times, console log 


print_hello_x_or_ten_times()
# call function, goes to 10

print_hello_x_or_ten_times(4)
# call function goes to 4


"""
Bonus section
"""

print(num3)


num3 = 72
# variable statement


fruit[0] = 'cranberry'
# tuples change value


print(person['favorite_team'])
# log statement, add value


print(pizza_toppings[7])
# log statement, access list item


print(boolean)
# log statment, data type


fruit.append('raspberry')
# tuples change value


fruit.pop(1)
# tuples delete value