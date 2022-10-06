
class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)


#tested and working
    def account_info(self):
        print(f"Your account balance is ${self.balance} with an interest rate of {self.int_rate}%")
        return self


#tested and working
    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited ${amount}, your new balance is ${self.balance}")
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
        if BankAccount.can_withdraw(self.balance,amount):
            temp = self.balance
            self.balance -= amount
            print(f"You withdrew ${amount} from ${temp} your new balance is ${self.balance}")
        else:
            temp = self.balance
            self.balance -= 5 #fee for insufficient funds
            print(f"Insufficient Funds. You cannot withdraw ${amount} from ${temp}  A $5 fee will be applied")
            print(f"Your balance is now ${self.balance}")
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
        sum = 0
        for account in cls.accounts:
            account.account_info()
        return sum





# create account
mikes_bank = BankAccount(2 , 800)
toms_bank = BankAccount(3 , 5000)


print("------check withdraw function-------")
toms_bank.with_draw(4900) 
print("------check overdraft function------")
toms_bank.with_draw(150)


print("-------test second account withdraw and deposit--------")
mikes_bank.with_draw(2)

mikes_bank.deposit(500)


print("------toms acct info------")
toms_bank.account_info()

print("-----toms 'yield' ------") 
toms_bank.yield_interest()


print("------test mikes account chaining------")
mikes_bank.account_info().deposit(400).deposit(300).deposit(1000).with_draw(1500).yield_interest().account_info() 

print("------test toms account chaining-------")
toms_bank.deposit(4245).deposit(7654).with_draw(234).with_draw(34).with_draw(764).with_draw(908).yield_interest().account_info()


print("--------all accounts------")
BankAccount.print_all_accounts()
