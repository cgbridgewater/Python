#literal notation
from optparse import Values
from tkinter import N
from tkinter.messagebox import NO


person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
capitals = {} #create an empty dictionary


#literal notation
person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

#   print(capitals)    # print can be used to show the current dicionary, which now holds values


# playground

# Challenge yourself!

person = {"first_name": "Ada", "last_name": "Lovelace", "age": 42, "is_organ_donor": True}
# Create a another person dictionary called person_2 and print it to the terminal
person_2 = {"first_name": "Mike", "last_name": "Jordan", "age": 48, "is_organ_donor": False}
# print(person_2)

capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
# Add 2 key-value pairs to this dictionary.
capitals["usa"] = "Washington D.C."
capitals["cnd"] = "Toronto"

# print the capitals dictionary to see how it changed!
# print(capitals)



person = {
    "first_name": "Ada", 
    "last_name": "Lovelace", 
    "age": 42, "is_organ_donor": True
}

person["email"] = "alovelace@codingdojo.com"
# print(person)


if "email" not in person:
    person["email"] = "wrongemail@email.com"

# print(person["email"])


person_3 = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# Adds a new key value pair for email to person_3
person_3["email"] = "alovelace@codingdojo.com"
        
# Changes person_3's "last" value to "Bobada" <<--- same for adding a new value as it is to update a value!!
person_3["last"] = "Bobada"
print(person_3)


# if some_key in my_dictionary:
if "last" in person_3:
    # update the value
    person_3["last"] = "Lovelace"
print(person_3)


# VERIFIY AND REQUEST EMAIL REPLACE #
if "email" not in person_3:
    person_3["email"] = "newemail@email.com"
else:
    print("Would you like to replace your existing email?")


# ACCESSING VALUES #
print(person_3["first"])
full_name = person_3["first"] + " " + person_3["last"]
print(full_name)



# REMOVING VALUES #
value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything
print(capitals)


# USEFUL METHODS
#.clear()
        #- removes all elements from the dictionary

#.get(key,default=None)
        # A safe way to get a value, if the key might not exist. Returns the value for the specified key or None (or a value you specify) if the key is not in the dictionary.

#.update(pairs_to_update)
        #- Add and update multiple key-value pairs at once, by passing in another dictionary of the pairs to update and add.









# UPDATING AND ADDING VALUES #
countries_so_far = {"Mexico": 1, "Morocco": 1}
new_visits = ["Albania", "Mexico", "Togo", "Morocco"]
    
# To add Albania to the list
countries_so_far["Albania"] = 1
# To add 1 to the Mexico tally
countries_so_far["Mexico"] += 1 # Changes Mexico tally to 2!
# your code here to finish updating your travel log!