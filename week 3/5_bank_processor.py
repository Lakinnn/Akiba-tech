print("===== Bank Processor =====")

def create_account(opening_balance=0, daily_withdrawal_limit=1000):
    if opening_balance < 0:
        raise ValueError("Opening balance cannot be negative.")

    if daily_withdrawal_limit < 0:
        raise ValueError("Daily withdrawal limit cannot be negative.")

    return {
        "balance": opening_balance,
        "daily_withdrawal_limit": daily_withdrawal_limit,
        "withdrawn_today": 0,
        "transactions": []
    }


def record_transaction(account, transaction_type, amount):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": account["balance"]
    }

    account["transactions"].append(transaction)


def deposit(account, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be greater than zero.")

    account["balance"] += amount
    record_transaction(account, "deposit", amount)


def withdraw(account, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")

    if amount > account["balance"]:
        raise ValueError("Withdrawal exceeds the current balance.")

    remaining_limit = (
        account["daily_withdrawal_limit"]
        - account["withdrawn_today"]
    )

    if amount > remaining_limit:
        raise ValueError(
            f"Withdrawal exceeds the remaining daily limit of "
            f"{remaining_limit:.2f}."
        )

    account["balance"] -= amount
    account["withdrawn_today"] += amount

    record_transaction(account, "withdrawal", amount)


def check_balance(account):
    return account["balance"]


def reset_daily_withdrawals(account):
    account["withdrawn_today"] = 0


def transaction_summary(account):
    total_deposited = sum(
        transaction["amount"]
        for transaction in account["transactions"]
        if transaction["type"] == "deposit"
    )

    total_withdrawn = sum(
        transaction["amount"]
        for transaction in account["transactions"]
        if transaction["type"] == "withdrawal"
    )

    return {
        "total_deposited": total_deposited,
        "total_withdrawn": total_withdrawn,
        "final_balance": account["balance"],
        "transaction_history": account["transactions"]
    }


# Example
account = create_account(
    opening_balance=1000,
    daily_withdrawal_limit=500
)

deposit(account, 500)
withdraw(account, 200)
deposit(account, 300)

print("Current balance:", check_balance(account))

summary = transaction_summary(account)

print("Total deposited:", summary["total_deposited"])
print("Total withdrawn:", summary["total_withdrawn"])
print("Final balance:", summary["final_balance"])
print("Transaction history:")

for transaction in summary["transaction_history"]:
    print(transaction)
