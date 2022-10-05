####  TYPES

##########   1. Encapsulation

class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")


##########  2. Inheritance

class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")



##########  3. Polymorphism

class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")
    def clean(self):
        print("Cleaning the froth!")


#######  4. Abstraction

class Barista:
    def __init__(self,name):
        self.name = name
        self.cafe = CoffeeM("Cafe")
    def make_coffee(self):
        self.cafe.brew_now()





##############################  INHERITANCE
### example of not connecting classes
class CheckingAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        # code
    def withdraw(self, amount):
        # code
    def write_check(self, amount):
        # code
    def display_account_info(self):
        # code

class RetirementAccount:
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.is_roth = is_roth
    def deposit(self, amount):
        # code - assess tax if necessary
    def withdraw(self, amount):
        # code - assess penalty if necessary
    def display_account_info(self):
        # code
    


class CheckingAccount(BankAccount):
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def withdraw(self,amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self



class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance = 0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth
    
    def withdraw(self,amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self
