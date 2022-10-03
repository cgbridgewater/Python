#CHECKING ACCOUNT
class BankAccount_Checking:
    accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount_Checking.accounts.append(self)

#tested and working
    def account_info(self):
        print(f"Your Checking Account balance is ${self.balance}")
        print(f"Your Savings Account balance is ${self.savings.balance} with an interest rate of {self.savings.int_rate}%")
        return self


#tested and working
    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited ${amount}")
        return self

#tested and working
    def yield_interest(self):
        temp = self.balance
        if self.balance > 0:    
            interest = self.balance * 1 + self.int_rate - temp
            print(f"Your interest is ${interest}")
        return self



#testing!!!
    def transfer_to_savings(self,amount):
        if BankAccount_Checking.can_transfer(self.balance, amount):
            temp = self.balance
            self.balance = self.balance - amount
            self.savings += amount
            print(f"You transfered ${amount} to savings")
        else:
            print(f"Insufficient Funds available to complete transfer")
        return self

    @staticmethod
    def can_transfer(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


#testing







#tested and working
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount_Checking.can_withdraw(self.balance,amount):
            temp = self.balance
            self.balance -= amount
            print(f"You withdrew ${amount}")
        else:
            temp = self.balance
            self.balance -= 5 #fee for insufficient funds
            print(f"Insufficient Funds. You cannot withdraw ${amount} from ${temp}  A $5 fee will be applied")
        return self

#tested and working
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.account_info()




#END CHECKING ACOUNT




#SAVINGS ACCOUNT
class BankAccount_Savings:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount_Savings.accounts.append(self)

#tested and working
    def account_info(self):
        print(f"Your Checking Account balance is ${self.balance} with an interest rate of {self.int_rate}%")
        return self

#tested and working
    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited ${amount}")
        return self

#tested and working
    def yield_interest(self):
        temp = self.balance
        if self.balance > 0:    
            interest = self.balance * 1 + self.int_rate - temp
            print(f"Your interest is ${interest}")
        return self

#tested and working
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount_Savings.can_withdraw(self.balance,amount):
            temp = self.balance
            self.balance -= amount
            print(f"You withdrew ${amount}")
        else:
            temp = self.balance
            self.balance -= 5 #fee for insufficient funds
            print(f"Insufficient Funds. You cannot withdraw ${amount} from ${temp}  A $5 fee will be applied")
        return self

#tested and working
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

#END SAVINGS ACCOUNT



    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.account_info()








    def transfer_to_savings(cls):
        for transfers in cls.accounts:

            if BankAccount_Checking.can_withdraw(self.balance,amount):
                temp = self.balance
                self.balance -= amount
                BankAccount_Savings.balance += amount
            else:
                temp = self.balance
                self.balance -= 5 #fee for insufficient funds
                print(f"Insufficient Funds. You cannot withdraw ${amount} from ${temp}  A $5 fee will be applied")
            return self







# # print balance
# print(BankAccount_Checking.checking_bal, BankAccount_Savings.savings_bal)










#USER INFO

class User:
    population = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.checking = BankAccount_Checking(.2, 0)
        self.savings = BankAccount_Savings(.2, 0)
        User.population += 1

    def greeting(self):
        print(f"Hello, My name is {self.first_name}!")


#MAKE DEPOSITS
    def savings_deposite(self,amount):
        self.savings.deposit(amount)
    def checking_deposite(self,amount):
        self.checking.deposit(amount)

#MAKE WITHDRAWALS
    def savings_withdrawal(self,amount):
        self.savings.with_draw(amount)
    def checking_withdrawal(self,amount):
        self.checking.with_draw(amount)

#CHECK BALANCE
    def check_balances(self):
        self.checking.print_all_accounts()

#Make Transfers
    def transfer_to_savings(self,amount):
        self.checking.transfer_to_savings(amount)


mike = User("Mike","Jordon",45)

print("---------------greating test")
mike.greeting()


print("---------------balance test")
mike.check_balances()


print("---------------deposite test")
mike.checking_deposite(500)
mike.savings_deposite(300)


print("---------------deposite test")
mike.checking_withdrawal(126)
mike.savings_withdrawal(205)

# mike.transfer_to_checking()
# mike.transfer_to_savings()

print("--------all accounts------")
BankAccount_Checking.print_all_accounts()


mike.transfer_to_savings(200)
mike.check_balances()