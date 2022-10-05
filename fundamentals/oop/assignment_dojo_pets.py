class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
    self.first_name = first_name
    self.last_name = last_name
    self.treats = treats
    self.pet_food = pet_food
    self.pet = pet

    def walk(self, pet):
        print(f"Taking {pet} out for a walk")
    
    def feed(self, pet, treats):
        print(f"Giving {pet} on some {treats}")

    def bathe(self, pet):    
        print(f"{pet} is now squeaky clean!")
    
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method




class Pet(Ninja): 
    def __init__( name , type , tricks ):



    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound
