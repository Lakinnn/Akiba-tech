class BankAccount:
    def __init__(self, account_holder, opening_balance=0):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.account_holder = account_holder  # Public attribute
        self.__balance = opening_balance     # Name-mangled attribute

    def deposit(self, amount):
        if amount < 0:
            print("Invalid deposit: amount cannot be negative.")
            return False

        self.__balance += amount
        print(f"Deposited {amount:.2f}.")
        return True

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid withdrawal: amount cannot be negative.")
            return False

        if amount > self.__balance:
            print("Withdrawal denied: insufficient funds.")
            return False

        self.__balance -= amount
        print(f"Withdrew {amount:.2f}.")
        return True

    def get_balance(self):
        return self.__balance


account = BankAccount("Liya", 500)

account.deposit(200)
account.withdraw(100)
account.withdraw(1000)

print(f"Account holder: {account.account_holder}")
print(f"Current balance: {account.get_balance():.2f}")

# Direct access using account.__balance is not available normally.
# Use get_balance() to read the balance.

"""Answers

What is encapsulation?

  Encapsulation means keeping data and the methods that work with it together in a class, while controlling how that data is accessed or changed.

Why use private attributes?

  Private attributes help prevent accidental changes from outside the class. The class can validate changes through methods such as deposit() and withdraw().

What is name mangling in Python?

  When an attribute begins with two underscores, such as __balance, Python internally changes its name to include the class name. 
  This makes accidental access or overriding less likely, but it is not strong security.

What are public, protected, and private naming conventions?

• name — public; intended to be accessed from anywhere.

• _name — protected convention; signals that it is mainly for the class and its subclasses. Python does not enforce this restriction.

• __name — private-style convention; Python applies name mangling, but the attribute is still not truly inaccessible.
"""
