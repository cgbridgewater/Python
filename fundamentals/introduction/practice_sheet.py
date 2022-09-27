# Practice Challenge: Correct the errors!
first_name = "Alana "
last_name = "Da Silva "
age = 36
profession = "Software Developer"
years_experience = 5

greeting = "Hello my name is "+ first_name + last_name

print(greeting)
# Desired output: Hello my name is Alana Da Silva


print(f"I am {age} years old") 

print("I am {} years old".format(age)) 
# # Desired output: I am 36 years old

print(f"I work as a {profession}")
# new way above old below
print("I work as a {}.".format(profession))
# # Desired output: I work as a Software Developer.

exp_string = "I have worked in the field for " + str(years_experience) + " years."
print(exp_string)
# # Desired output: I have worked in the field for 5 years.

print("I started in the field when I was " + str(age - years_experience) + " years old.")
# # Desired output: I started in the field when I was 31 years old.


# old style more similar to java and c+
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

x = "hello world"
y = "678" + "3245"
print(x.title())
# output:
# "Hello World"

print(x.upper())

print(x.isalnum())

print(y.isalnum())

print(x.join(y))