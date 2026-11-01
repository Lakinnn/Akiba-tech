class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"Product: {self.name}, "
            f"Price: {self.price:.2f} Birr, "
            f"Quantity: {self.quantity}"
        )

    def total_value(self):
        return self.price * self.quantity


product1 = Product("Notebook", 100, 5)
product2 = Product("Pen", 15, 20)
product3 = Product("Backpack", 750, 3)

print("\nProducts")
print(product1)
print("Total value:", product1.total_value(), "Birr")

print(product2)
print("Total value:", product2.total_value(), "Birr")

print(product3)
print("Total value:", product3.total_value(), "Birr")

# The __str__() method controls what is displayed when an object is
# passed directly to print(). It provides a readable description.