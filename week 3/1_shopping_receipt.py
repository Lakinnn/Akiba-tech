print("=" * 5, "SHOPPING RECEIPT", "=" * 5)

items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Laptop", "price": 50000, "quantity": 8},
]


def calculate_subtotal(items):
    for item in items:
        if item["price"] < 0 or item["quantity"] < 0:
            raise ValueError("Price and quantity cannot be negative.")

    return sum(
        item["price"] * item["quantity"]
        for item in items
    )


def calculate_discount(subtotal):
    if subtotal < 1000:
        return 0
    elif subtotal < 3000:
        return subtotal * 0.05
    else:
        return subtotal * 0.10


def calculate_tax(amount, tax_rate):
    return amount * tax_rate


def generate_receipt(items, tax_rate):
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    discounted_amount = subtotal - discount
    tax = calculate_tax(discounted_amount, tax_rate)
    final_amount = discounted_amount + tax

    receipt = []
    receipt.append("===== PURCHASE SUMMARY =====")

    for item in items:
        item_total = item["price"] * item["quantity"]
        receipt.append(
            f'{item["name"]}: {item["quantity"]} x '
            f'{item["price"]:.2f} = {item_total:.2f} Birr'
        )

    receipt.append("-" * 28)
    receipt.append(f"Subtotal: {subtotal:.2f} Birr")
    receipt.append(f"Discount: {discount:.2f} Birr")
    receipt.append(f"Tax: {tax:.2f} Birr")
    receipt.append(f"Final amount: {final_amount:.2f} Birr")

    return "\n".join(receipt)


try:
    tax_percent = float(input("Enter tax rate (%): "))
    tax_rate = tax_percent / 100

    print(generate_receipt(items, tax_rate))

except ValueError as error:
    print("Error:", error)
