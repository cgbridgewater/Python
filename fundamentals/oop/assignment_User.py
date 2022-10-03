#user class
from re import T


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_memeber = False
        self.gold_card_points = 0

    #display member info onto seperate lines
    # def 
#user print out
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
            print("Already a member")
            
        else:
            self.is_rewards_memeber = True
            self.gold_card_points += 200
        print("Thanks for signing up, enjoy is 200 points!!")


shopper_1 = User("Mike", "Jones", "Mike.Jones@email.com", 22)
shopper_2 = User("Joe","Shopper","Joe.Shopper@yahoo.com", 23)




    #spend points (self,amount) decrease points by specified amount (ensure points are sufficent to subtract them!! )




shopper_1.display_info()
print("----------------------------")
shopper_2.display_info()

print("----------------------------")
shopper_2.enroll()
shopper_2.display_info()