#chaining adds return self at the end of each method but not the constructor method.
#This will return the instance itself after each call so no need to call the object again.
#This reduces the code at calling.  a.make deposit(200) a.displayuserbalance  bceomes a.make depost(200).displayuserbalance

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
        return self
    def make_withdrawal(self, amount):
        if amount >= 0:
            self.account_balance -= amount
        else:
            print("Cannot be negative ")
        return self
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
        return self
    def transfer_money(self, other_user, amount):
        if amount < self.account_balance:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
        else:
            print("not enough money")
        return self


a=User("jack", "jack@yahoo.com")
b=User("Jill", "jill@gmail.com")
c=User("dog", "dog@gmail.com")

a.make_deposit(20).make_deposit(110).make_deposit(10000).make_withdrawal(10000).display_user_balance()

b.make_deposit(20).make_deposit(110).make_withdrawal(10).make_withdrawal(1).display_user_balance()

c.make_deposit(2000).make_withdrawal(110).make_withdrawal(1032).make_withdrawal(24).display_user_balance()

a.transfer_money(c, 20).display_user_balance()
c.display_user_balance()

