#for loops through dictionaries -
# if we want each key....

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(each_key)
# output: name, language

# same as 
# for var in whatever_dict:
#   print(var)


# if we want each value....
my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python




capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc


# dictionary madness demo video
# List of dictionaries
users = [
    {"first" : "Ada", "last" : "Lovelace"}, # index 0
    {"first" : "Alan", "last" : "Turing", "birthday" :"June 13, 1913"}, # index 1
    {"first" : "Eric", "last" : "Idle"}, # index 2
]

print(users[0]["last"])
first_user= {'first': 'Ada', 'last': 'Lovelace'}
print(first_user["last"])


#dictionary containing lists
resume_data = {
    "skills" : ["front-end", "back-end", "database"],
    "languages" : ["Python", "Javascript"],
    "hobbiees" : ["rock climbing", "knitting"]
}



# NESTING #

# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}


#ACCESSING VALUES IN NESTED DICTIONARIES 
print(users[0]["last"]) # prints Lovelace


print(resume_data["skills"][1])
print(users[2]["first"])





#multi-layer nesting

#print the first listed language of the second resume

resumes = [
    {#dictionary 1
        "skills" : ["front-end", "back-end", "database"],#list 1
        "languages" : ["Python", "Javascript"],#list 2
        "hobbies" : ["rock climbing", "knitting"]#list 3
    },
    {#dictionary 2
        "skills" : ["front-end", "back-end", "database"],#list 1
        "languages" : ["Python", "Javascript"],#list 2
        "hobbies" : ["rock climbing", "knitting"]#list 3
    },
    {#dictionary 3
        "skills" : ["front-end", "back-end", "database"],#list 1
        "languages" : ["Python", "Javascript"],#list 2
        "hobbies" : ["rock climbing", "knitting"]#list 3
    },
]

#    (variable[dict]["list"][location])
print(resumes[1]["hobbies"][0:2])

