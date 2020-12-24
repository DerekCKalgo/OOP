
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
            print("Cannot be negative")
    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
    def transfer_money(self, other_user, amount):
        if amount < self.account_balance:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
        else:
            print("not enough money")


derek=User("Derek Kong", "derkoman@yahoo.com")
derek.make_deposit(40)
derek.display_user_balance()
apple=User("Apple Cai", "caimiao215@gmail.com")
apple.display_user_balance()
derek.transfer_money(apple, 10)
derek.display_user_balance()
apple.display_user_balance()
