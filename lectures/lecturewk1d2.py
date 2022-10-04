
def countdown(num):
    print(f"input: {num}")
    output=[]
    for i in range(num,-1,-1):
        print(f"i:{ i}")
        output.append(i)
    print(f"output: {output}")
    print(f"length: {len(output)}")
    return output

countdown(5)

num = 5


# print(countdown(num))

def countdown2(input):
    # print(f"length: {len(output)}")
    return list(range(num,-1,-1))
print(countdown2(5))




def goldilocks(input):
    if(input[0] > len(input)):
        print("Too big")
    elif(input[0] < len(input)):
        print("Too small")
    else:
        print("Just right")

goldilocks([2,13,7,54,2])


# oooooor, compact but a tougher read and trouble shoot

def goldilocks(input):
    a=input[0]
    b=len(input)
    print("just right" if a == b else "Too Big" if a > b else "Too Small")


goldilocks([2,13,7,54,2])

# LECTURE STARTS HERE!!!!
# LECTURE STARTS HERE!!!!
# LECTURE STARTS HERE!!!!
# LECTURE STARTS HERE!!!!
# LECTURE STARTS HERE!!!!

people = [
    {
        'id' : 1,
        'name': "Bob",
        'height': 5.8,
        'gender': "male",
        'money': 100,
        'age':24,
        'email' : 'bob@aol.com',
    },
    {
        'id' : 2,
        'name': "Stacy",
        'height': 5,
        'gender': "female",
        'money': 10,
        'age':30,
        'email' : 'stacy16@aol.com',
    },
    {
        'id' : 3,
        'name': "Jessica",
        'height': 4.6,
        'gender': "female",
        'money': 90,
        'age':52,
        'email' : 'jessbess@aol.com',
    },
    {
        'id' : 4,
        'name': "Billy",
        'height': 6.1,
        'gender': "male",
        'money': 120,
        'age':43,
        'email' : 'billyTheKid@aol.com',
    },
    {
        'id' : 5,
        'name': "Davey",
        'height': 5.9,
        'gender': "male",
        'money': 50,
        'age':19,
        'email' : 'crocket@aol.com',
    },
    {
        'id' : 6,
        'name': "Heather",
        'height': 5,
        'gender': "female",
        'money': 10,
        'age':46,
        'email' : 'Heathers@aol.com',
    },
    {
        'id' : 7,
        'name': "Jennie",
        'height': 5.1,
        'gender': "female",
        'money': 40,
        'age':18,
        'email' : 'jenjen@aol.com',
    },
    {
        'id' : 8,
        'name': "Sara",
        'height': 5.2,
        'gender': "female",
        'money': 80,
        'age':35,
        'email' : 'rocknroll@aol.com',
    },
    {
        'id' : 9,
        'name': "David",
        'height': 5.6,
        'gender': "male",
        'money': 35,
        'age':28,
        'email' : 'TheMuppetsMadeMeDoIt@aol.com',
    },
]


# ask for parameters
# receive arguments

# Get user by id
def get_user_by_id(id):
 for person in people:
    if person['id'] == id:
        return person

print(get_user_by_id(9))


# Get user by email

def get_user_by_email(email):
 for person in people:
    if person['email'] == email:
        return person

print(get_user_by_email(9))


# Get all males

def get_male_users():
    male_users = []
    for person in people:
        if person['gender'] == 'male':
            male_users.append(person)
        return male_users

print(get_male_users())

# get all females

def get_female_users():
    female_users = []
    for person in people:
        if person['gender'] == 'female':
            female_users.append(person)
        return female_users

print(get_female_users())


# too much work and making two functions, when you can have just one!! see below


# create user log in with verifying email and making new ID

def create_new_user(name, age, gender, email, height, money):
    if get_user_by_email(email):
        return False
    id =len(people) + 1
    people.append(
        {
            'id' : id,
            'name' : name,
            'age' : age,
            'gender' : gender,
            'email' : email,
            'height' : height,
            'money' : money,
        }
    )
    return True

create_new_user( 
            name = 'Billybob Ray',
            age = 22,
            gender = 'male',
            email = 'Billybob@bigtruckin.inc',
            height = 6.3,
            money = '2',
)


# cleaner version

def create_new_user_2(data):
        if get_user_by_email(data['email']): return False
        data['id'] = len(people) + 1
        people.append(data)
        return True

user_submitted_form_data = {
            'name' : 'Johny B Goode',
            'age' : 36,
            'gender' : 'male',
            'email' : 'jb@aol.net',
            'height' : 6,
            'money' : '20',
}

create_new_user_2(user_submitted_form_data)
print(people)
#get users by age, gender, and income