#user class

class User:

    def __init__(self, first_name, last_name, email, age):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.age = age
            self.is_rewards_memeber = False
            self.gold_card_points = 0

    def display_info(self):
        print(f'''{self.first_name}
{self.last_name}
{self.email}
{self.age}
{self.is_rewards_memeber}
{self.gold_card_points}''')

    #enroll member and turn member status to true and 200 points
    def enroll(self):
        if self.is_rewards_memeber == True:
            print(f"{self.first_name}, No need to enroll. You're already a member")
        else:
            self.is_rewards_memeber = True
            self.gold_card_points += 200
            print(f"{self.first_name}, Thanks for signing up. Enjoy these 200 free points!!")


    #spend points (self,amount) decrease points by specified amount (ensure points are sufficent to subtract them!! )
    def spend_points(self,amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
            print(f"{self.first_name}, Thank you for your purchase. Your new Gold Card Points balance is {self.gold_card_points}")
        else:
            print("Sorry, but this purchase requires more gold card reward points")


#new user creations
shopper_1 = User("Mike", "Jones", "Mike.Jones@email.com", 22)
shopper_2 = User("Joe","Shopper","Joe.Shopper@yahoo.com", 23)
shopper_3 = User("Johnny","Law","ImComingForYou@aol.com", 55)


#shopper info displays test
print("shopper 1 sign up----------------------------")
shopper_1.display_info()
print("shopper 2 sign up----------------------------")
shopper_2.display_info()
print("shopper 3 sign up----------------------------")
shopper_3.display_info()

print(" ")
print(" ")
print(" ")
print("begin enrollments----------------------------")
#shopper enrollment test
shopper_1.enroll()
shopper_1.display_info()
print("----------------------------")
shopper_2.enroll()
shopper_2.display_info()
print("----------------------------")
shopper_3.enroll()
shopper_3.display_info()
print("----------------------------")



#shopper points spending test
shopper_1.spend_points(50)
shopper_1.display_info()

print("----------------------------")
shopper_2.spend_points(80)
shopper_2.display_info()

print("----------------------------")
shopper_3.spend_points(40)
shopper_3.spend_points(40)
shopper_3.spend_points(40)
shopper_3.spend_points(40)
shopper_3.spend_points(40)
shopper_3.spend_points(40)
shopper_3.display_info()
print("----------------------------")



print("-------------test double enrollment------------")
shopper_1.enroll()
shopper_1.display_info()
shopper_1.spend_points(199)
