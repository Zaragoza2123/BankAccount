class BankAccount:
    all_accounts = []
    def __init__(self, int_rate=.01, balance = 0): 
        self.balance = balance
        self.int_rate= int_rate
        if balance > 0:
            self.balance = balance 
        BankAccount.all_accounts.append(self)
    @classmethod
    def all_instantces(cls):
        for account in cls.all_accounts:
            account.display_account_info()
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}, Interste Rate: {self.int_rate}" )
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate) 
        return self

acc1 = BankAccount(balance=100)
acc2 = BankAccount()

acc1.deposit(100).deposit(100).deposit(100).withdraw(300).yield_interest().display_account_info()

acc2.deposit(1000).deposit(1000).withdraw(500).withdraw(500).withdraw(300).withdraw(300).yield_interest().display_account_info()
BankAccount.all_instantces()

