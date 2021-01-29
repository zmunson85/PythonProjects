class User:
    def __init__(self, name, email_address):  # now our method has 2 parameters!
        self.name = name			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        self.account_balance += amount

        print(self.account_balance)
        return self

    def withdraw(self, money):
        self.account_balance -= money
        print(self.account_balance)

        return self


guido = User(name="Guido van Rossum", "guido@python.com")
monty = User(name="Monty Python", email_address="monty@python.com")
guido.make_deposit(100).withdraw(200)
