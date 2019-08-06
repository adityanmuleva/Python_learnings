class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for {}".format(name))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("your account has been credited + ")
            self.mini_statement()

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            print("Your account has been debited - ")
            self.mini_statement()
        else:
            print("You don't have enough balance")
            self.mini_statement()

    def mini_statement(self):
        print("Your remaining balance is {} :".format(self.balance))


Aaditya = Account("Aaditya Muleva", 0)
Aaditya.deposit(1000)
Aaditya.withdraw(500)
Aaditya.withdraw(600)
