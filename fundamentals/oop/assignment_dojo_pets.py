class Ninja:
    def __init__(self, first_name, last_name, treats):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats


    def walk(self):
        print(f"Going out for a walk")
    

    def feed(self):
        print(f"Eating some snacks")

    def bathe(self):    
        print(f"Squeaky clean now!")





class Pet(Ninja): 
    def __init__(self, name, type, tricks, noise, pet_food, action):
        self.name = name
        self.type = type
        self.tricks = tricks
        self._noise = noise
        self.pet_food = pet_food
        self.action = action
        self.energy = 70
        self.health = 70

    def add_energy(self,amount):
        if self.energy == 100:
            print("Already at full energy")
        elif self.energy + amount >= 100:
            self.energy = 100
            print(f"health is now - {self.energy}")
        else:
            self.energy += amount
            print(f"energy is now - {self.energy}")
        return self

    def add_health(self,amount):
        if self.health == 100:
            print("Already at full health")
        elif self.health + amount >= 100:
            self.health = 100
            print(f"health is now - {self.health}")
        else:
            self.health += amount
            print(f"health is now - {self.health}")
        return self



    def sleep(self):
        self.add_energy(25)
        print(f"{self.name} is now taking a nap")


    def eat(self):
        super().feed()
        # self.noise()
        self.add_energy(5)
        self.add_health(10)
        # print(f"{self.name} is eating {self.pet_food}")

    def play(self):
        super().walk()
        self.add_health(5)
        print(f"{self.name} says 'Play Time'")

    def noise(self):
        print(f"{self.name} makes noises of joy {self._noise}")

    def say_no_food(self):
        print(f"After telling {self.name} he can't have any food because hes chonky. {self.name} gets mad and {self.action} you")




chris = Ninja("chris","B.","tacos")
cat = Pet("Wiskers", "cat", "jumps", "purrs", "kitty food","scratches")
dog = Pet("Sparky","dog","runs in circles", "barks","kibble", "bites")


print("check feed")
chris.feed()
print("check bathe")
chris.bathe()
print("check walk")
chris.walk()

print('''


''')


print('''----cat does eat---''')
cat.eat()
print('''----cat does play--''')
cat.play()
print('''----cat does sleep---''')
cat.sleep()
print('''----cat does bath---''')
cat.bathe()
print('''----cat does noise ---''')
cat.noise()
print('''----cat does action---''')
cat.say_no_food()


print('''


''')



print('''----dog does things now---''')
dog.eat()
dog.play()
dog.sleep()
dog.bathe()
dog.noise()
dog.say_no_food()