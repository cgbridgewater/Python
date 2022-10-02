class User:
    def __init__(self,first_name,last_name,age):
        self.firt_name = first_name
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print(f"Hello, my name is {self.firt_name}!")

chris = User("Chris", "Bridgewater", 43)
chris.greeting()