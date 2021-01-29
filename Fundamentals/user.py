class User:
    def __init__(self, name, email_address):  # now our method has 2 parameters!
        self.name = name			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        self.account_balance += amount

    def make_withdraw(self, money):
        self.account_balance -= money
        print(self.account_balance)

    def transfer(self, amount, name):
        self.account_balance = self.account_balance - amount
        name.account_balance = name.account_balance + amount
        return self.account_balance

    def display(self):
        print("Available Balance=", self.name, self.account_balance)


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
anna = User("anna boNana", "abc123@email.com")

anna.make_deposit(1000)
anna.make_deposit(200)
anna.make_deposit(2500)
guido.make_deposit(500)
guido.make_deposit(250)
guido.make_withdraw(751)
anna.transfer(100, guido)
guido.display()
anna.display()
