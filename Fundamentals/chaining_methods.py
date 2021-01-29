class User:
    def __init__(self, name, email_address):  # now our method has 2 parameters!
        self.name = name			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0

    def display(self):
        print("Available Balance=", self.name, self.account_balance)

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        self.account_balance += amount

        print(self.account_balance)
        return self

    def make_withdraw(self, money):
        self.account_balance -= money
        print(self.account_balance)

        return self


guido = User(name="Guido van Rossum", email_address="guido@python.com")
monty = User(name="Monty Python", email_address="monty@python.com")
guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdraw(50)
guido.display()
monty.make_deposit(2500).make_withdraw(250).make_deposit(400)
monty.display()
