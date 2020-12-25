
class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
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

a=BankAccount(0.01, 100)
a.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()
b=BankAccount(0.01)
b.deposit(100).deposit(200).withdraw(50).withdraw(29).withdraw(10).withdraw(15).yield_interest().display_account_info()
