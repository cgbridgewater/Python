
class Ninja:
    def __init__(self, first_name, last_name, treats):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        # self.pet = cat


    def walk(self):
        print(f"Going out for a walk")
    

    def feed(self, treats):
        print(f"Eating some {treats}")

    def bathe(self, pet):    
        print(f"squeaky clean now!")



    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method




class Pet(Ninja): 
    def __init__(self, name, type, tricks, noise, pet_food):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.pet_food = pet_food
        self.energy = 70
        self.health = 70

    def add_energy(self,amount):
        if self.energy == 100:
            print("Already at full energy")
        else:
            self.energy += amount
            print(f"energy is now - {self.energy}")
        return self

    def add_health(self,amount):
        if self.health == 100:
            print("Already at full health")
        else:
            self.health += amount
            print(f"health is now - {self.health}")
        return self



    def sleep(self):
        self.add_energy(25)
        print(f"{self.name} is now taking a nap")


    def eat(self):
        super().feed(self.pet_food)
        # self.noise()
        self.add_energy(5)
        self.add_health(10)
        # print(f"{self.name} is eating {self.pet_food}")

    def play(self):
        super().walk()
        self.add_health(5)
        print(f"{self.name} says 'Play Time'")

    def noise(self):
        print(f"{self.name} makes noises of joy {self.noise}")

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound



chris = Ninja("chris","B.","snacks")
cat = Pet("Wiskers", "cat", "jumps", "purrs", "kitty food")


# chris.pet = cat
# chris.feed()

print('''----cat eat---''')
cat.eat()


print('''


---chris walk---''')
chris.walk()


print('''


---cat play---''')
cat.play()

# cat.eat()