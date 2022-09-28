# tuple examples
tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"
dog = ("Canis Familiaris", "dog", "carnivore", 12)


# conditional Example
ninja = {
    "first_name" : "Adrian",
    "last_name" : "Dion",
    "age" : 30,
    "favorite_languages" : ["Python", "C#", "JavaScript"]
}

if ninja["age"] > 30:
    print("that's old!")
elif ninja["age"] < 30:
    print("Whew, still young")
else:
    print("Right on!")



# conditional statements 
x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false   


# operational checks

# ==	Checks if the value of two operands are equal	
# 1 == 2 => False
# 1 == 1 => True

# !=	Checks if the value of two operands are not equal	
# 1 != 2 => True
# 1 != 1 => False

# >	Checks if the value of left operand is greater than the value of right operand	
# 1 > 2 => False
# 2 > 1 => True

# <	Checks if the value of left operand is less than the value of right operand	
# 1 < 2 => True
# 2 < 1 => False

# >=	Checks if the value of left operand is greater than or equal to the value of right operand	
# 1 >= 2 => False
# 2 >= 2 => True

# <=	Checks if the value of left operand is less than or equal to the value of right operand	1 <= 2 => True
# 2 <= 2 => True

# and	Checks that each expression on the left and right are both True	
# (1 <= 2) and (2 <= 3) => True
# (1 <= 2) and (2 >= 3) => False
# (1 >= 2) and (2 >= 3) => False

# or	Checks if either the expression on the left or right is True	
# (1 <= 2) or (2 >= 3) => True
# (1 <= 2) or (2 <= 3) => True
# (1 >= 2) or (2 >= 3) => False

# not	Reverses the true-false value of the operand	
# not True => False
# not False => True
# not 1 >= 2 => True
# not 1 <= 2 => False
# not (1 <= 2 and 2 >= 3)  => True
# not 1 <= 2 and 2 >= 3 => False

