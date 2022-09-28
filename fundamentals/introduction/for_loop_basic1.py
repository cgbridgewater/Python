# 1 - Basic - Print all integers from 0 to 150.

import numbers


for INTEGER in range(151):
    print(INTEGER)

print(" ")
print(" ")
# 2 - Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for mult_5 in range(5,1001,5):
    print(mult_5)

print(" ")
print(" ")
# 3 - Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for counting in range(1,101):
    if counting % 10 ==0:
        print("Coding Dojo")
        continue
    if counting % 5 ==0:
        print("Coding")
        continue
    else: print(counting)

print(" ")
print(" ")
# 4 - Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum_of_numbers = sum(range(1,500001))
print(sum_of_numbers)

print(" ")
print(" ")
# 5 - Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for dec_by_4 in range(2018,1,-4):
    print(dec_by_4)

print(" ")
print(" ")
# 6 - Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 3
highNum = 9
mult = 3

for flexCounter in range(lowNum,highNum+1):
    if flexCounter % mult ==0:
        print(flexCounter)
        continue
    else: continue