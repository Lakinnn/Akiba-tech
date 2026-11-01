class BankAccount:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print(f"{amount:.2f} Birr deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Withdrawal denied: insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount:.2f} Birr withdrawn successfully.")

    def display_balance(self):
        print(f"{self.owner}'s balance: {self.balance:.2f} Birr")


account1 = BankAccount("Abebe", 1000)
account2 = BankAccount("Sara", 2000)

print("\nAccount 1 transactions")
account1.display_balance()
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(2000)
account1.display_balance()

print("\nAccount 2 transactions")
account2.display_balance()
account2.deposit(1000)
account2.withdraw(250)
account2.withdraw(500)
account2.display_balance()

# When a withdrawal is greater than the available balance, the withdrawal
# is rejected and the balance remains unchanged.