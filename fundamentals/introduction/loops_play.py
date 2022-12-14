# range exmples 

# only one argument  0 by default exits loop when 5 is reached



for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4


print("break")


# two arguments -- first number is start -- second is stop
for i in range(2, 7):
    print(i)
# Output: 2, 3, 4, 5, 6


print("break")



# three arguments -- first is start --  second is stop -- third is increment step
for i in range(2, 16, 3):
    print(i)

# Output: 2, 5, 8, 11, 14


# incementing
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8

# decrementing
for x in range(5, 1, -3):
    print(x)
# output: 5, 2


# playground demo 

for x in range(0, 10, 2):
    print(x)

# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2


# Challenge: Write a for loop to print all integers from 1 to 20, including 20.

for x in range(1,21):
    print(x)
# output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20


# looping through strings
for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'


# counting up in a list
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz


# playground demo 

countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Challenge 1: Fix the range!
for integer in range(0, len(countries)):
    #print(integer)    # Challenge 2: print the index here
    print(integer, countries[integer])   # Challenge 3: print the country here



countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Looping over values only...
for country in countries:
    print(country)
    # Challenge 4: print the country here


# While loops 
for count in range(0,5):
    print("looping =", count)
# output 
# looping = 0
# looping = 1
# looping = 2
# looping = 3
# looping = 4

count = 0
while count <= 5:
    print("looping - ", count)
    count += 1
# Output
# looping -  0
# looping -  1
# looping -  2
# looping -  3
# looping -  4
# looping -  5

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")
# # output
# 3
# 2
# 1
# Final else statement


# loop break example
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

for val in "string":
    if val == "o":   # break never occurs
        break
    print(val)
# output: s, t, r, i, n., g



# loop continue example
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i


y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1

