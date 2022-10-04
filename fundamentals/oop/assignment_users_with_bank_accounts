###CHECKING ACCOUNT 
# CHECKING ACCOUNT CONSTRUCTOR
class BankAccount_Checking:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount_Checking.accounts.append(self)

# CHECKING ACCOUNT INFO
    def account_info(self):
        print(f"Your Checking Account balance is ${self.balance}")
        print(f"Your Savings Account balance is ${self.savings.balance} with an interest rate of {self.savings.int_rate}%")
        return self


# CHECKING DEPOSITE
    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited ${amount}")
        return self

# CHECKING YIELD 
    def yield_interest(self):
        temp = self.balance
        if self.balance > 0:    
            interest = self.balance * 1 + self.int_rate - temp
            print(f"Your interest is ${interest}")
        return self


# CHECKING WITHDRAWAL
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

# CHECKING OVERDRAFT BALANCE CHECK - STATIC METHOD
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

# ALL ACCOUNTS METHOD - STILL NOT SURE IF NEEDED
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.account_info()

#####END CHECKING ACOUNT




######SAVINGS ACCOUNT

# SAVINGS ACCOUNT CONSTRUCTOR
class BankAccount_Savings:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount_Savings.accounts.append(self)

# SAVINGS ACCOUNT INFO
    def account_info(self):
        print(f"Your Checking Account balance is ${self.balance} with an interest rate of {self.int_rate}%")
        return self

# SAVINGS DEPOSIT
    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited ${amount}")
        return self

# SAVINGS YIELD
    def yield_interest(self):
        temp = self.balance
        if self.balance > 0:    
            interest = self.balance * 1 + self.int_rate - temp
            print(f"Your interest is ${interest}")
        return self

# SAVINGS WITHDRAWAL
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

# SAVINGS OVERDRAFT BALANCE CHECK - STATIC METHOD
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

# PRINT ALL ACCOUNTS -- STILL NOT SURE IF NEEDED
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.account_info()


######END SAVINGS ACCOUNT





####USER INFO

class User:
    population = 0
#CONSTRUCT USER -- INCLUDING LINKING ACCOUNTS
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.checking = BankAccount_Checking(.2, 0)
        self.savings = BankAccount_Savings(.2, 0)
        User.population += 1


#USER GREATING
    def greeting(self):
        print(f"Hello, My name is {self.first_name}!")


#MAKE TRANSFER TO CHECKING
    def transfer_to_checking(self, amount):
        if self.savings.balance >= amount:
            self.savings.with_draw(amount)
            self.checking.deposit(amount)
        else:
            print("insuficient funds to complete transaction")

#MAKE TRANSFER TO SAVINGS
    def transfer_to_savings(self, amount):
        if self.checking.balance >= amount:
            self.checking.with_draw(amount)
            self.savings.deposit(amount)
        else:
            print("insuficient funds to complete transaction")

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
        print(f"Your Checking Account balance is ${self.checking.balance}")
        print(f"Your Savings Account balance is ${self.savings.balance}")


#### END USER INFO




# FUNCTION TESTS!!


#BUILD A BANKER
mike = User("Mike","Jordon",45)
#TEST
print("---------------greating test")
mike.greeting()


print("---------------balance test")
mike.check_balances()


print("---------------deposite test")
mike.checking_deposite(500)
mike.savings_deposite(300)


print("---------------withdraw test")
mike.checking_withdrawal(126)
mike.savings_withdrawal(205)



print("--------rechecking all account balances------")
mike.check_balances()


print("--------transfer to checking test and check balance------")
mike.transfer_to_checking(20)
mike.check_balances()


print("--------transfer to savings test and check balance------")
mike.transfer_to_savings(350)
mike.check_balances()
