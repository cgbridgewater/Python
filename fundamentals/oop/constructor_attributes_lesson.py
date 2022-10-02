#declare a class and give it a name User

class User:
    def __init__(self):
        self.first_name = "ada"
        self.last_name = "lovelace"
        self.age = 42


print("hello")

user_ada = User()
user_2 = User()

print(user_ada.first_name)
print(user_2.last_name)