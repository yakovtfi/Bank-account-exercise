class Bankaccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def transfer_funds(self, amount, other_account=None):
        if other_account is None:
            return self.withdraw(amount)
        if self.withdraw(amount):
            other_account.deposit(amount)
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def __str__(self):
        return f"Account holder: {self.account_holder}, Balance: {self.balance}"


account1 = Bankaccount("Yakov", 1000)
account2 = Bankaccount("Joni", 500)

print(account1)
print(account2)

account1.transfer_funds(200, account2)

print(account1)
print(account2)
