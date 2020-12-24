
class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account_balance=0
    def make_deposit(self, amount):
        if amount >= 0:
            self.account_balance += amount
        else:
            print("Cannot be negative")
    def make_withdrawal(self, amount):
        if amount >= 0:
            self.account_balance -= amount
        else:
            print("Cannot be negative ")
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
    def transfer_money(self, other_user, amount):
        if amount < self.account_balance:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
        else:
            print("not enough money")


a=User("jack", "jack@yahoo.com")
b=User("Jill", "jill@gmail.com")
c=User("dog", "dog@gmail.com")

a.make_deposit(20)
a.make_deposit(110)
a.make_deposit(10000)
a.make_withdrawal(10000)
a.display_user_balance()

b.make_deposit(20)
b.make_deposit(110)
b.make_withdrawal(10)
b.make_withdrawal(1)
b.display_user_balance()

c.make_deposit(2000)
c.make_withdrawal(110)
c.make_withdrawal(1032)
c.make_withdrawal(24)
c.display_user_balance()

a.transfer_money(c, 20)
a.display_user_balance()
c.display_user_balance()

