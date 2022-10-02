class User:
    def __init__(self,first_name,last_name,age, email):
        self.firt_name = first_name
        self.last_name = last_name
        self.name = f"{first_name} {last_name}" #is this okay???
        self.age = age
        self.email = email

    def greeting(self):
        print(f"Hello, Thank you for signing up {self.firt_name}!")

chris = User("Chris", "Bridgewater", 43, "SomeEmail@aol.com")
chris.greeting()
print(f"Hello, my name is {chris.name}.")

adrien = User("Adrien","Dion",39,"adion@codingdojo.com")
sadie = User("Sadie", "Flick", 35, "sflick@codingdojo.com")

sadie.greeting()
adrien.greeting()
chris.greeting()