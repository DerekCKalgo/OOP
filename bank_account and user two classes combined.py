class User:
    def __init__(self, name, email, int_rate, balance=0):
        self.name=name
        self.email=email
        self.account=BankAccount(int_rate, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
    def transfer_money(self, other_user, amount):
        if amount < self.account.balance:
            self.account.withdraw(amount)
            other_user.deposit(amount)
        else:
            print("not enough money")
        return self

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            print("Cannot be negative")
        return self
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance*self.int_rate)
        return self

a=User("derek", "d@gmail.com", 0.01, 100)
a.make_deposit(100)
a.make_withdrawal(40)
a.display_user_balance()
